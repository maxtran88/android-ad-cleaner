#!/usr/bin/env python3
"""手机去广告 · 总入口。所有命令都要带 -s <序列号>（adb devices 第一列）。

  python3 tool/run.py devices                      列出连着的手机、型号、系统版本、有没有现成机型脚本
  python3 tool/run.py -s 序列号 check              只读：锁屏、机型脚本匹配、广告包挂起状态
  python3 tool/run.py -s 序列号 ui-check           只读：检查手机读屏服务，不点击任何开关
  python3 tool/run.py -s 序列号 backup             改动前快照，存到 backups/<型号>-<时间>/
  python3 tool/run.py -s 序列号 recipe [段名 …]     跑本机型机型脚本（不带段名=全跑）
  python3 tool/run.py -s 序列号 chan-scan          只读：列出开着的营销通知渠道 → backups/.../channels.tsv
  python3 tool/run.py -s 序列号 chan-off 清单.tsv   关掉清单里的渠道
  python3 tool/run.py -s 序列号 chan-on  清单.tsv   还原
  python3 tool/run.py -s 序列号 suspend 包名 …       挂起广告包（先征得机主同意），记录到 backups/.../suspended.txt
  python3 tool/run.py -s 序列号 unsuspend [包名 …]   解除挂起（不给包名=解除记录里的全部）
  python3 tool/run.py -s 序列号 quickapp          只读：检测快应用组件（装没装、挂没挂、在不在跑、用没用过）
  python3 tool/run.py -s 序列号 quickapp off      关闭快应用：挂起全部快应用组件（先征得机主同意）
  python3 tool/run.py -s 序列号 quickapp on       恢复快应用
  python3 tool/run.py -s 序列号 finish             收尾：插电常亮改回备份时的值，提醒关闭开发者模式
  python3 tool/run.py -s 序列号 dev-off --yes      从电脑上关闭开发者模式和 USB 调试（执行后电脑与手机断开）
  python3 tool/run.py -s 序列号 status-json        只读：一次输出全部状态（JSON，给图形界面用）
"""
import datetime, glob, json, os, re, shutil, subprocess, sys
from pathlib import Path
for _st in (sys.stdout, sys.stderr):
    try:
        _st.reconfigure(encoding="utf-8", errors="replace")   # Windows 控制台默认不是 UTF-8
    except Exception:
        pass
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import adb_link
import troubleshooting
from i18n import t, extract_lang_args, current_lang

# --lang on the command line is honoured before any module-level output
# (e.g. the adb-missing exit below); main() re-applies it to its own argv.
extract_lang_args(sys.argv[1:])

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOL = os.path.join(ROOT, "tool")
BACKUPS = os.environ.get("AAC_BACKUPS") or os.path.join(ROOT, "backups")

# 各品牌常见的系统广告包（快应用另列在 QUICKAPP）。只在机主同意后挂起；挂起可一条命令还原。
AD_PKGS = {
    "OPPO": ["com.opos.ads", "com.heytap.pictorial"],
    "OnePlus": ["com.opos.ads", "com.heytap.pictorial"],
    "realme": ["com.opos.ads", "com.heytap.pictorial"],
    "HONOR": [],
    "Xiaomi": ["com.miui.systemAdSolution"],
    "Redmi": ["com.miui.systemAdSolution"],
    "vivo": [],
}

# 快应用组件：免安装的「轻 App」，广告常用 hap:// 链接把人跳进去。
# (包名, 名称, 品牌, 是否实测过挂起)
QUICKAPP = [
    ("com.nearme.instant.platform", "快应用平台", "OPPO / 一加 / realme", True),
    ("com.oppo.instant.local.service", "快应用本地服务", "OPPO / 一加 / realme", True),
    ("com.nearme.instant.card", "快应用卡片", "OPPO / 一加 / realme", True),
    ("com.hihonor.quickengine", "快应用引擎", "荣耀", True),
    ("com.hihonor.quickgame", "快游戏", "荣耀", True),
    ("com.honor.quickgamecenter", "快游戏中心", "荣耀", True),
    ("com.huawei.fastapp", "快应用中心", "华为", False),
    ("com.miui.hybrid", "快应用服务框架", "小米 / Redmi", False),
    ("com.miui.hybrid.accessory", "快应用服务框架辅件", "小米 / Redmi", False),
    ("com.vivo.hybrid", "快应用", "vivo / iQOO", False),
]
# 挂了会坏功能的包，不许挂
QUICKAPP_NAME_KEY = {
    "com.nearme.instant.platform": "cli.quickapp.name.platform",
    "com.oppo.instant.local.service": "cli.quickapp.name.local_service",
    "com.nearme.instant.card": "cli.quickapp.name.card",
    "com.hihonor.quickengine": "cli.quickapp.name.engine",
    "com.hihonor.quickgame": "cli.quickapp.name.quickgame",
    "com.honor.quickgamecenter": "cli.quickapp.name.gamecenter",
    "com.huawei.fastapp": "cli.quickapp.name.center",
    "com.miui.hybrid": "cli.quickapp.name.framework",
    "com.miui.hybrid.accessory": "cli.quickapp.name.accessory",
    "com.vivo.hybrid": "cli.quickapp.name.vivo",
}

NEVER = {"com.heytap.quicksearchbox", "com.coloros.assistantscreen", "com.android.systemui",
         "com.vivo.systemuiplugin", "com.heytap.market", "com.xiaomi.market", "com.hihonor.appmarket"}


def adb_bin():
    for c in (os.environ.get("ADB"), shutil.which("adb"),
              os.path.expanduser("~/Library/Android/sdk/platform-tools/adb"),
              os.path.expanduser("~/platform-tools/adb"), os.path.expanduser("~/android-tools/platform-tools/adb")):
        if c and os.path.exists(c):
            return c
    sys.exit(t("cli.errors.no_adb", default="找不到 adb。安装方法见 docs/01-准备工作.md"))


ADB = adb_bin()


def adb_shell(serial, cmd):
    """手机掉线时等它回来重试一次；仍不在就停止本步骤（Issue #147：以前读到空结果仍显示成功）。"""
    for attempt in range(2):
        r = subprocess.run([ADB, "-s", serial, "shell", cmd], capture_output=True, text=True, encoding="utf-8", errors="replace",
                           creationflags=0x08000000 if os.name == "nt" else 0)
        if not (r.returncode and adb_link.client_gone(r.stderr)):
            return r
        if attempt or not adb_link.wait_for(serial, ADB):
            sys.exit(str(adb_link.lost(r.stderr)))


def sh(serial, cmd, check=False):
    return adb_shell(serial, cmd).stdout.strip()


def sh_all(serial, cmd):
    """stdout + stderr：pm suspend 失败的原因在 stderr 里。"""
    r = adb_shell(serial, cmd)
    return (r.stdout + r.stderr).strip()


MSA = "com.miui.systemAdSolution"


def msa_net(serial, enable):
    """仅用本系统确实提供的接口；Android 13 等旧系统不伪报断网成功。"""
    help_text = sh_all(serial, "cmd connectivity help")
    required = ["set-package-networking-enabled", "get-package-networking-enabled"]
    if not enable:
        required += ["set-chain3-enabled", "get-chain3-enabled"]
    if not all(re.search(r"(?m)^\s*" + re.escape(command) + r"(?:\s|$)", help_text) for command in required):
        return {"ok": False, "supported": False, "reason": t("cli.msa.unsupported", default="本系统不支持 msa 断网接口；仅挂起仍可能出现广告")}
    commands = [f"cmd connectivity set-package-networking-enabled {'true' if enable else 'false'} {MSA}"]
    if not enable:
        commands.append("cmd connectivity set-chain3-enabled true")
    for command in commands:
        result = sh_all(serial, command)
        if re.search(r"unknown command|exception|permission denial|error|not supported|denied", result, re.I):
            return {"ok": False, "supported": True, "reason": t("cli.msa.rejected", detail=result[-180:], default="系统拒绝更改 msa 网络状态：{detail}")}
    result = sh_all(serial, f"cmd connectivity get-package-networking-enabled {MSA}").strip().lower()
    # HyperOS 实机返回「包名:allow/deny」，部分接口返回布尔值；不接受错误信息中的碰巧匹配。
    expected = {"true", f"{MSA}:allow".lower()} if enable else {"false", f"{MSA}:deny".lower()}
    ok = result in expected
    if ok and not enable:
        chain = sh_all(serial, "cmd connectivity get-chain3-enabled").strip().lower()
        ok = chain in {"chain:enabled", "true"}
    return {"ok": ok, "supported": True, "reason": "" if ok else t("cli.msa.verify_failed", default="msa 网络状态回读未确认成功")}


def prop(serial, k):
    return sh(serial, f"getprop {k}")


def info(serial):
    return {
        "brand": prop(serial, "ro.product.brand"),
        "model": prop(serial, "ro.product.model"),
        "name": prop(serial, "ro.vendor.oplus.market.name") or prop(serial, "ro.product.marketname") or prop(serial, "ro.product.vendor.marketname"),
        "build": prop(serial, "ro.build.display.id"),
        "os": prop(serial, "ro.mi.os.version.incremental") or prop(serial, "ro.build.version.opporom")
              or prop(serial, "ro.vivo.os.build.display.id") or prop(serial, "ro.build.version.magic"),
        "android": prop(serial, "ro.build.version.release"),
    }


FAMILY = {"oppo": "oppo", "oneplus": "oppo", "realme": "oppo", "honor": "honor",
          "xiaomi": "xiaomi", "redmi": "xiaomi", "poco": "xiaomi", "vivo": "vivo", "iqoo": "vivo"}


def recipe_meta(path):
    with open(path, encoding="utf-8") as f:
        src = f.read()
    m = re.search(r'^BUILD\s*=\s*"([^"]*)"', src, re.M)
    models = re.search(r'^MODELS\s*=\s*\[([^\]]*)\]', src, re.M)
    return {"build": m.group(1) if m else "", "steps": re.findall(r'^@step\("([^"]+)"\)', src, re.M),
            "models": re.findall(r'"([^"]+)"', models.group(1)) if models else []}


def recipe_for(model, brand=""):
    """返回 (路径, 是否参考)。先找本型号（目录名或脚本里的 MODELS）；没有就找同品牌别的机型，作参考。"""
    allr = sorted(glob.glob(os.path.join(ROOT, "recipes", "*", "recipe.py")))
    for r in allr:
        d = os.path.basename(os.path.dirname(r))
        if d.endswith("-" + model) or model in recipe_meta(r)["models"]:
            return r, False
    fam = FAMILY.get((brand or "").lower())
    for r in allr:
        if fam and os.path.basename(os.path.dirname(r)).startswith(fam + "-"):
            return r, True
    return None, False


def build_ok(i, rb):
    """录制版本 rb 和这台对不对得上：比 ro.build.display.id，小米再比 HyperOS 版本号。"""
    return (not rb) or i["build"].startswith(rb) or (i.get("os") or "").startswith(rb)


def input_blocked(serial, brand):
    """小米系没开「USB 调试（安全设置）」时，电脑发出的点击会被拒。KEYCODE_UNKNOWN 不触发任何操作。"""
    if FAMILY.get((brand or "").lower()) != "xiaomi":
        return False
    return troubleshooting.input_blocked(sh_all(serial, "input keyevent 0"))


def locked(serial):
    return "isKeyguardShowing=true" in sh(serial, "dumpsys window | grep -m1 isKeyguardShowing") or \
           "mDreamingLockscreen=true" in sh(serial, "dumpsys window | grep -m1 mDreamingLockscreen")


def latest_backup(serial, create=False):
    m = info(serial)["model"]
    hits = sorted(glob.glob(os.path.join(BACKUPS, f"{m}-*")))
    if hits and not create:
        return hits[-1]
    d = os.path.join(BACKUPS, f"{m}-{datetime.datetime.now():%Y%m%d-%H%M}")
    os.makedirs(d, exist_ok=True)
    return d


def display_backup_path(path):
    """Windows 程序和备份可能位于不同盘符，此时不能计算相对路径。"""
    path = os.fspath(path)
    home = os.path.expanduser("~")
    if os.environ.get("AAC_BACKUPS"):
        return "~" + path[len(home):] if path.startswith(home + os.sep) else path
    try:
        return os.path.relpath(path, ROOT)
    except ValueError:
        return path


def suspended(serial, pkg):
    out = sh(serial, f"dumpsys package {pkg} | grep -m1 -o 'suspended=[a-z]*'")
    return out.endswith("true")


def installed(serial, pkg):
    return "package:" in sh(serial, f"pm path {pkg}")


VIVO_QUICKAPP = "switch_quick_app_service"


def quickapp_switch(serial):
    if prop(serial, "ro.product.brand").lower() not in ("vivo", "iqoo"):
        return None
    value = sh(serial, f"settings --user 0 get secure {VIVO_QUICKAPP}")
    return value if value in ("0", "1") else None


def quickapp_setting_backup(serial):
    """跨多次 backup 找回本设备未还原的记录；不借用另一台同型号手机的设置。"""
    for path in sorted(glob.glob(os.path.join(BACKUPS, "*", "quickapp-setting.json")), reverse=True):
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        if data.get("serial") == serial and data.get("key") == VIVO_QUICKAPP and data.get("original") in ("0", "1"):
            return path, data
    return None, None


def set_quickapp_service(serial, restore=False):
    value = quickapp_switch(serial)
    if value is None:
        raise RuntimeError(t("cli.quickapp.service_unreadable", default="读不到 vivo 快应用服务开关，未修改"))
    path, data = quickapp_setting_backup(serial)
    if restore:
        if data is None:
            raise RuntimeError(t("cli.quickapp.service_no_backup", default="没有找到本设备的快应用开关备份，未按默认值开启；请在手机上手动核对"))
        target = data["original"]
    else:
        if value == "0":
            return t("cli.quickapp.service_already_off", default="快应用服务已经关闭，未改动")
        if path is None:
            path = os.path.join(latest_backup(serial), "quickapp-setting.json")
            # 先落盘再改设置；重复关闭不能把最初原值覆盖成 0。
            with open(path, "x", encoding="utf-8") as f:
                json.dump({"serial": serial, "key": VIVO_QUICKAPP, "original": value}, f)
        target = "0"
    sh(serial, f"settings --user 0 put secure {VIVO_QUICKAPP} {target}")
    if quickapp_switch(serial) != target:
        raise RuntimeError(t("cli.quickapp.service_write_failed", default="快应用服务开关写入后校验失败，保留原值备份"))
    if restore:
        os.remove(path)
    else:
        sh(serial, "am force-stop --user 0 com.vivo.hybrid")
    if restore:
        return t("cli.quickapp.service_restored", target=target, default="快应用服务已恢复原值 {target}")
    return t("cli.quickapp.service_closed", default="快应用服务已关闭")


def quickapps(serial):
    """装着的快应用组件，带状态。"""
    ev = sh(serial, "dumpsys usagestats")
    disabled = set(re.findall(r"^package:(\S+)", sh(serial, "pm list packages --user 0 -d"), re.M))
    out = []
    for pkg, name, brand, tested in QUICKAPP:
        if not installed(serial, pkg):
            continue
        fg = len(re.findall(rf"type=ACTIVITY_RESUMED package={re.escape(pkg)}\b", ev))
        switch = quickapp_switch(serial) if pkg == "com.vivo.hybrid" else None
        is_suspended = suspended(serial, pkg)
        out.append({
            "pkg": pkg, "name": t(QUICKAPP_NAME_KEY[pkg], default=name), "brand": brand, "tested": tested,
            "suspended": is_suspended,
            "closed": is_suspended or switch == "0" or pkg in disabled,   # 以前手动 disable-user 的也算关闭
            "method": "setting" if switch is not None else "suspend",
            "service_switch": switch,
            "running": bool(sh(serial, f"pidof {pkg}") or sh(serial, f"pidof {pkg}:provider")),
            "used": fg,
        })
    return out


def fold_open(serial):
    """折叠屏展开时屏幕接近正方形：引擎会找错位置，要合上用外屏。"""
    m = re.search(r"(\d+)x(\d+)", sh(serial, "wm size").splitlines()[-1] if sh(serial, "wm size") else "")
    if not m:
        return False
    w, h = int(m.group(1)), int(m.group(2))
    return min(w, h) / max(w, h) > 0.8


def record(serial, pkgs, fn="suspended.txt"):
    with open(os.path.join(latest_backup(serial), fn), "a", encoding="utf-8") as f:
        for p in pkgs:
            f.write(p + "\n")


DEV_REMINDER = t("cli.finish.dev_reminder", default='\n================ 最后一步：关闭开发者模式 ================\n收尾不代表每一步都成功，请先核对执行结果。若不再继续排查或重试，建议关闭开发者模式和 USB 调试：\n  · 部分银行、支付、游戏 App 检测到 USB 调试开着会提醒或拒绝运行\n  · 关掉以后，别人拿你的手机插电脑也连不上\n\n两种关法，选一种：\n  1) 手机上：设置 → 搜索「开发者选项」→ 关掉页面最上方的总开关\n  2) 电脑上：python3 tool/run.py -s {s} dev-off --yes\n     （执行后电脑和手机断开，这是正常的）\n\n关掉开发者模式不会撤销这次的改动：关掉的开关、挂起的包、关掉的通知都保持原样。\n以后要还原挂起的包，重新打开开发者模式和 USB 调试即可（见 docs/00-打开开发者模式.md）。\n==========================================================\n')
DEV_REMINDER_GUI = t("cli.finish.dev_reminder_gui", default='\n================ 最后一步：关闭开发者模式 ================\n收尾不代表每一步都成功，请先核对执行结果。若不再继续排查或重试，建议关闭开发者模式和 USB 调试：\n  · 部分银行、支付、游戏 App 检测到 USB 调试开着会提醒或拒绝运行\n  · 关掉以后，别人拿你的手机插电脑也连不上\n\n两种关法，选一种：\n  1) 手机上：设置 → 搜索「开发者选项」→ 关掉页面最上方的总开关\n  2) 电脑上：点客户端完成页的「帮我关闭」\n     （执行后电脑和手机断开，这是正常的）\n\n关掉开发者模式不会撤销这次的改动：关掉的开关、挂起的包、关掉的通知都保持原样。\n以后要还原挂起的包，重新打开开发者模式和 USB 调试即可（见 docs/00-打开开发者模式.md）。\n==========================================================\n')


def py(script, *args):
    return subprocess.call(script_cmd(script, *args))


def script_cmd(script, *args):
    """启动 tool/ 里的另一个脚本。打包版（客户端）里 sys.executable 是客户端本身，
    必须带 --cli，否则会再打开一个客户端窗口、引擎没跑起来（Windows 小米 18 Pro Max 反馈）。"""
    if getattr(sys, "frozen", False):
        return [sys.executable, "--cli", script, *args]
    return [sys.executable, os.path.join(TOOL, script), *args]


def main():
    _, a = extract_lang_args(sys.argv[1:])
    if not a or a[0] in ("-h", "--help"):
        print(t("cli.help.run", default=__doc__)); return
    if a[0] == "devices":
        out = subprocess.run([ADB, "devices"], capture_output=True, text=True, encoding="utf-8", errors="replace").stdout
        rows = [l.split("\t") for l in out.splitlines()[1:] if "\t" in l]
        if not rows:
            print(t("cli.devices.none", default="没有连着的手机。检查数据线、USB 调试，见 docs/01-准备工作.md"))
        for ser, st in rows:
            if st != "device":
                print(f"{ser}\t{st}\t" + t("cli.devices.status_note", default="（unauthorized=手机上点「允许 USB 调试」；offline=重插或重开无线调试）")); continue
            i = info(ser); r, ref = recipe_for(i["model"], i["brand"])
            tag = (os.path.relpath(r, ROOT) + (t("cli.devices.ref_suffix", default="（同品牌参考）") if ref else "")) if r else t("cli.devices.no_recipe", default="无（只能跑通用部分）")
            print(t("cli.devices.row", ser=ser, name=i['name'] or i['brand'] + ' ' + i['model'], model=i['model'], build=i['build'], tag=tag,
                    default="{ser}\t{name}\t{model}\t{build}\t机型脚本：{tag}"))
        return
    if a[0] != "-s" or len(a) < 3:
        sys.exit(t("cli.errors.usage", default="命令格式：run.py -s <序列号> <命令>。先跑 run.py devices 看序列号"))
    s, cmd, rest = a[1], a[2], a[3:]

    if cmd == "ui-check":
        sys.exit(py("fast.py", "-s", s, "check"))

    elif cmd == "check":
        i = info(s); r, ref = recipe_for(i["model"], i["brand"])
        disp = i['name'] if i['name'].upper().startswith(i['brand'].upper()) else i['brand'] + ' ' + i['name']
        print(t("cli.check.model", display=disp, model=i['model'], build=i['build'], android=i['android'],
                default="机型：{display}（{model}），系统 {build}，Android {android}"))
        print(t("cli.check.locked_yes", default="锁屏：是（请机主解锁）") if locked(s) else t("cli.check.locked_no", default="锁屏：否"))
        if input_blocked(s, i["brand"]):
            print(t("cli.check.input_blocked", default="电脑点击：被系统拒绝。") + t("cli.troubleshooting.xiaomi_input", default=troubleshooting.XIAOMI_INPUT))
        if r and ref:
            print(t("cli.check.recipe_ref", path=os.path.relpath(r, ROOT),
                    default="机型脚本：本型号没有；同品牌参考 {path}。要用：recipe --ref（安全模式：只关脚本里点名的开关，找不到就跳过）"))
        elif r:
            rb = recipe_meta(r)["build"]
            ok = build_ok(i, rb)
            verdict = t("cli.check.recipe_match", default="版本一致") if ok else t("cli.check.recipe_mismatch", default="版本不同：用安全模式跑，部分步骤可能找不到入口")
            print(t("cli.check.recipe", path=os.path.relpath(r, ROOT), build=rb or t("cli.check.recipe_unmarked", default="未标"), verdict=verdict,
                    default="机型脚本：{path}；录制版本 {build}，{verdict}"))
        else:
            print(t("cli.check.recipe_none", default="机型脚本：没有。可跑：通知渠道 chan-scan/chan-off、广告包挂起；其余照 docs/清单 手动做，或用 tool/explore.py 探路"))
        for p in AD_PKGS.get(i["brand"], []):
            exists = "package:" in sh(s, f"pm path {p}")
            state = t("cli.check.ad_not_installed", default="未安装") if not exists else (t("cli.check.ad_suspended", default="已挂起") if suspended(s, p) else t("cli.check.ad_not_suspended", default="未挂起"))
            print(t("cli.check.ad_pkg", pkg=p, state=state, default="  广告包 {pkg}：{state}"))
        for q in quickapps(s):
            state = t("cli.quickapp.state_closed", default="已关闭") if q['closed'] else t("cli.quickapp.state_open", default="未关闭")
            method = t("cli.quickapp.method_setting", default="系统服务开关") if q['method'] == 'setting' else t("cli.quickapp.method_suspend", default="挂起状态")
            print(t("cli.check.quickapp", pkg=q['pkg'], name=q['name'], state=state, method=method,
                    default="  快应用 {pkg}（{name}）：{state}（{method}）"))
        print(t("cli.check.stay_on", value=sh(s, 'settings get global stay_on_while_plugged_in'), default="插电常亮：{value}"))

    elif cmd == "backup":
        d = latest_backup(s, create=True)
        Path(d, "info.txt").write_text("\n".join(f"{k}={v}" for k, v in info(s).items()), encoding="utf-8")
        for name, c in [("sys.txt", "pm list packages --user 0 -s"), ("user.txt", "pm list packages --user 0 -3"),
                        ("disabled.txt", "pm list packages --user 0 -d"), ("notif.txt", "dumpsys notification --noredact")]:
            Path(d, name).write_text(sh(s, c), encoding="utf-8")
        st = "\n".join(f"## {n}\n" + sh(s, f"settings list {n}") for n in ("system", "secure", "global"))
        Path(d, "settings-before.txt").write_text(st, encoding="utf-8")
        Path(d, "stay_on.txt").write_text(sh(s, "settings get global stay_on_while_plugged_in"), encoding="utf-8")
        print(t("cli.backup.saved", path=display_backup_path(d), default="快照已存：{path}"))

    elif cmd == "recipe":
        i = info(s); r, ref = recipe_for(i["model"], i["brand"])
        use_ref = "--ref" in rest
        rest = [x for x in rest if x != "--ref"]
        if not r or (ref and not use_ref):
            sys.exit(t("cli.recipe.no_recipe", default="这个型号没有机型脚本。") +
                     (t("cli.recipe.ref_hint", path=os.path.relpath(r, ROOT), default="同品牌有参考脚本 {path}，加 --ref 试用。") if r else "") +
                     t("cli.recipe.docs_hint", default="写法见 docs/04-给新机型写脚本.md"))
        if locked(s):
            sys.exit(t("cli.errors.phone_locked", default="手机锁屏了，请机主解锁后再跑"))
        if ref or not build_ok(i, recipe_meta(r)["build"]):
            os.environ["AAC_REF"] = "1"                 # 安全模式：fast.py 不做整页全关
            print(t("cli.recipe.safe_mode", default="⚠ 安全模式：这份机型脚本不是按这台的型号和系统版本录的。只关脚本里点名的开关，找不到入口的步骤跳过。"))
        stay_on = sh(s, "settings get global stay_on_while_plugged_in")
        try:
            sh(s, "settings put global stay_on_while_plugged_in 7")
            rc = py("fast.py", "-s", s, "run", r, *rest)
        finally:
            sh(s, f"settings put global stay_on_while_plugged_in {int(stay_on) if stay_on.isdigit() else 0}")
        sys.exit(rc)

    elif cmd == "chan-scan":
        d = latest_backup(s)
        result = subprocess.run(script_cmd("chan_fast.py", "-s", s, "scan"),
                                capture_output=True, text=True, encoding="utf-8", errors="replace")
        if result.returncode:
            print(result.stderr or result.stdout, file=sys.stderr)
            sys.exit(result.returncode)
        out = result.stdout
        f = os.path.join(d, "channels.tsv")
        Path(f).write_text(
            t("cli.chan_scan.header", default="# 包名\t渠道id\t渠道名。人工核对：删掉服务类（热点共享、红包、防盗、直播提醒等）后再 chan-off\n") + out, encoding="utf-8")
        print(out); print(t("cli.chan_scan.saved", path=display_backup_path(f), count=out.count(chr(10)), default="候选清单：{path}（共 {count} 条）"))

    elif cmd in ("chan-off", "chan-on"):
        if not rest:
            sys.exit(t("cli.chan_list.usage", default="要给清单文件，比如 backups/<型号>-<时间>/channels.tsv"))
        sys.exit(py("chan_fast.py", "-s", s, cmd.split("-")[1], rest[0]))

    elif cmd == "suspend":
        bad = [p for p in rest if p in NEVER]
        if bad:
            sys.exit(t("cli.suspend.never", bad=bad, default="这些包挂了会坏功能，不挂：{bad}"))
        d = latest_backup(s)
        fail = 0
        with open(os.path.join(d, "suspended.txt"), "a", encoding="utf-8") as f:
            for p in rest:
                out = sh_all(s, f"pm suspend --user 0 {p}")
                if suspended(s, p):
                    f.write(p + "\n")
                    extra = ""
                    if p == MSA:
                        sh(s, f"am force-stop {p}")
                        network = msa_net(s, False)
                        extra = t("cli.suspend.net_off", default="，已禁止联网") if network["ok"] else t("cli.suspend.partial", reason=network["reason"], default="；部分完成：{reason}")
                        if not network["ok"]:
                            fail += 1
                    print(t("cli.suspend.done", pkg=p, extra=extra, default="  {pkg}：已挂起{extra}"))
                else:
                    fail += 1
                    print(t("cli.suspend.failed", pkg=p, reason=(out.splitlines() or [t("cli.errors.no_reason", default="系统没给原因")])[-1][:160], default="  {pkg}：挂起失败（{reason}）"))
        if fail:
            sys.exit(1)

    elif cmd == "unsuspend":
        pk = rest
        if not pk:
            f = os.path.join(latest_backup(s), "suspended.txt")
            pk = sorted(set(open(f, encoding="utf-8").read().split())) if os.path.exists(f) else []
        failures = 0
        for p in pk:
            sh(s, f"pm unsuspend --user 0 {p}")
            extra = ""
            if p == MSA:
                network = msa_net(s, True)
                if network["supported"] and not network["ok"]:
                    failures += 1
                    extra = t("cli.unsuspend.net_restore_failed", reason=network["reason"], default="；联网还原失败：{reason}")
                elif not network["supported"]:
                    extra = t("cli.unsuspend.no_net_api", default="；本机无 msa 断网接口，未更改联网设置")
            still = suspended(s, p)
            failures += still
            state = t("cli.unsuspend.failed", default="解除挂起失败") if still else t("cli.unsuspend.done", default="已恢复挂起状态")
            print(p, state + extra)
        if failures:
            sys.exit(1)

    elif cmd == "quickapp":
        sub = rest[0] if rest else "check"
        qs = quickapps(s)
        if not qs:
            print(t("cli.quickapp.none", default="没有检测到快应用组件。")); return
        if sub == "check":
            print(t("cli.quickapp.detected", count=len(qs), default="检测到 {count} 个快应用组件："))
            for q in qs:
                state = t("cli.quickapp.state_closed", default="已关闭") if q['closed'] else t("cli.quickapp.state_open", default="未关闭")
                running = t("cli.quickapp.running", default="后台在跑") if q['running'] else t("cli.quickapp.not_running", default="没在跑")
                used = t("cli.quickapp.used", count=q['used'], default="近期打开过 {count} 次") if q['used'] else t("cli.quickapp.not_used", default="近期没打开过")
                note = t("cli.quickapp.note_setting", default="  （系统服务开关）") if q['method'] == 'setting' else ("" if q['tested'] else t("cli.quickapp.note_untested", default="  （这个包的挂起效果还没实测）"))
                print(t("cli.quickapp.row", name=q['name'], pkg=q['pkg'], state=state, running=running, used=used, note=note,
                        default="  {name:<10} {pkg:<34} {state}  {running}  {used}{note}"))
            h = sh(s, "pm query-activities --brief -a android.intent.action.VIEW -d hap://app/x")
            who = re.findall(r"^\s*(\S+/\S+)$", h, re.M)
            if all(q["closed"] for q in qs):
                print(t("cli.quickapp.all_closed", default="快应用组件已关闭；系统可能显示「应用无法使用」或「快应用服务已关闭」。恢复：quickapp on"))
            else:
                if who:
                    print(t("cli.quickapp.hap", who=who[0], default="hap:// 链接由 {who} 接管：网页或 App 里的广告可以用这类链接跳进快应用。"))
                print(t("cli.quickapp.close_hint", serial=s, default="关闭：python3 tool/run.py -s {serial} quickapp off（要机主同意，可还原）"))
        elif sub == "off":
            todo = [q["pkg"] for q in qs if not q["closed"] and q["method"] == "suspend"]
            why = {}
            for q in qs:
                if q["method"] == "setting":
                    try:
                        print(set_quickapp_service(s))
                    except (RuntimeError, OSError, ValueError) as e:
                        why[q["pkg"]] = str(e)
            for p in todo:
                why[p] = sh_all(s, f"pm suspend --user 0 {p}")
                if suspended(s, p):
                    sh(s, f"am force-stop --user 0 {p}")
            done = [p for p in todo if suspended(s, p)]
            record(s, done)
            bad = []
            for q in quickapps(s):
                ok = q["closed"]
                reason = "" if ok else "（" + ((why.get(q["pkg"]) or "").splitlines() or [t("cli.errors.no_reason", default="系统没给原因")])[-1][:160] + "）"
                if ok:
                    print(t("cli.quickapp.off_row_closed", name=q['name'], pkg=q['pkg'], default="  {name:<10} {pkg:<34} 已关闭"))
                else:
                    print(t("cli.quickapp.off_row_failed", name=q['name'], pkg=q['pkg'], reason=reason, default="  {name:<10} {pkg:<34} 关闭失败{reason}"))
                if not ok:
                    bad.append(q)
            if not bad:
                print(t("cli.quickapp.off_done", default="快应用组件已关闭。请按常用入口核对效果；恢复：quickapp on"))
            else:
                # Issue #7：vivo 的快应用挂起被系统拒绝。如实报失败，不说「已关闭」
                if current_lang() == "zh":
                    names = "」「".join(q["name"] for q in bad)
                else:
                    names = ", ".join('"' + q["name"] + '"' for q in bad)
                print(t("cli.quickapp.off_failed", count=len(bad), names=names,
                        default="有 {count} 个快应用组件关闭失败。可以在手机上检查快应用服务开关，或仅关掉它的通知：设置 → 通知 → 找到「{names}」→ 关掉「允许通知」。"))
                sys.exit(1)
        elif sub == "on":
            failures = 0
            for q in qs:
                if q["method"] == "setting":
                    try:
                        print(set_quickapp_service(s, restore=True))
                    except (RuntimeError, OSError, ValueError) as e:
                        print(t("cli.quickapp.on_error", err=e, default="  ✗ {err}")); failures += 1
                if q["suspended"]:
                    sh(s, f"pm unsuspend --user 0 {q['pkg']}")
                    failed = suspended(s, q['pkg'])
                    failures += failed
                    state = t("cli.quickapp.on_restore_failed", default="还原挂起失败") if failed else t("cli.quickapp.on_unsuspended", default="已解除挂起")
                    print(t("cli.quickapp.on_row", name=q['name'], state=state, default="  {name}: {state}"))
            if failures:
                sys.exit(1)
        else:
            sys.exit(t("cli.quickapp.usage", default="quickapp 后面跟 check / off / on"))

    elif cmd == "finish":
        f = os.path.join(latest_backup(s), "stay_on.txt")
        v = open(f, encoding="utf-8").read().strip() if os.path.exists(f) else "0"
        sh(s, f"settings put global stay_on_while_plugged_in {v or 0}")
        sh(s, "input keyevent HOME")
        print(t("cli.finish.stay_on", value=v or 0, default="插电常亮已改回 {value}"))
        on = sh(s, "settings get global development_settings_enabled") == "1"
        if on:
            print((DEV_REMINDER_GUI if os.environ.get("AAC_GUI") else DEV_REMINDER).format(s=s))

    elif cmd == "status-json":
        import json
        i = info(s); r, ref = recipe_for(i["model"], i["brand"]); steps, rb, ok = [], "", True
        if r:
            meta = recipe_meta(r)
            steps, rb = meta["steps"], meta["build"]
            ok = (not ref) and build_ok(i, rb)
        ads = [{"pkg": p, "suspended": suspended(s, p)} for p in AD_PKGS.get(i["brand"], []) if installed(s, p)]
        print(json.dumps({
            "info": i, "locked": locked(s),
            "recipe": os.path.relpath(r, ROOT) if r else None, "recipe_ref": ref, "recipe_build": rb, "recipe_ok": ok, "steps": steps,
            "ads": ads, "quickapps": quickapps(s),
            "stay_on": sh(s, "settings get global stay_on_while_plugged_in"),
            "dev": sh(s, "settings get global development_settings_enabled") == "1",
            "backup": os.path.relpath(latest_backup(s), BACKUPS) if glob.glob(os.path.join(BACKUPS, f"{i['model']}-*")) else None,
            "fold_open": fold_open(s),
            "input_blocked": input_blocked(s, i["brand"]),
        }, ensure_ascii=False))

    elif cmd == "dev-off":
        if "--yes" not in rest:
            sys.exit(t("cli.devoff.usage", default="这一步会关闭开发者模式和 USB 调试，电脑随后与手机断开。确认后加 --yes 再执行"))
        print(t("cli.devoff.starting", default="正在关闭开发者模式……执行后电脑会和手机断开，这是正常的。"))
        sh(s, "settings put global adb_wifi_enabled 0; settings put global development_settings_enabled 0; "
              "settings put global adb_enabled 0")
        print(t("cli.devoff.sent", default="已发出关闭指令。请在手机上打开 设置 → 搜索「开发者选项」，确认总开关是关着的。"))
    else:
        print(t("cli.help.run", default=__doc__))


if __name__ == "__main__":
    main()

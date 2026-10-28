# 07 Quick Apps: Detection and Turning Them Off

## What is a Quick App

A Quick App is an "install-free mini program" jointly launched by phone manufacturers: tap a link and it opens, without downloading from a store. OPPO, Xiaomi, vivo, Honor, and Huawei Chinese phones all come with a Quick App framework preinstalled.

The problem is ads: ads in web pages, short-video apps, and novel apps often use links starting with `hap://` to jump you into a Quick App, opening pages like "Read novels", "Claim red packets", or "Mini games". You did not tap "Install", yet it can open, and it can send you push notifications.

## Do I use it?

`quickapp` checks the system's usage records and tells you how many times you opened one recently (links opened manually during testing also count). On a tested OPPO Find N3: two Quick App components were running in the background, and the recent open count was 0.

```text
$ python3 tool/run.py -s <序列号> quickapp
检测到 2 个快应用组件：
  快应用平台      com.nearme.instant.platform        未挂起  后台在跑  近期没打开过
  快应用本地服务    com.oppo.instant.local.service     未挂起  后台在跑  近期没打开过
hap:// 链接由 com.nearme.instant.platform/.dispatch.activity.HapDispatcherActivity 接管：网页或 App 里的广告可以用这类链接跳进快应用。
关闭：python3 tool/run.py -s <序列号> quickapp off（要机主同意，可还原）
```

In English, that output means: 2 Quick App components detected — Quick App Platform (`com.nearme.instant.platform`), not suspended, running in background, not opened recently; Quick App Local Service (`com.oppo.instant.local.service`), same status. `hap://` links are handled by `com.nearme.instant.platform/.dispatch.activity.HapDispatcherActivity`: ads in web pages or apps can use such links to jump into a Quick App. To turn off: `python3 tool/run.py -s <序列号> quickapp off` (requires the owner's consent, can be restored). The original Chinese output above is kept verbatim because it is literal program output.

| Result | Recommendation |
|---|---|
| Not opened recently | Turn it off; it will not affect you |
| Opened recently | Think about whether you actively use it. If a service you use often (for example, bill payment or a transit code) opens from a Quick App, that entry will stop opening after you turn it off |

## Turning off and restoring

```bash
python3 tool/run.py -s <序列号> quickapp        # Detect (read-only)
python3 tool/run.py -s <序列号> quickapp off    # Turn off
python3 tool/run.py -s <序列号> quickapp on     # Restore
```

After turning off, detecting again gives:

```text
$ python3 tool/run.py -s <序列号> quickapp
检测到 2 个快应用组件：
  快应用平台      com.nearme.instant.platform        已挂起  没在跑  近期没打开过
  快应用本地服务    com.oppo.instant.local.service     已挂起  没在跑  近期没打开过
快应用已全部关闭。广告里的 hap:// 链接会弹「应用无法使用」，不会跳进快应用。恢复：quickapp on
```

In English: both components are now suspended and not running, not opened recently. All Quick Apps are closed. An ad's `hap://` link will pop up "App unavailable" and will not jump into a Quick App. Restore with `quickapp on`.

When an ad tries to jump into a Quick App again, the system pops up this prompt; tapping "OK" returns you to the original page:

<p align="center"><img src="../../images/quickapp-blocked.png" width="480" alt="After Quick Apps are turned off, a hap link pops up 'App unavailable'"></p>

### Test record (OPPO Find N3 Collector's Edition, ColorOS 16.0.5, 2026-10-24)

| Step | Result |
|---|---|
| `quickapp off` | 2 components suspended in 2.6 seconds, all background processes exited |
| Opening a `hap://` link | Pops up "App unavailable", Quick App did not start |
| `quickapp on` | 2 components restored, the same link launched a Quick App |
| `quickapp off` again | 2 components suspended, the link was blocked again |

Most models use `pm suspend` (suspend); vivo's system service switch is in the next section:

- Components stay on the phone; nothing is uninstalled or disabled, and system updates are unaffected.
- Suspension limits later launches, but an already-running process may not exit immediately; current source runs `force-stop` after a successful suspension. Icons may still be in the app drawer; do not judge success by whether an icon disappeared.
- `quickapp on` restores with a single command. The suspension record is in `backups/<型号>-<时间>/suspended.txt`.

## Quick App components by brand

| Brand | Package name | Name | Suspension tested |
|---|---|---|---|
| OPPO / OnePlus / realme | `com.nearme.instant.platform` | Quick App Platform | ✅ Find N6, Find X10 Pro Max, Find N3 |
| | `com.oppo.instant.local.service` | Quick App Local Service | ✅ Find N6, Find N3 |
| | `com.nearme.instant.card` | Quick App Card | ✅ Find X10 Pro Max |
| Honor | `com.hihonor.quickengine` | Quick App Engine | ✅ PNM-AN10 |
| | `com.hihonor.quickgame` | Quick Game | ✅ |
| | `com.honor.quickgamecenter` | Quick Game Center | ✅ |
| Xiaomi / Redmi | `com.miui.hybrid` | Quick App Service Framework | Not tested |
| | `com.miui.hybrid.accessory` | Quick App Service Framework Accessory | Not tested |
| vivo / iQOO | `com.vivo.hybrid` | Quick App | ❌ System refuses to suspend; current source prefers the system service switch, see next section |
| Huawei | `com.huawei.fastapp` | Quick App Center | Not tested |

For "Not tested" packages, after suspending, check that commonly used apps still open normally; if there is a problem, restore with `quickapp on` and file an Issue telling us.

## vivo / iQOO system service switch

According to the real-device record in [PR #20](https://github.com/rddmwmddr/android-ad-cleaner/pull/20) for V2547A / OriginOS 7, `switch_quick_app_service=0` can block Quick App entries. Current source only uses it on vivo / iQOO and only when this switch can be read; it does not disable or uninstall apps, and does not handle other `hap://` receivers such as Smart Life.

- `quickapp off` first saves the original value, then writes and reads back to confirm; repeated closing does not overwrite the original value.
- `quickapp on` searches past backups for this device's record and restores it; if no record is found, it reports failure and does not write `1` by default.
- The backup file is `quickapp-setting.json`, inside the ignored `backups/` directory, containing a device identifier; do not upload it publicly.
- The client shows the actual closed state, and no longer mistakes a closed service switch for "not suspended, still on". This round has automatic regression coverage, but still awaits retesting on a vivo phone; the 0.2.0 installer does not include this feature.

## Without a computer

Suspension needs adb. With only a phone, you can do two things:

1. Turn off Quick App notifications: Settings → Notification management → search "Quick App" → turn off "Allow notifications".
2. After jumping into a Quick App, long-press its icon on the home screen and delete the shortcut.

These two steps cannot block ad jumps; they only block push notifications and the home-screen icon.

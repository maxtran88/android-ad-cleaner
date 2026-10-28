# 04 Writing a Recipe for a New Model

A model recipe is a Python file recording "in which app, tap which words, turn off which switches". With a model recipe, the same model finishes in a few minutes.

## Where a model recipe lives

```text
recipes/<品牌>-<型号>/recipe.py
```

`<型号>` is the output of `adb shell getprop ro.product.model`, for example `PLP120`, `M154FF`, `PNM-AN10`. `run.py` matches on this name automatically.

When one recipe applies to several models, write `MODELS = ["M154FF", "2608BPX34C"]` in the recipe, and all those models will use it.

When there is no recipe for your model, `run.py` looks for a same-brand recipe as a reference; it only runs with `recipe --ref`, and it is unticked by default in the client. Reference recipes and recipes whose version does not match both run in **safe mode**: they only turn off switches named in `only=[…]`, and do not turn off a whole page. So write `only` in recipes whenever you can.

## Why each model needs its own recipe

Within the same brand, a different minor system version changes the settings pages. A tested example:

| Model | System | Browser settings entry | Video settings entry |
|---|---|---|---|
| Find N6 | ColorOS 16.0.9 | Bottom ☰ → gear icon | My → Settings → Personalized content management |
| Find X9 Ultra | ColorOS 16.0.10 | Bottom "My" → Settings | Cannot find "My" |

So a model recipe starts by stating the system version it was recorded on (`BUILD`, compared against the start of `ro.build.display.id`, or, for Xiaomi, the HyperOS version `ro.mi.os.version.incremental`). When the version differs, the engine warns and enters safe mode.

Entry names change between old and new versions, so a recipe can be written as "tap if present, skip if absent"; see `maybe()` in `recipes/xiaomi-M154FF/recipe.py`.

**Protective switches**: switches like "Limit ad tracking", "Prevent ad tracking", and "Turn off personalized recommendations" — starting with "Limit / Prevent / Block / Prohibit / Turn off" and related to ads — protect you when turned ON. `p.off()` flips them to "on", so recipes do not need special handling for them.

## What a section of a model recipe looks like

```python
# OPPO Find N6（PLP120，ColorOS 16.0.9）机型脚本
BUILD = "PLP120_16.0.9"          # ro.build.display.id 的开头

@step("软件商店")
def _():
    p.start("com.heytap.market")                 # 拉起 App，关掉开屏弹窗
    p.go("我的", "设置")                          # 点「我的」，直到屏幕上出现「设置」
    p.tap("设置", exact=True, scrolls=0)
    if p.tap("隐私", exact=True):                 # 找到「隐私」就点，找不到会翻页
        p.off(only=["个性化推荐"], page="商店·隐私")   # 只关标题含「个性化推荐」的开关
        p.back()
    if p.tap("服务管理", exact=True):
        p.off(keep=["帮助与客服", "应用安全"], page="商店·服务管理")   # 全关，保留这两项
        p.back()
```

The `@step` definition can simply be copied from the start of an existing model recipe. (The code comments and UI strings above are kept in the original Chinese because they are literal tap targets and comments from the source recipe; the surrounding explanation is in English.)

## Actions provided by the engine

| Action | What it does |
|---|---|
| `p.start(包名, activity=None)` | Launch an app or a specific page |
| `p.setting(关键词, 结果)` | Search for a keyword in system Settings and tap the search result |
| `p.tap(文字, exact=True, scrolls=6)` | Tap the text when found; `scrolls=0` only looks at the current screen, and waits up to 3 seconds while dismissing pop-ups |
| `p.go(文字, 期望)` | Tap the text until the expected text appears |
| `p.off(keep=[], only=None, page="")` | Turn off switches that are on on the current page; `only` turns off only these, `keep` keeps these |
| `p.back(n)` | Press back n times |
| `p.find(文字)` | Only find, do not tap; returns coordinates or None |
| `p.confirm()` | Tap confirm when a confirmation dialog pops up while turning off a switch |
| `p.d.shell(命令)` | Run any shell command |

If the first entry in a section is not found, later entries in that section only look at the current screen and do not scroll; the section ends in a few seconds and does not tap at random.

## Steps to write a model recipe

1. Walk through it manually:

   ```bash
   python3 tool/fast.py -s S ls            # 看当前屏幕上有什么字、什么开关
   python3 tool/fast.py -s S tap 我的 设置   # 一步一步点进去
   python3 tool/fast.py -s S scan          # 到了设置页，列出所有开关
   ```

   (The commands above are kept verbatim, including the Chinese example tap words `我的 设置`, which are the literal on-screen labels on a Chinese phone; the comments translate as: see what words and switches are on the current screen / tap in step by step / once on a settings page, list all switches.)

2. Write the path that works as `@step` sections.
3. For pages that can be launched with an activity, write the activity — fastest and most stable:

   ```bash
   adb -s S shell dumpsys window | grep mCurrentFocus   # 停在设置页时查当前 activity
   ```

   Write it as `p.start("包名", ".settings.XxxActivity")`.

4. Run it once: `python3 tool/run.py -s S recipe 软件商店`.
5. Run it all, note how long it took, and fill it into the README model table.

## Pathfinding tool (experimental)

```bash
python3 tool/explore.py -s S com.heytap.market com.heytap.browser
```

Opens each app's settings pages and sub-pages one by one, lists switches that look ad-related, and outputs `探路-<型号>.tsv`. Read-only; it does not flip switches. On some apps it enters a sub-page and cannot get back, so treat the results as reference only.

## Submitting a PR

1. Create `recipes/<品牌>-<型号>/recipe.py`.
2. Add this model's differences to the corresponding brand checklist in `docs/checklists/`.
3. Add a row to the README model table, stating the test date and time taken.
4. Do not submit the `backups/` directory; it contains your phone's app list and notification records.

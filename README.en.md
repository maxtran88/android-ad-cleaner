# Remove Ads from Your Phone

Turn off system ads, trending searches, news recommendations, and marketing push notifications on Chinese Android phones.

Intro page: **https://rddmwmddr.github.io/android-ad-cleaner/**

> Language: [English](README.en.md) | [Tiếng Việt](README.vi.md) | [中文](README.md)

## Download the Desktop Client

Plug in your phone and click a few buttons. No Python and no AI tool needed.

> **v0.2.5 · 2026-10-27**: Added error-log reporting. When a run fails, you can send the log to the maintainer without a GitHub account; the full content is shown exactly as it will be sent, and it is only sent after you confirm. Serial numbers, user directories, email addresses, phone numbers, and IPs are replaced once in the client and once on the server, and the server keeps reports for 90 days. All fixes from 0.2.4 are retained. Older versions do not update automatically, so please download again; existing backups are kept. See [Changelog](CHANGELOG.md) and [Error Log Reporting](docs/en/12-error-log-reporting.md). Official site: https://ahuamiao.com/sites/other/android-ad-removal-intro.html

Earlier versions already handled Windows local-page timeouts, Honor screenshot out-of-bounds errors, notification-channel misoperation risks, and vivo Quick App and backup issues. The scope and pending verification items for each issue are in [Community Issue Handling](docs/en/09-community-issue-handling.md). Only Android devices connected via adb are supported; native HarmonyOS using HDC is not yet supported.

| Computer | Download | Notes |
|---|---|---|
| Mac · Apple Silicon (M1 and later) | [AndroidAdCleaner-0.2.5-mac-arm64.dmg](https://github.com/rddmwmddr/android-ad-cleaner/releases/download/v0.2.5/AndroidAdCleaner-0.2.5-mac-arm64.dmg) | Signed and notarized by Apple, opens with a double-click |
| Mac · Intel (macOS 11 and above) | [AndroidAdCleaner-0.2.5-mac-intel.dmg](https://github.com/rddmwmddr/android-ad-cleaner/releases/download/v0.2.5/AndroidAdCleaner-0.2.5-mac-intel.dmg) | Same as above |
| Windows 10 / 11 · Installer | [AndroidAdCleaner-0.2.5-windows-setup.exe](https://github.com/rddmwmddr/android-ad-cleaner/releases/download/v0.2.5/AndroidAdCleaner-0.2.5-windows-setup.exe) | If you see "Windows protected your PC", click "More info" → "Run anyway" |
| Windows 10 / 11 · Portable | [AndroidAdCleaner-0.2.5-windows-portable.zip](https://github.com/rddmwmddr/android-ad-cleaner/releases/download/v0.2.5/AndroidAdCleaner-0.2.5-windows-portable.zip) | After unzipping, double-click `AndroidAdCleaner.exe` |

Not sure which Mac chip you have: click the Apple icon at the top left → About This Mac; if "Chip" starts with Apple M, choose Apple Silicon. All versions: [Releases](https://github.com/rddmwmddr/android-ad-cleaner/releases). Usage: [docs/en/08-desktop-client.md](docs/en/08-desktop-client.md).

| | |
|---|---|
| <img src="images/gui-1-connect.png" alt="Connect phone"><br>**1 Connect phone**: plug in the cable and the phone is recognized, with an illustrated tutorial for turning on USB debugging | <img src="images/gui-3-detect.png" alt="Detect"><br>**2 Detect**: model, system version, model recipe, Quick Apps, ad components |
| <img src="images/gui-4-choose.png" alt="Choose"><br>**3 Choose what to turn off**: marketing notifications are ticked per channel; service-type items are unticked by default | <img src="images/gui-6-run.png" alt="Run"><br>**4 Run**: progress bar and live log |
| <img src="images/gui-7-done.png" alt="Done"><br>**5 Done**: the result of every step, with a final reminder to turn off Developer mode | <img src="images/gui-8-feedback.png" alt="Feedback"><br>**Feedback**: diagnostic info is attached automatically; submit a GitHub Issue with one click |

---

- No root, no unlocking, no flashing; system updates are unaffected.
- Only the switches built into the system and its apps are used. Suspending an ad package requires the owner's approval, and a single command can restore it.
- Search, minus-one-screen cards, app-store installation and updates, weather alerts, and delivery reminders are kept.

<p align="center"><img src="images/store-before.png" width="560" alt="Before: app store home page full of recommendations"></p>
<p align="center">Before: OPPO App Store home page. Carousel, must-haves, must-plays, and benefit tags — all promotional slots.</p>

---

## What It Handles

| Category | Examples | How it is handled |
|---|---|---|
| System ads | Personalized ads, ad tracking (OAID), smart recommendation services | Switches in system settings |
| Trending searches and news | Hot lists in pull-down search, minus-one-screen news, browser news feeds | Switches in each app's settings; browser switched to a simple home page |
| Promotional slots | Store carousels, splash screens, floating activities, check-in benefits | Switches under the store's "Service management" |
| Marketing push notifications | Each app's "Content & marketing" and "Event offers" notifications | Turned off per channel; the same app's order, delivery, and update notifications are kept |
| Ad components | `com.opos.ads`, `com.miui.systemAdSolution`, etc. | `pm suspend` suspends them, with the owner's consent |
| Quick Apps | "Install-free mini programs" you land in by tapping an ad | `quickapp` detection, `quickapp off` to turn them off; see [docs/en/07-quick-apps.md](docs/en/07-quick-apps.md) |

## What It Does Not Do

- It does not uninstall or disable system apps (neither `pm uninstall` nor `pm disable-user` is used).
- It does not modify the system partition or install modules.
- It does not accept any app's user agreement on your behalf. If you reach an agreement page, tap "Cancel" or "Later".
- It does not screenshot account pages or phone-number pages.

---

## Four Ways to Use It

<p align="center"><img src="images/ways.png" width="460" alt="Three ways to use it"></p>

> Method 1 requires Developer mode and USB debugging to be turned on first, with a screenshot tutorial here: [docs/en/00-enabling-developer-mode.md](docs/en/00-enabling-developer-mode.md).

| Method | Who it suits | What you need | Docs |
|---|---|---|---|
| **1: An AI agent runs it for you** | You have a computer and want to save effort | A computer, a data cable, an AI tool that can run commands | [docs/en/02-using-an-ai-agent.md](docs/en/02-using-an-ai-agent.md) |
| **2: A chat AI walks you through it** | You only have a phone | Any one of DeepSeek, Doubao, or ChatGPT | [docs/en/03-using-a-chat-ai.md](docs/en/03-using-a-chat-ai.md) |
| **3: Follow the checklist manually** | You want to control every step yourself | Just a phone | [docs/en/checklists/](docs/en/checklists/) |
| **4: Desktop client** | You don't want to type commands | Mac (Apple / Intel chip) or Windows 10/11, a data cable | [Download](#download-the-desktop-client) · [Instructions](docs/en/08-desktop-client.md) |

Opening line for method 1 — copy it to the AI:

```text
Please clone https://github.com/rddmwmddr/android-ad-cleaner , read the AGENTS.md in the repo,
then help me remove ads from the phone connected to this computer. Before each change, tell me what you are about to change.
```

---

## Tested Models

**Model recipe**: the automatic steps for one model, recording "which app to open, which words to tap to reach a settings page, which switches to turn off, and which to keep". The computer follows it and taps on the phone, finishing in a few minutes. Settings pages differ by model and system version, so each model gets its own recipe.

| Brand | Model (model number) | System | Model recipe | Manual checklist | Marketing notifications |
|---|---|---|---|---|---|
| Honor | PNM-AN10 | MagicOS 10 | ✅ Tested, re-run in 4 minutes | ✅ | ✅ 26 channels |
| OnePlus | Ace 2 Pro (PJA110) | ColorOS 14.0.0.812 / Android 14 | New in source: 3 personalization items + 6 store promotional slots turned off and read back | Partial, see test record | ✅ 23 in total, master switch unchanged; weather-reminder difference, see test record |
| OPPO | Find N6 (PLP120) | ColorOS 16.0.9 | ⚠️ Paths tested, whole flow still to be verified | ✅ | ✅ 30 channels |
| OPPO | Find X10 Pro Max (PMX110) | ColorOS 17 | — | ✅ | ✅ |
| OPPO | Find X9 Ultra (PMA120) | ColorOS 16.0.10 | ❌ Pages differ from N6, to be added | Partial | ✅ 27 channels |
| OPPO | Find N3 Collector's Edition (PHN110) | ColorOS 16.0.5 | ❌ To be added | Partial | ✅ 27 channels |
| Xiaomi | 18 Pro Max (M154FF) | HyperOS 4.0.24 | ✅ First nine sections passed before 10-25, new compatibility changes still to be retested | ✅ | ✅ |
| vivo | X300 Ultra (V2547DA) | OriginOS 6 | ⚠️ Recipe added, whole flow still to be verified on a real device | ✅ | ✅ |

The table reflects the current recipes and verification scope. Xiaomi 10, Honor Magic7 Pro, and other reports have had fixable generic defects repaired, but still need retesting on the corresponding real devices; a same-brand reference recipe is not the same as dedicated adaptation. See [Changelog](CHANGELOG.md) for details.

- You can run the generic detection first; whether a notification channel can be safely turned off depends on the system page and permissions, and some vivo pages will be skipped. The ad-tracking entry also varies by brand.
- Within the same brand, a different minor system version can change settings-page names and levels. Model recipes are stored by model and system version; if the version does not match, the engine will warn you, and steps whose entry cannot be found are skipped — it will not tap at random.
- Your model is not in the table: follow [docs/en/04-writing-a-recipe-for-a-new-model.md](docs/en/04-writing-a-recipe-for-a-new-model.md) to write one, and PRs are welcome.

---

## One Complete Flow

<p align="center"><img src="images/flow.png" width="340" alt="Process flow"></p>

Command syntax:

```bash
pip3 install -r requirements.txt
python3 tool/run.py devices                 # See serial numbers, models, and whether a model recipe exists
python3 tool/run.py -s <序列号> check        # Read-only check
python3 tool/run.py -s <序列号> backup       # Snapshot before changes
python3 tool/run.py -s <序列号> recipe       # Run the model recipe
python3 tool/run.py -s <序列号> chan-scan    # List marketing notification channels
python3 tool/run.py -s <序列号> chan-off backups/<型号>-<时间>/channels.tsv
python3 tool/run.py -s <序列号> quickapp     # Detect Quick Apps; quickapp off turns them off
python3 tool/run.py -s <序列号> finish       # Finish up, with a reminder to turn off Developer mode
python3 tool/run.py -s <序列号> dev-off --yes  # Turn off Developer mode from the computer (last step; disconnects afterwards)
```

<p align="center"><img src="images/channel-off.png" width="420" alt="What marketing notification channels look like after being turned off"></p>
<p align="center">Marketing notifications are turned off per channel: Weather's "Content & marketing" is off, while weather alerts are kept.</p>

---

## Repository Structure

```text
AGENTS.md            Operating rules for AI agents to read
CHANGELOG.md         Source updates, verification results, and installer release status
docs/
  00-打开开发者模式.md Screenshot step-by-step tutorial
  01-准备工作.md      Install adb, connect to a computer, wireless debugging
  02-用AI智能体.md    WorkBuddy, Claude Code, Codex, Trae, Cursor
  03-用聊天AI.md      DeepSeek, Doubao, ChatGPT
  04-给新机型写脚本.md
  05-还原.md
  06-常见问题.md
  07-快应用.md        What Quick Apps are, how to detect and turn them off
  08-桌面客户端.md     Mac / Windows client usage, data locations, packaging
  09-社区问题处理.md   Issue / PR handling scope and pending verification items
  清单/               Manual checklists per brand
prompts/             Prompts to copy to a chat AI
tool/
  run.py             Main entry point
  fast.py            Screen-reading, entry-finding, switch-flipping engine (uiautomator2)
  chan_fast.py       Marketing notification channels
  explore.py         New-model pathfinding (experimental)
gui/                 Desktop client (pywebview UI + PyInstaller packaging)
recipes/<品牌>-<型号>/recipe.py   Model recipes per model
images/              Documentation illustrations
tests/               Engine regression tests that do not connect to a phone
```

## Feedback

If you run into a problem, want a new feature, or want your phone supported, file it at [Issues](https://github.com/rddmwmddr/android-ad-cleaner/issues/new/choose) and pick the matching template.

If you use the desktop client, click "Feedback" at the bottom left: it automatically attaches the client version, phone model, system version, and recent logs (serial numbers replaced, no app list and no notification content), opens the GitHub page, and you just click Submit. Submitting requires a GitHub account.

## Restore

See [docs/en/05-restore.md](docs/en/05-restore.md). Suspended packages and notification channels each take one command; switches inside apps are turned back on manually following the checklist paths.

## Disclaimer

This project only calls settings publicly provided by Android and the manufacturers' apps. Manufacturers' interfaces change with system updates; please back up before use, and what you see on your phone is authoritative. Any problems caused by using this project are the user's own responsibility.

License: MIT

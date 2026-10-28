# 08 Desktop Client (Mac / Windows)

If you do not want to type commands or use AI tools, use the desktop client: plug in the phone and click a few buttons.
The client calls the same engine (`tool/`); anything the command line can do, it can do.

> **Version note (2026-10-27)**: the current version is **0.2.5**, adding error-log reporting sent after user confirmation, retaining 0.2.4's marketing-notification page compatibility, Xiaomi security-settings detection, disconnect stopping and connection prompts, diagnostic garbling, and Mac Intel minimum-system-version fixes. Older versions do not update automatically; please download again. The original data and backup directories are kept. Test scope and compatibility limits are in [Changelog](../../CHANGELOG.md).

| Platform | Installer | Status |
|---|---|---|
| macOS (Apple Silicon) | `AndroidAdCleaner-<版本>-mac-arm64.dmg` | Signed, notarized; native UI, images, JS API, and built-in command line verified |
| macOS (Intel) | `AndroidAdCleaner-<版本>-mac-intel.dmg` | Signed, notarized; tested under Rosetta on an Apple Silicon Mac, Intel real device still to be tested |
| Windows 10 / 11 (64-bit) | `AndroidAdCleaner-<版本>-windows-setup.exe` (installer)<br>`AndroidAdCleaner-<版本>-windows-portable.zip` (portable) | Packaged on GitHub Actions cloud, smoke tests passed (command line, Chinese output, native GUI, images, and JS API); connecting a phone and the reporter's computer still to be tested |

## Download and install

Download the matching installer from the [Releases page](https://github.com/rddmwmddr/android-ad-cleaner/releases/latest).

Not sure which Mac chip you have: click the Apple icon at the top left of the screen → About This Mac; "Chip" starting with Apple M means Apple Silicon, and Intel means Intel.

**Mac**

1. Double-click the dmg and drag "安卓去广告" to the adjacent "Applications" folder.
2. Open "安卓去广告". The installer has passed Apple notarization, so it opens with a double-click.

**Windows**

1. Double-click `…-windows-setup.exe` to install. If you do not want to install, download `…-windows-portable.zip`, unzip it, and double-click `AndroidAdCleaner.exe`.
2. The installer has no code signature, so Windows pops up the blue "Windows protected your PC": click "More info" → "Run anyway".
3. After opening, if it says WebView2 is missing: click "OK" to go to Microsoft's site, download and install the "Evergreen Bootstrapper", then open this program again. Windows 11 includes it; some Windows 10 installs need it.
4. If the client does not recognize the phone after plugging it in: this computer lacks the phone's USB driver; see "Windows drivers" below.

No Python and no AI tool are needed. If there is no adb on the computer, the client prompts on first open to download it from Google's site (about 10 MB, only once).

## Five steps

**1. Connect phone**: plug in the data cable and the client recognizes the phone. If USB debugging is not yet on, the page has an illustrated tutorial. If there is no adb on the computer, the client prompts to download it from Google's site.

<p align="center"><img src="../../images/gui-1-connect.png" width="640" alt="Connect phone"></p>
<p align="center"><img src="../../images/gui-2-tutorial.png" width="640" alt="Illustrated tutorial for turning on USB debugging"></p>

**2. Detect**: reads the model, system version, whether a model recipe exists, and the status of Quick Apps and ad components. Read-only; it changes nothing. It warns if the phone is locked or a foldable is unfolded.

<p align="center"><img src="../../images/gui-3-detect.png" width="640" alt="Detect"></p>

**3. Choose what to turn off**:

| Item | Default |
|---|---|
| Ad switches in each app (when a model recipe exists) | Ticked, can be unticked per app |
| Marketing notifications | Clearly marketing-type items ticked; service-type, real-time activity, eye-care, event, alert, and vague categories like "Other / General notifications" kept by default |
| Quick Apps | Not ticked; you decide |
| System ad components | Not ticked; you decide |

<p align="center"><img src="../../images/gui-4-choose.png" width="640" alt="Choose marketing notifications"></p>
<p align="center"><img src="../../images/gui-5-choose-more.png" width="640" alt="Choose Quick Apps and ad components"></p>

Before running, if you need to troubleshoot the phone connection, tap "Check screen-reading connection". It only checks the service and page readability and does not tap switches; success does not mean all app paths have been verified.

**4. Run**: progress bar plus live log. Do not touch the phone while it runs.

<p align="center"><img src="../../images/gui-6-run.png" width="640" alt="Run"></p>

**5. Done**: lists the result of every step. The last card is "Turn off Developer mode": tap "Turn it off for me" and the client turns it off from the computer; or turn it off on the phone yourself. Turning it off does not undo this work.

<p align="center"><img src="../../images/gui-7-done.png" width="640" alt="Done"></p>

## Feedback

Bottom left "💬 Feedback", or "Report this problem" on the Done page (appears when a step fails).

1. Choose a type: encountered a problem / feature suggestion / adapt a new model.
2. Write one sentence about what happened.
3. By default, diagnostic info is attached: client version, computer system, phone model and system version (including HyperOS version), run results, the last 60 log lines, and the full cause of the most recent failure. The current user directory and phone serial number in errors are replaced, and it contains no notification text. Expand "View / edit diagnostics" to delete or edit.
4. Click "Submit to GitHub"; the browser opens a new Issue page with the content already filled in. After signing in to GitHub, click "Submit new issue".

If the log is too long, the diagnostics are copied to the clipboard; paste them into the page that opens.

<p align="center"><img src="../../images/gui-8-feedback.png" width="640" alt="Feedback"></p>

## Restore

Bottom left "Restore changes": restores Quick Apps, restores suspended ad components, and re-opens marketing notifications that were turned off.

<p align="center"><img src="../../images/gui-9-restore.png" width="640" alt="Restore"></p>
Restoring needs the phone connected; if Developer mode has been turned off, turn it back on following [00-enabling-developer-mode](00-enabling-developer-mode.md).

## Where data lives

Mac data directory:

| Content | Location |
|---|---|
| Pre-change snapshots, marketing notification lists, suspension records | `~/Library/Application Support/AndroidAdCleaner/backups/` |
| Most recent failure's full diagnostics (since 0.2.2, including the start of the exception) | `~/Library/Application Support/AndroidAdCleaner/logs/last-error.txt` |
| adb downloaded by the client | `~/Library/Application Support/AndroidAdCleaner/platform-tools/` |

The Windows equivalent directory is `%APPDATA%\AndroidAdCleaner\`; the full error is in `logs\last-error.txt`, with `backups\` holding snapshots and records and `platform-tools\` holding the downloaded adb. Bottom left "Open backup folder" opens it directly.

## Running from source and packaging

For development or building it yourself, first get the current source:

```bash
git clone https://github.com/rddmwmddr/android-ad-cleaner.git
cd android-ad-cleaner
```

If you already have a repo and the working tree is clean, switch to `main` and run `git pull --ff-only`. If you have your own changes, save them first to avoid overwriting. An existing installer will not automatically use this source; you need to run the source entry point below.

**Mac Apple Silicon** (requires `uv` installed first):

```bash
uv venv --python cpython-3.12-macos-aarch64 gui/.venv
uv pip install --python gui/.venv/bin/python pywebview pyinstaller uiautomator2 pillow
gui/.venv/bin/python gui/app.py          # Run
```

**Other platforms** can use an installed Python 3.12 to create a virtual environment, install `pywebview uiautomator2 pillow`, then run `gui/app.py`; Windows also needs WebView2. Current Windows source has passed cloud packaging and native GUI verification, and page startup now reads local files directly; connecting a phone, the reporter's computer, and Intel Mac regression of the new version are still to be done, see Known issues below. If you only need the command line, install `requirements.txt` following the root [README](../../README.md#one-complete-flow) and run `tool/run.py`.

Local Mac packaging:

```bash
gui/build_mac.sh                        # Package into gui/dist/
```

Packaging with signing and notarization (first prepare a Developer ID Application certificate in the keychain, and store notarization credentials with `xcrun notarytool store-credentials`):

```bash
SIGN_ID="Developer ID Application: 名字 (TEAMID)" NOTARY_PROFILE=公证配置名 gui/build_mac.sh
```

Release packages only contain explicitly listed programs, model recipes, and image resources; they do not pack local run logs, backups, or test models. The Intel main program adds the executable-memory permission needed for callbacks following the [PyObjC code-signing docs](https://pyobjc.readthedocs.io/en/latest/notes/codesigning.html); this round only enabling `allow-jit` still stuck on libffi, and after switching to a dedicated Intel entitlement it passed GUI tests. That permission is only given to the main program, keeping hardened runtime and library signature verification. Full release checks are in the changelog.

## Windows drivers

Mac needs no drivers. When Windows does not recognize the phone, install drivers by brand:

| Brand | Driver |
|---|---|
| Xiaomi / Redmi | Xiaomi Phone Assistant or [Google USB Driver](https://developer.android.com/studio/run/win-usb) |
| OPPO / OnePlus / realme | OPPO Phone Assistant, or Google USB Driver |
| vivo / iQOO | vivo Phone Assistant |
| Honor / Huawei | Huawei Phone Assistant / Honor Phone Assistant (quit it after installing, to avoid occupying the connection) |
| Other | Google USB Driver |

After installing, plug the cable back in and tap "Allow USB debugging" on the phone.

## Known issues

| Symptom | Explanation |
|---|---|
| When the window is in the background, the first click only brings the window to the front | Default behavior of a macOS web window; click again |
| Windows pops up "Windows protected your PC" | The installer has no code signature; click "More info" → "Run anyway" |
| Foldable unfolded cannot run model recipes | Fold closed and use the outer screen; marketing notifications, Quick Apps, and ad components are unaffected |
| 0.2.0 opens another window after tapping Run, or a subtask does not start | 0.2.1 fixed the packaged subprocess `--cli` entry point; please update the installer |
| 0.2.0 vivo / iQOO checklist link won't open | Open the [vivo checklist](checklists/vivo-OriginOS.md) first; 0.2.1 fixed brand jumping and Chinese path encoding |
| Windows shows "127.0.0.1 took too long to respond" after opening | [Issue #18](https://github.com/rddmwmddr/android-ad-cleaner/issues/18): 0.2.1 reads local files directly, avoiding the HTTP service; please update the installer, the reporter's computer is still to be retested. If you cannot update yet, use the old command-line entry point below |

### Using the built-in command line when the Windows 0.2.0 interface won't open

Unzip the portable version, and in the directory containing `aac-cli.exe`, open PowerShell; no separate Python install is needed:

```powershell
.\aac-cli.exe --cli run.py --help
.\aac-cli.exe --cli run.py devices
.\aac-cli.exe --cli run.py -s <序列号> check
```

This still runs the **0.2.0 engine** and will not get the latest source fixes. Do not copy bulk channel operations with known problems; first do read-only checks, then handle things manually following the [checklists](checklists/). If you need the new engine, download 0.2.3 or run from source as above.

### Verifying the local interface

From source you can run `python gui/app.py --smoke-gui`; after packaging, run `python gui/smoke_test.py <可执行文件> --gui`. This check verifies pages, tutorial images, JS API communication, and that no local HTTP service is created, without connecting a phone. The Windows workflow runs this check on the packaged program, and [cloud verification on 2026-10-25 passed](https://github.com/rddmwmddr/android-ad-cleaner/actions/runs/40198943037); passing does not mean all Windows security software and computer environments are covered.

### QueryController / UiDevice / UiAutomation stack traces in notification scans

0.2.1 starts the phone screen-reading service before scanning notifications, and blocks the scan if initialization fails; the UI only shows the tail of the exception, so the specific cause cannot be judged. Please update to 0.2.3: scanning and status re-checks read adb directly, while turning off a switch still needs normal screen reading.

After connecting and detecting, tap "Check screen-reading connection". On failure, expand "View full diagnostics" or tap "Copy full diagnostics"; even before any run starts, bottom-left "Feedback" will attach this full error. Keep the `Exception` / `Caused by` at the start of the exception; do not screenshot only the last few lines.

Read-only check from the command line (in the Windows portable directory):

```powershell
.\aac-cli.exe --cli run.py -s <序列号> ui-check
```

### AccessibilityServiceAlreadyRegisteredError / already registered

The full 0.2.2 log confirmed: Windows 11, Xiaomi 18 Pro Max, OS4.0.27.0.XEOCNXM / Android 17, when actually turning off a switch, the phone's UiAutomation service was already registered and the new session was rejected. App ads and marketing notification taps both need it, so they may fail together; notification scanning itself can still run. This is not caused by the `SLF4J` prompt or PyInstaller trailing text, and the specific occupant cannot be determined from this alone.

Supplementary feedback on 2026-10-26: the same user said 0.2.3 still failed, and after turning off GKD and Auto Accounting at the same time, processing could start. This is a troubleshooting lead; the specific tool or mode is not yet determined, and the absolute prompt "no need to turn off accessibility services" is no longer used.

Handling order:

1. Quit the old ad-removal client, Appium, UI inspectors, and other automation tasks operating on the same phone; keep only one client.
2. Check whether GKD, Auto Accounting, and similar tools have automation, screen-reading, or Shizuku features on. Only pause features you confirm can be paused; if necessary, the owner temporarily turns off the corresponding app's accessibility service, keeping screen readers and accessibility services they depend on.
3. Keep the phone unlocked, and after pausing items one by one, tap "Check screen-reading connection". If it still says already registered, the owner can manually restart the phone, then check without starting the above automation tools.
4. After the check passes, retry unfinished items; if it still fails, copy the full diagnostics. Afterwards, restore paused tools as needed; there is no need to clear data or repeatedly install the client.

The latest source, on failure, does a time-limited read-only check of the master switch and service count, and shows troubleshooting prompts in the error summary and Done page; it does not automatically disable accessibility. The 0.2.3 installer does not yet include these new prompts, but you can manually follow the troubleshooting above. For mistakenly turned-off "find photo spot" notifications and protection scope, see the [special guide](11-screen-reading-conflicts-and-functional-notification-protection.md).

0.2.3 uses a device lock on this machine to prevent multiple ad-removal processes from reading the screen at the same time; startup failure, operation exceptions, and normal completion all close the connection started this time, releasing the lock after it exits. An already-registered error is retried only once; persistent failure exits clearly, without waiting indefinitely or force-stopping other tools. Later tasks needing screen reading are marked "Skipped", the first error can still be copied, and finishing only means restore operations like restoring stay-on-while-charging — it does not mean all items succeeded. If you still need to troubleshoot or retry, keep USB debugging on first, then turn it off after finishing.

Technical basis: [Android's UiAutomation registration logic](https://android.googlesource.com/platform/frameworks/base/+/master/services/accessibility/java/com/android/server/accessibility/UiAutomationManager.java) limits registration to one service at a time; [uiautomator2 3.7.1 lifecycle code](https://github.com/openatx/uiautomator2/blob/3.7.1/uiautomator2/core.py) by default only registers exit cleanup after successful initialization, and uses a non-waiting exit method. The project adds this cleanup and handover handling; this cannot be used to conclude that the occupant on the reporting phone was necessarily produced by the old client.

### OnePlus Ace 2 Pro / ColorOS 14 source test

The latest source has added a limited recipe for this model and independent notification-settings page compatibility; details are in the [test record](10-oneplus-legacy-system-test.md). These updates have not yet entered the 0.2.3 installer; when running from source, install dependencies following the root `requirements.txt`. After this machine went online, 3 personalized recommendations and 6 store promotional slots were turned off and read back, and 23 marketing notifications were turned off. Other apps still have entry differences; a limited scope must not be written up as the whole device's ad removal being complete.

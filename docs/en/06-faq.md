# 06 Frequently Asked Questions

## Will it affect system updates?

No. No root, no unlocking, no changes to the system partition. Suspending (`pm suspend`) only pauses an app; receiving and installing system updates is unaffected.

## Will it affect the warranty?

No. It only uses Developer options and the system's own settings.

## Will there still be ads after finishing?

Some will remain:

| Remaining | Reason |
|---|---|
| Carousel hot words in the browser search box | There is no switch for them in settings |
| OPPO App Store "Must-haves on first boot" pop-up | It still pops up even after turning off everything under Service management |
| Pull-down search only usable with Baidu | The Chinese configuration only pushes one search engine; it cannot be changed without root |
| Some apps stuck on the "Agree to terms" page | This project does not agree on your behalf, so without entering, there is nothing to turn off |
| Newly installed apps | Ad tracking is on by default and marketing notifications are on by default; re-run the generic part once |

## Do I need to re-run after a system update?

It is recommended. A major update restores some switches to their defaults and may move settings pages. Before re-running, run `check` once to see whether the model recipe version matches.

## Why not uninstall the ad apps?

Chinese system apps cannot be uninstalled without root; `pm disable-user` is mostly rejected by the system, and the few that can be disabled break other functions when stopped. Suspension can be undone with a single command, so only suspension is used.

## Which suspended packages break functions?

Tested:

| Package | Function | Result of suspending |
|---|---|---|
| `com.heytap.quicksearchbox` | OPPO pull-down search | Search stops opening; must not be suspended |
| `com.coloros.assistantscreen` | OPPO minus-one screen | All cards disappear; must not be suspended |
| `com.opos.ads` | OPPO ad service | Normal |
| `com.heytap.pictorial` | OPPO Glance lock screen | Normal; lock-screen magazine disappears |
| `com.miui.systemAdSolution` | Xiaomi system ads | Normal, needs network blocking as well |
| `com.hihonor.quickengine`, etc. | Honor Quick Apps, Quick Games | Normal |

## The script reports "not found" — what do I do?

Your system version differs from the one the model recipe was recorded on, so a settings page changed name or location. Three ways to handle it:

1. Let the AI follow the checklist step by step, then save it as a new model recipe.
2. Turn things off manually following the [checklists](checklists/).
3. File an Issue stating the model, system version, and which section was not found.

## Windows client cannot recognize the phone?

Check in order (after going through these, the situation in [Issue #6](https://github.com/rddmwmddr/android-ad-cleaner/issues/6) was resolved):

1. Use a cable that can transfer data, plugged into a USB port at the back of the computer.
2. Pull down the phone's notification shade and set the USB purpose to "File transfer".
3. In Developer options, turn "USB debugging" off and back on; on the phone pop-up, tick "Always allow" and tap "Allow". If there is no pop-up, tap "Revoke USB debugging authorizations" and plug in again.
4. Honor, Huawei: in Developer options, also turn on "Allow ADB debugging in charge-only mode".
5. Install your phone brand's USB driver; see [08-desktop-client](08-desktop-client.md#windows-drivers). Samsung needs the official Samsung Android USB Driver; Honor and Huawei can get a driver by installing the corresponding phone assistant, then quitting the assistant afterwards.
6. Turn off other phone assistants and Android emulators on the computer (they occupy the connection).

Since 0.2.4, when the Windows client cannot wait for a phone, it queries Device Manager read-only: if the plugged-in phone has no debugging interface, or the debugging interface lacks a driver, it says directly which one it is. On a computer with only an old adb such as 1.0.32, the client no longer uses it and instead prompts you to download the official adb.

## Xiaomi / Redmi: lots of "not found" and "channel state unchanged after tapping", and the screen locks midway?

In Developer options, also turn on "USB debugging (Security settings)"; this item requires a SIM card inserted and a Xiaomi account signed in. Without it, the computer can read the screen, but taps it sends are rejected by the system and settings cannot be written: every section of the model recipe reports "not found", every marketing notification reports "channel state unchanged after tapping", stay-on-while-charging cannot be set, and the screen locks after a while.

In 0.2.4, the detection page first tries once (sending an empty keypress that triggers nothing); if it is rejected, it prompts you to turn on this item and does not proceed to the next step yet.

## Mid-run error `device '<序列号>' not found`?

The adb connection between phone and computer broke midway. Most commonly, a phone assistant, App Store assistant, 360 Mobile Assistant, Wandoujia, iTools, flashing tool, or Android emulator is also open on the computer; its own version of adb fights this tool's connection. It can also be a loose cable, port, or dock.

0.2.4 waits for the phone to come back and retries once; if it is still disconnected, it stops at that step and explains why, and later steps no longer show "Success". In 0.2.3 and earlier, after a disconnect it read empty results: the snapshot directory name became "-date", and Quick Apps showed "none detected" — those results are not trustworthy; please update and re-run. When copying diagnostics, it lists other adb processes running on the computer.

## Marketing notifications report "This vivo notification page's switch affects the whole app"?

That is the 0.2.3 message. On vivo / iQOO, the app notification master page and the single-channel page are carried by the same `com.vivo.systemuiplugin` page: the master page's "Allow notifications" turns off the whole app's notifications, so order and chat reminders disappear too; a channel page only controls one channel. 0.2.3 rejected that page entirely.

0.2.4 still does not tap the master page; it only operates on a channel page reached from the master page whose top bar shows the channel name, and afterwards checks that the app master switch has not changed (tested on X300 Ultra / OriginOS 6). When the channel name and the app name are the same, it cannot tell them apart and will skip it; you can enter that channel on the phone and turn it off manually. Do not use the app master switch as a substitute.

## Copied diagnostics paste as garbled text?

In 0.2.3 and earlier, on Windows, writing to the clipboard via PowerShell was decoded as GBK on Chinese systems, so pasted text came out as garbled characters like "鎻忚堪". 0.2.4 writes directly to a Unicode clipboard; when diagnostics are long, the feedback URL also carries the phone model, each step's result, and a log excerpt, instead of only "Please paste".

## Mac Intel version won't open?

The 0.2.0–0.2.3 Intel installers mistakenly used a Python built for macOS 26, so Intel Macs below macOS 26 could not open them ([#103](https://github.com/rddmwmddr/android-ad-cleaner/issues/103)). 0.2.4 uses a Python with minimum support macOS 11, and checks each file's minimum system version at packaging time. macOS 10.15 and earlier are still unsupported.

## Is the "Limit ad tracking" switch on or off?

On. Switches like "Limit ad tracking" and "Prevent ad tracking" are inverted: turning them on is the protection. The engine flips them to "on" and does not treat them as ad switches to turn off.

## Foldable phone won't run?

Fold it closed and use the outer screen. When unfolded it is a two-column layout with a taskbar at the bottom, and the engine looks in the wrong place. 0.2.1 refreshes the size when reading the screen and discards off-screen nodes (Issue #2 / #21), avoiding missing switches on the right side in landscape or tapping outside the screen; see [Changelog](../../CHANGELOG.md).

## Xiaomi search box keeps typing `%`?

The current source's Xiaomi model recipe now goes through menus to reach the ad service, avoiding reliance on settings search. Generic search also gained input-box readiness, input timeout, and text verification, and stops input on failure. Please upgrade to 0.2.1, or [run from source](08-desktop-client.md#running-from-source-and-packaging), or follow the [Xiaomi checklist](checklists/Xiaomi-HyperOS.md) manually.

## vivo client checklist link won't open?

You can open the [vivo / OriginOS checklist](checklists/vivo-OriginOS.md) directly. Current source already selects the specific file by brand and encodes the Chinese path; vivo and iQOO both point to this checklist. The fix entered 0.2.1, so the old link in 0.2.0 only changes after updating the client.

## Windows shows "127.0.0.1 took too long to respond" after opening?

See [Issue #18](https://github.com/rddmwmddr/android-ad-cleaner/issues/18). Current source loads the local page directly with `file://` and no longer depends on the HTTP service that timed out; the reporter's Windows 11 computer still needs retesting. Please update to 0.2.1 first; if you cannot update yet, use the 0.2.0 [built-in command line](08-desktop-client.md#using-the-built-in-command-line-when-the-windows-020-interface-wont-open) for read-only checks, or follow the [manual checklists](checklists/).

## Honor shows "not recognized" or "not supported"?

First distinguish two cases: the connection page never shows a device — check the data cable, USB debugging authorization, and Windows drivers; a model is shown but there is no model recipe — that model lacks a recorded path. Current source can actively choose a same-brand reference recipe, unticked by default; Magic5, Magic6, 100 Pro, and Magic7 Pro cannot be counted as fully adapted on that basis alone. When giving feedback, include the model code, system version, detection stage, and error message.

## Can native HarmonyOS be used?

Currently only Android devices connected via adb can be operated; HDC debugging and UI automation for native HarmonyOS have not been implemented. HDC is a separate device debugging tool; see [Huawei docs](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V13/hdc-V13). If a device only offers an HDC connection, installing Android USB drivers or borrowing a Honor recipe will not make it compatible; do not treat "Honor" and "native HarmonyOS" as the same system.

## Scan found no marketing channels — does that mean there are no ads?

No. It can only scan notification channels an app has already created; a new device or one just reset may have few, and the count is also affected by which apps are installed and used. An app needs to create a channel before sending notifications, and creation does not necessarily wait until the first notification is sent; see [Android notification docs](https://developer.android.google.cn/develop/ui/compose/notifications/create-notification?hl=en). After normal use, you can scan again; the current client clearly distinguishes "no candidates" from "scan failed".

## What does error-log reporting send?

Only what is shown in the pop-up: client version, computer system, phone model and system version, each step's result, the tail of the log, and a random install ID. Serial numbers, user directories, email addresses, phone numbers, and IPs are all replaced; it contains no app list and no notification content. The server keeps reports for 90 days, and IPs are only stored as hashes. See [Error log reporting](12-error-log-reporting.md).

## Is the data safe?

The script runs on your own computer and uploads nothing over the network. Snapshots live in local `backups/`, which contains app lists and notification records; do not upload it to a public repo. `.gitignore` already excludes this directory.

## Can the phone be used while it runs?

No. The script is tapping the screen; if you touch it, things go wrong. Keep the screen on, unlocked, and plugged in throughout.

## Notification scan reports a QueryController / UiDevice error — what do I do?

Please update to 0.2.3. The old scan unnecessarily started UiAutomation, and if initialization on the phone failed, channels could not be listed; the new version scans with adb read-only. Actually turning off a switch still needs screen reading, so first tap "Check screen-reading connection"; on failure, "Copy full diagnostics" provides the original exception. The `Failed to execute script app` at the end of a screenshot is only the program's exit result and cannot be used to judge the specific cause on the phone. See [client troubleshooting](08-desktop-client.md#querycontroller--uidevice--uiautomation-stack-traces-in-notification-scans).

## Full log says "already registered", and ads and marketing notifications all fail?

The phone's screen-reading service is already registered, and a new connection is rejected; the specific occupant cannot be determined from the stack trace alone. 0.2.3 added release of the current session, same-device mutual exclusion, and one limited retry; persistent conflicts skip later screen-reading steps and keep the first error. Please quit the old client and other phone automation tools; if it still fails, the owner should manually restart the phone, unlock it, and open only one client, then tap "Check screen-reading connection". There is no need to turn off accessibility services or clear data. See [Recovery steps and verification scope](08-desktop-client.md#accessibilityservicealreadyregisterederror--already-registered).

## Could screen-reading failure be related to GKD or Auto Accounting?

Users have reported that pausing both tools restored operation, but the specific tool and mode have not been pinpointed. On UiAutomation already-registered or screen-reading connection failures, follow [Screen-reading conflict troubleshooting](11-screen-reading-conflicts-and-functional-notification-protection.md) item by item; only the owner pauses automation features that can be paused, keeping dependent accessibility services, and restores them afterwards as needed. That guide also covers how to restore a single channel after a "find photo spot" notification was mistakenly turned off.

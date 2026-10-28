# 11 Screen-Reading Conflict Troubleshooting and "Find Photo Spot" Notification Protection

Updated: 2026-10-26. The code changes below have not yet entered the released 0.2.3 installer; 0.2.3 users can first follow the troubleshooting and restore steps.

## What this feedback shows

The original feedback environment was Windows 11, Xiaomi 18 Pro Max / OS4.0.27, with an error containing `AccessibilityServiceAlreadyRegisteredError`. After upgrading to 0.2.3, the user still failed, then turned off GKD and Auto Accounting at the same time and reported that processing could start.

This provides a usable conflict-troubleshooting direction, but tools and modes have not been compared one by one, nor independently reproduced. So it cannot be asserted which tool occupies the service, let alone inferred that all accessibility services must be turned off. 0.2.3's session cleanup and mutual exclusion are still kept; what this round improves is troubleshooting ability and prompts.

[Android's UiAutomation registration code](https://android.googlesource.com/platform/frameworks/base/+/master/services/accessibility/java/com/android/server/accessibility/UiAutomationManager.java) limits registration to one UiAutomation service at a time, which is not the same as saying only one ordinary accessibility service can be on. The [GKD official FAQ](https://gkd.li/guide/faq) and [Auto Accounting project notes](https://github.com/AutoAccountingOrg/AutoAccounting) also indicate the relevant tools may use accessibility or Shizuku; that technical background cannot prove the specific occupant on the reporting phone.

## Handling order when screen reading fails

1. Keep the phone unlocked, and quit duplicate ad-removal clients and Appium, UI inspectors, and other tasks operating on this phone.
2. Check whether GKD, Auto Accounting, and similar tools have automation, screen-reading, or Shizuku modes on. Only pause features you confirm can be paused; if necessary, the owner temporarily turns off the corresponding app's accessibility service.
3. Keep screen readers and accessibility services you depend on; do not turn off all accessibility at once. After pausing, tap "Check screen-reading connection", retesting after each single change to help locate the cause.
4. If it still fails, the owner can manually restart the phone; after unlocking, do not start the above automation tools before checking again. If it still fails, copy the full diagnostics.
5. After ad removal ends and the screen-reading session exits, restore previously paused tools as needed.

The client will not turn off the accessibility master switch on the user's behalf, modify the service list, force-stop other tools, or restart the phone. Post-failure auxiliary checks only read the master switch and the number of configured services via adb, waiting at most 3 seconds; service identifiers and app lists are not written into diagnostics. A failed read does not overwrite the original exception.

A master switch being on, or a service count greater than zero, is only a clue; it does not mean the occupant has been found. Reading off or zero items also cannot rule out a separate automation / Shizuku session. The UI's screen-reading check result and the run's Done page both give troubleshooting prompts, so prompts are not buried under a long stack trace.

## Protection scope for "find photo spot" notifications

A user separately reported that the Xiaomi 18 Pro series' "find photo spot" notification was mistakenly turned off by the marketing notification flow. That feature is a functional notification the user needs; it must not be turned off merely because a channel name or ID contains "recommend / activity / recommend" and similar words.

Current protection covers channels whose names contain "找机位", "机位推荐", or "推荐机位", accounting for simplified/traditional characters, spaces, and zero-width characters. Protection covers:

- Scan candidates: these functional notifications are excluded.
- Client list: even with old scan results, they are not put into the select-all marketing list.
- Old-list execution: the phone's current channel name, channel ID, and list description are checked; a hit on the protection rule is skipped; when only such items exist, screen reading is not started.
- Before actual tapping: the current name is read again, to prevent old list labels or post-scan renames from bypassing protection.
- Re-check statistics: protected channels are not counted as "marketing channels still on", and are noted as kept; ordinary marketing channels are still handled normally.

The real package name, full channel name, and channel ID for this feature have not yet been received; this is currently name protection, not precise ID adaptation verified on the reporting phone. If its actual name differs from the words above, information still needs to be supplemented before the rule can be improved.

## How to restore a mistakenly turned-off channel

You can enter that feature's app's system notification settings, find the channel corresponding to "找机位 / 机位推荐", and turn only that item back on.

With the original list, you can also copy that channel's row into a separate `restore-photo-spot.tsv`, keeping the original package name and channel ID, then run:

```bash
python tool/run.py -s "<序列号>" chan-on "backups/<原备份目录>/restore-photo-spot.tsv"
```

After running, check the read-back result to confirm that channel is on. The new protection rule only blocks turning off; it does not block an explicitly run restore. Scanning or running ad removal again will not by itself turn on channels previously turned off, so as not to overwrite the user's original choices.

## Verification and items to confirm

123 device-independent regressions passed, covering read-only checks and timeouts, service-list non-leakage, original-exception retention, GUI error prompts, functional-notification candidate exclusion, old-list protection, pre-tap re-checks, keeping already-closed states, and targeted restore. Native GUI smoke tests separately verified that a troubleshooting card and buttons actually appear when a simulated screen-reading failure occurs.

Code commit [`92a539f`](https://github.com/rddmwmddr/android-ad-cleaner/commit/92a539f07267b751fe0dfa9246dc1bba61e68fb7) passed Mac local regression and native GUI smoke tests, plus Windows [Actions #40213007991](https://github.com/rddmwmddr/android-ad-cleaner/actions/runs/40213007991) regression, PyInstaller packaging, native GUI / CLI smoke tests, and portable-package and installer generation. This Windows build was manual verification, not uploaded to Release, and did not replace the released 0.2.3 installer; packaging passing cannot substitute for retesting on the reporter's phone.

This round did not turn off any real-device accessibility service, nor re-enable notifications on the reporter's behalf. The reporter still needs to provide channel metadata and verify the new filtering and targeted restore on their device; success after turning off two tools together cannot be recorded as a single-tool root cause having been proven.

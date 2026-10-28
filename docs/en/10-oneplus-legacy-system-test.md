# 10 OnePlus Legacy System Test: Ace 2 Pro / ColorOS 14

Test date: 2026-10-25. Device: OnePlus Ace 2 Pro (PJA110), system `PJA110_14.0.0.812(CN01)`, Android 14, screen 1240 × 2772. Run via adb on a Mac; this is not a test of Windows connecting to this phone, and it cannot substitute for retesting Xiaomi OS4.0.27.

At first the store showed "No network connection"; the phone date was 2026-02-05 and the computer date was 2026-10-25. After the owner went online, the phone date also became 2026-10-25; the script did not change network or time settings. After going online, the service-management list gained items and some targets moved to the next screen, so cross-page search, target read-back, and other-switch preservation checks were added.

## App versions and adaptation scope

System versions and app versions affect entries separately. The versions actually installed this time were:

| App | Version | Result this time |
|---|---|---|
| Pull-down search | 11.31.4 | "Settings → Account & privacy → Privacy → Personalized recommendations" found and turned off |
| App Store | 12.21.0 | "My → Settings → Privacy → Personalized recommendations" is a second-level settings page; personalized recommendations turned off |
| App Store promotional slots | Same as above | After the owner went online, six clearly promotional items turned off and read back across pages; other service switches kept as they were |
| Browser | 40.10.1.9 | "My → Settings → Privacy → Personalized recommendations" found and turned off; the reference recipe's "Home page settings / Ad management" entries did not match |
| Theme Store | 11.6.3 | After fixing a small amount of first-screen text being misjudged as a blank ad, it could stay on this app's home page normally; the ad settings entry still awaits adaptation |
| Video | 40.7.11.1 | "My" page settings use a textless icon; ad switch verification not completed |
| Game Center | 14.27.1 | Guide page and settings entry differ from the reference recipe; ad switch verification not completed |
| Minus-one screen | 14.5.134 | Reference recipe's "Search box prompt words / Recommendation service" did not match; not marked successful |

The system ad entry is actually "Settings → Permissions & privacy → Privacy → Device identifiers & ads → Ad tracking". That page uses a per-app status list, not the single-page switch the reference recipe expected; this run did not automatically handle that list. System Settings also did not match the reference recipe's "OPPO AI → Xiao Bu Suggestions".

## Original reference recipe and dedicated recipe

First backed up, then ran the ColorOS 16 same-brand reference recipe in full in safe mode, taking 324 seconds, adjusting only 1 item (pull-down search personalized recommendations). Other items had entry mismatches or protective stops; a command exit code of 0 must not be taken as everything succeeding.

Then, following the real-device pages, added `recipes/oneplus-PJA110/recipe.py`, containing four sections: pull-down search, App Store, store promotional slots, and browser. It only handles explicitly listed switches, confirms the target before operating, and reads back afterwards. When an entry is missing or a switch is still on, the unfinished step is recorded and the CLI returns non-zero; logs of successfully changed items are still kept.

After fixing cold-start waiting, the final full re-run of the four sections, with four optional components kept suspended, took **155 seconds, 9 items read back as off, 0 items adjusted, 0 unfinished steps, exit code 0**.

Store promotional slots only selected these six items: floating activity icon, activity pop-up, top carousel card, bottom activity section, game detail page activity card, and software benefits. Download updates, app security, ordinary game categories, and Quick App entries are not on that list. The post-online closing section took 96 seconds, all 6 items read back as off, 0 unfinished steps; at the same time, other switches in the list were checked as unchanged from before the operation.

## Marketing notifications

The first scan found 27 candidates; keeping a mixed payment channel, two live-stream reminders, and the unclear-purpose "Important news", 23 clearly marketing channels were selected.

The old engine skipped ColorOS 14's standalone notification settings app. After the fix, only the two tested Activities are accepted:

- `com.oplus.notificationmanager.ChannelNotificationSettingsActivity`
- `com.oplus.notificationmanager.AppNotificationSettingsActivity` (only used to find channel entries; the app master switch must not be treated as a channel switch)

Channel titles and the clear "Allow notifications" switch still need checking. After 23 channels were turned off, the read-back count of still-on channels was 0. When closing first completed, against 368 existing channels, other channel states and each app's notification master switch matched the backup, with 2 new channels added at that time.

After going online and completing the full re-run: the 23 targets were still off, and all apps' notification master switches still matched the backup; 13 new channels in total. One other non-target channel changed: Weather's "Weather reminder" importance level changed from 4 to 3, `mUserLockedFields` changed from 0 to 34, and it was still on. It was not on this run's closing list, and the cause of the change is not yet confirmed; the public record keeps this difference, and the final result must not be written as "all non-target states unchanged".

Google Play's "Payment matters, special offers, and recommended content" also carries payment notifications, and has been added to the scan exclusion rules; it must not be turned off merely because its name contains "recommend".

## Engine fixes and verification boundaries

- A first screen with one or two labels can still be a normal page; it must not be treated as a blank ad and backed out of.
- The store had a brief blank on cold start; the old logic pressed back after 3 seconds and exited a normal app. Now it waits up to 8 seconds, only handles recognizable close / reject buttons; if there is still no page, it reports failure and does not blindly press back. The foreground package is checked before and after reading and handling pop-ups.
- After a slow start completes, time is still left for update and guide pop-ups to be handled.
- The store pops up a system notification permission request covering the app home page; only a clear "Reject / Do not allow" is tapped, and if there is no reject button it stops. Permission pop-ups that appear after the home page appears are also handled, without automatically granting permissions. That store notification master switch was already off before the operation and stayed off afterwards.
- The store keeps the engine's "stop the target app, then launch from the desktop entry" approach; the browser uses a verified public Activity and clears old tasks, to avoid exiting or reusing the last settings sub-page. The store could still enter its home page normally with the four optional components suspended; no app data was cleared.
- The dedicated recipe confirms with an actual Activity whether a settings page opened, handling the case where the first tap is swallowed by a switch animation.
- After going online, the store service list grew longer; all specified targets must first be found across pages, then operated on and read back, and other switch states checked. Finding only five items on the first screen cannot be assumed to mean the sixth does not exist, nor expanded into turning off the whole page.

112 device-independent regressions passed, covering the standalone notification page, mixed payment-channel retention, sparse first screens, stopping after leaving the foreground, permission-only-reject, cross-page targets and retained items, missing targets, and failure exit codes. Unit tests cannot substitute for per-model real-device tests.

Source commit `d4ee2d2`'s [Windows CI](https://github.com/rddmwmddr/android-ad-cleaner/actions/runs/40204906189) also passed the same 112 regressions, plus PyInstaller packaging, command-line and native GUI / image / JS API smoke tests, and portable-package and installer generation. This was a manual build verification; no new Release was published, and it did not cover the 0.2.3 installer.

Original backups, app lists, notification data, and full run logs are only kept on this machine in `backups/` and are not uploaded to GitHub. Public docs only keep the model, versions, operation scope, and verification conclusions.

## Components closed with the owner's consent

After the owner explicitly chose to close all four items, `pm suspend` was run and suspension status read back; Quick Apps and the still-running ad service and Glance processes then stopped, and on first check none of the four were running.

**Background stopping is only partially effective**: after re-running apps like the store, the ad service, Glance, and Quick App platform processes appeared again, while all four packages' suspension status was still true. After stopping again at the end, Glance and both Quick App processes were not running, but `com.opos.ads` was running again. The specific re-launch mechanism has not been located, so only "four packages suspended" is confirmed; it must not be written as "four items permanently closed" or "ad service completely stopped".

| Component | Package name | Impact |
|---|---|---|
| OPPO ad service | `com.opos.ads` | Suspends the ad service component; not equal to verifying all system ads are gone |
| Glance lock screen | `com.heytap.pictorial` | Disables the lock-screen magazine function |
| Quick App Platform | `com.nearme.instant.platform` | Disables install-free Quick Apps |
| Quick App Local Service | `com.oppo.instant.local.service` | Disables the corresponding Quick App service |

App Store, pull-down search, and the minus-one screen were all confirmed not suspended. Suspension does not uninstall apps and does not clear data; whether the system re-launches them later still needs actual observation.

## Restore

Notifications can be restored using this run's filtered list:

```bash
python tool/run.py -s <序列号> chan-on backups/PJA110-<时间>/channels-approved.tsv
```

The three personalized recommendation switches and six store promotional slots can be re-opened along the original paths above. Component restore:

```bash
python tool/run.py -s <序列号> unsuspend com.opos.ads com.heytap.pictorial
python tool/run.py -s <序列号> quickapp on
```

`run.py finish` has been run; stay-on-while-charging finally read back as the backup original value `0`. This machine refused to write that setting, and security permissions were not adjusted to work around the restriction; it cannot be claimed that stay-on was maintained throughout the test. When no longer troubleshooting, turn off the phone's Developer options master switch; completed ad-removal settings are not undone by that.

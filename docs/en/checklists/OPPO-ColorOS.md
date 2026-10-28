# OPPO / ColorOS Manual Checklist

Tested models: Find N6 (ColorOS 16.0.9), Find X10 Pro Max (ColorOS 17). OnePlus and realme ColorOS / OxygenOS structures are similar, though entry names may differ.
Symbols: 🔴 Turn off　🟢 Keep　⚠️ Note

---

## 1. System: Ad tracking

**Path**: Settings → Privacy → Device identifiers & ads → Ad tracking

- 🔴 One switch per app, no master switch. The count varies with installed apps and model: a phone may have over a hundred; the OPPO Pad Mini community test found about 26.
- ⚠️ On some versions, scroll down to the "More" group to see "Device identifiers & ads"; "More" is not necessarily a tappable sub-page.
- ⚠️ Newly installed apps are on by default; come back and turn them off after installing a new app.

## 2. Minus-one screen (Quick View)

**Path**: Swipe right from the left edge of the home screen → top-left avatar → Settings

- 🔴 Search box prompt words
- 🔴 Recommendation service → Carousel recommendations → choose "Don't show"
- 🔴 Hot news
- 🟢 Service updates (travel, life reminders), quick services
- ⚠️ Do not turn off the "Recommendation service" master switch: it removes weather, steps, and cleanup cards.

## 3. Pull-down search

**Path**: Swipe down in the middle of the home screen → "Settings" at the bottom of the search page

| Sub-page | 🔴 Turn off | 🟢 Keep |
|---|---|---|
| Search scope | Rankings, novels, shopping, personalized recommendations, featured news | In-app search, search suggestions, mini programs, AI search, convenient services |
| Home card management | Uninstalled app recommendations, app suggestion mini-cards, Discover, activity skins | App suggestions, local asset recommendations |
| Feature management | Search box prompt words | — |
| Account & privacy → Privacy | Personalized recommendations | — |

- ⚠️ "In-app search" must stay on; turning it off means local apps cannot be searched.
- ⚠️ The top of the search page prompts "Search results limited, turn on all search scopes"; do not tap "Turn on".
- ⚠️ Swiping down on a search settings sub-page exits it; scroll by swiping up with your finger.

## 4. App Store

**Path**: App Store → My → top-right gear icon

| Sub-page | 🔴 Turn off | 🟢 Keep |
|---|---|---|
| Privacy | Personalized recommendations | — |
| Service management | Home floating activity icon, home activity pop-up, home top carousel card, bottom activity section, game section items, game detail page activity card, etc., over 30 items in total | Help & customer service, app security, app tools, storage cleanup, my assets, security guard, Xiao i customer service, app usage records, home AI search, auto-detect risky apps |

- ⚠️ The "My" page has an avatar and phone number; avoid them in screenshots.
- ⚠️ After turning off everything under Service management, the "Must-haves on first boot" pop-up still appears.

## 5. Browser

**Path**: Find N6: bottom ☰ → gear icon; Find X9 Ultra: bottom "My" → Settings

- 🔴 Home page settings → Page layout → choose "Simple" (news feed and activity images disappear)
- 🔴 Privacy → Ad management → Splash ads, news list ads (shake ads grey out as a result)
- 🔴 Personalized recommendations
- ⚠️ There is no switch for carousel hot words in the search box.

## 6. Theme Store

**Path**: Theme Store → My → gear icon

- 🔴 Service management → Messages & ads → Message notifications, splash ads
- 🔴 Privacy → Personalized recommendation settings → Personalized recommendations
- 🟢 "All services / Basic services" stays on "All services"

## 7. Video (OPPO Video)

**Path**: Video → My → Settings → Personalized content management

- 🔴 Personalized recommendations

## 8. Game Center

**Path**: Game Center → My → Settings → Privacy switch settings → Personalized recommendation management

- 🔴 Personalized recommendations

## 9. Xiao Bu Suggestions

**Path**: Settings → OPPO AI → Xiao Bu Suggestions → Content & news

- 🔴 News service
- 🟢 Delivery, flight, schedule reminders, business-district services

## 10. Marketing notifications

**Path**: Settings → Notifications & status bar → Notification management → choose an app → tap a channel name

- 🔴 In each app, the channel called "Content & marketing". Alipay, JD, Meituan, Dianping, Xiaohongshu, Xianyu, Douyin, Kuaishou, Dewu, QQ, Tencent Meeting, Weather, and pull-down search all have one.
- 🔴 System messages "Featured recommendations", Cloud Service "Exclusive offers" and "Benefits", Wallet "Benefit notifications", Video "Important marketing information", minus-one screen "Latest news notifications".
- 🟢 The same app's order, delivery, update, security, and chat channels.

<p align="center"><img src="../../../images/channel-off.png" width="420" alt="Content & marketing channel turned off"></p>

With a computer: `run.py chan-scan` lists all candidates, `chan-off` turns them off in one go; 27 channels take about 60 seconds.

A just-reset device may not have created many notification channels yet; an empty list does not mean there are no ads. Scan again after normal use.

## 11. Ad packages (need adb, need your consent)

| Package | Function | After suspending |
|---|---|---|
| `com.opos.ads` | OPPO ad service | Normal |
| `com.heytap.pictorial` | Glance lock screen | Lock-screen magazine disappears |

## 12. Quick Apps (need adb, need your consent)

| Package | Function |
|---|---|
| `com.nearme.instant.platform` | Quick App Platform, handles `hap://` links |
| `com.oppo.instant.local.service` | Quick App Local Service |
| `com.nearme.instant.card` | Quick App Card (on some models) |

With a computer: `run.py quickapp` to detect, `quickapp off` to turn off. See [07-quick-apps](../07-quick-apps.md).

- ⚠️ Do not suspend `com.heytap.quicksearchbox` (pull-down search) or `com.coloros.assistantscreen` (minus-one screen).

---

## Differences by model

| Item | Find N6 (16.0.9) | Find X9 Ultra (16.0.10) | Find N3 Collector's Edition (16.0.5) |
|---|---|---|---|
| Browser settings entry | Bottom ☰ → gear icon | Bottom "My" → Settings | To be added |
| Store settings page | Has "Privacy" and "Service management" | Has them | Gear icon leads to "Apps & services", entry to be added |
| Video, Game Center | My → Settings | Cannot find "My", to be added | To be added |

Contributions welcome: file a PR to edit this table.

### OPPO Pad Mini (OPD2515 / ColorOS 16.1.0)

The following comes from [Issue #9 community testing](https://github.com/rddmwmddr/android-ad-cleaner/issues/9); there is no full automatic recipe for this model yet:

| Location | Difference and handling |
|---|---|
| App Store 12.21.62 | Settings has no "Privacy" or "Service management"; do not apply the 30+ promotional-slot list above, and do not turn off download updates or app security functions |
| Browser 40.10.10.9 | The tablet home page originally has no news feed, so there is no "Home page settings → Page layout". Keep the already-on website ad blocking; after turning off splash ads, shake ads may only grey out, which cannot count as an independent successful turn-off |
| Pull-down search | First dismiss the keyboard, then enter from "Settings" at the bottom; when a direct Activity is not exported, do not work around permissions. "Account & privacy" is only a group title. "Home card management" can turn off uninstalled app recommendations, app suggestion mini-cards, hot-search apps, featured recommendations, hot-search rankings, and recommendation cards; app suggestions, convenient services, and local search data sources are kept |
| Xiao Bu Suggestions | "Content & news → News service" is a second-level page; turn off news, keep events, travel, and other services |
| Taskbar | "Settings → Accessibility → Taskbar → Taskbar display content → Recent and suggested apps" shows suggested apps. Turning it off also removes recent apps, and you may need to re-pin common icons; the user decides, and it is not added to the generic automatic flow |
| Ad components | The community device has no `com.opos.ads` or `com.heytap.pictorial`; if detection finds none, skip them and do not substitute other packages |

Feedback also mentioned the `mcs_not_intercept_pkg` notification exemption list. This is an item to research; the impact of changing it on service notifications cannot be judged from package names alone. Currently it is not automatically changed, the full list is not copied verbatim, and the push transport layer `com.heytap.mcs` is not suspended.

### OnePlus Ace 5 (PKG110 / ColorOS 16)

Source: [PR #3 community testing](https://github.com/rddmwmddr/android-ad-cleaner/pull/3), not a full regression result from this repo.

- The store has no "Privacy" or "Service management"; personalized recommendations are on the "Account & privacy → Privacy authorization management → Personalized recommendations" sub-page.
- The browser bottom bar has no text labels; the community entered via the public entry `com.heytap.browser/.settings.component.BrowserPreferencesPage`. Video is skipped when it has no launch entry; Game Center is entered from "My → Settings → Privacy switch settings → Personalized recommendation management".
- Search scope is local data sources, kept; recommendation items are in home card management and feature management. Xiao Bu Suggestions' "On" is a text status; you need to enter the second-level page to handle it, and it cannot be tapped directly as a list switch.

### OnePlus Ace 2 Pro (PJA110 / ColorOS 14.0.0.812 / Android 14)

Real-device run on 2026-10-25; full scope is in [OnePlus legacy system test](../10-oneplus-legacy-system-test.md). The following is the latest source adaptation, not yet in the 0.2.3 installer.

- The system path is "Permissions & privacy → Privacy → Device identifiers & ads → Ad tracking"; the last page is a per-app status list, not automatically handled this time.
- App Store 12.21.0: "My → Settings → Privacy → Personalized recommendations" needs entering a second-level page; personalized recommendations were turned off. After going online, six clearly promotional slots in Service management were turned off across pages, and other service switches were read back as unchanged; download updates and risk detection are kept.
- Browser 40.10.1.9: "My → Settings → Privacy" can turn off personalized recommendations; the reference recipe's "Home page settings / Ad management" was not found.
- Pull-down search 11.31.4: "Settings → Account & privacy → Privacy" personalized recommendations turned off; other reference entries are not equal to adapted.
- System notification settings are at `com.oplus.notificationmanager`; 23 marketing channels were turned off and read back as passed, with the app master switch unchanged. After going online, the Weather reminder importance level changed but it stayed on; see the test record for the difference.
- Themes, Video, Game Center, minus-one screen, and others still have entry differences; the dedicated recipe only lists the limited scope already identified, and does not pass off all ColorOS 16 steps as verified.

After the owner consented to suspend the ad service, Glance, and two Quick App components on this machine, some processes were still observed being re-launched; at the end, the ad service was still running. Suspension status cannot prove complete background stopping; detailed status and restore methods are in the test record above.

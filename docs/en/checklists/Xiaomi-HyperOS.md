# Xiaomi / HyperOS Manual Checklist

Tested models are in the table below. Redmi and POCO structures are similar; without a recipe for your model, the client can borrow this one as a reference (safe mode).
Symbols: 🔴 Turn off　🟢 Keep　⚠️ Note

| Model | System | Source |
|---|---|---|
| Xiaomi 18 Pro Max (M154FF) | HyperOS OS4.0.24, Android 17 | Tested 2026-10-22; nine-section recipe re-run passed 2026-10-25 |
| Xiaomi 18 Fold (2608BPX34C) | CP2A.260605.016, Android 17 | Community test 2026-10-24 ([Issue #2](https://github.com/rddmwmddr/android-ad-cleaner/issues/2)) |

Both share the same system base; the difference is in app versions: after the Store, Browser, Global search, and Security apps were upgraded, entries changed. Each item below gives both "old version / new version" entries; pick the one you see on your phone.

---

## 1. System ads

**Path**: Settings → Privacy & security → (new version adds a "Security" layer) → More security settings → Ad services

- 🔴 Personalized ad recommendations
- ⚠️ Switches like "Limit ad tracking" and "Prevent ad tracking" are inverted: they must be **turned on**.

## 2. App Store

**Path**: App Store → My → top-right gear icon

- 🔴 Privacy settings (old version called "Privacy") → Personalized services; Store 4.129.s.00 needs tapping into the "Personalized services" sub-page, then turning off the switch inside
- 🔴 Mode switch → Minimal mode (only search, install, update remain). New Store versions do not have this item
- 🔴 Notification settings → New-user help
- 🟢 Notification settings → App updates
- ⚠️ Do not turn off "Push messages" in Notification settings: it is a parent switch; turning it off turns off "Like messages" and "Comment messages" together.

## 3. Security

**Path**: Security → top-right gear icon

- 🔴 Privacy settings → Personalized recommendations
- 🔴 Trash cleanup → Recommended content
- ⚠️ New Security (13.6.5) has neither item; skip them.

## 4. Downloads

**Path**: Downloads → top-right "More" → Settings → Feed settings (on some versions, directly the gear icon)

- 🔴 Resource recommendations, hot-list recommendations

## 5. Themes

**Path**: Themes → My → top-right gear icon

- 🔴 Notify on every network connection
- 🟢 Auto-update (right next to the item above; do not tap the wrong row)
- 🔴 Privacy settings → Personalized recommendations

## 6. Browser

**Path**: Browser → My → gear icon

- 🔴 Privacy & security → Personalized content recommendations, personalized ad recommendations (both old and new versions have them)
- 🔴 Old version: Home settings → Grid pushes; Search settings → Show "Guess what you want to search" module; Feature settings → Novels (🟢 My cloud drive)
- ⚠️ The new version has none of these three items. Home settings only has "Explore edition / Custom home page"; a custom home page needs a URL, `about:blank` cannot be entered, and `https://www.bing.com` can be entered. Choose according to your preference; not choosing is also fine.
- ⚠️ The browser pops up a Xiaomi account sign-in box; tap "Cancel".

## 7. Global search

**Path**: Swipe down on the home screen → gear icon at the top right of the search page

- 🔴 Home display modules → Search prompt words
- 🔴 Home display modules → App recommendations → Recommend uninstalled apps; 🟢 Show frequently used apps
- 🔴 Hot-search rankings:
  - Old version: tapping in shows switches directly — Recommendations, Weibo, News, All web, Film & TV, Music, Novels, Zhihu — turn them all off
  - New version: tapping in shows "My hot lists", in three pages: Hot searches → News, All web; Life → Featured; Topics → Zhihu. After turning them all off, the whole hot-search block on the search page disappears

## 8. Minus-one screen

**Path**: Swipe right from the left edge of the home screen → Settings

- 🔴 Recommendation cards, popular activities
- 🔴 Privacy settings → Personalized recommendations
- 🟢 Search box, travel assistant

## 9. Weather, Calendar

**Path**: Weather / Calendar → Settings → User experience program. Weather 18.0.0.27-R is entered from the bottom "City management → More settings → Settings"; Calendar from the top-right "More → Settings".

- 🔴 Inside: recommended content, personalized recommendations, content promotion
- On 2026-10-25, Weather and Calendar "Content promotion" were verified and turned off on Xiaomi 18 Pro Max (Weather 18.0.0.27-R, Calendar 18.0.1.30). The Redmi K60 entry comes from [community feedback](https://github.com/rddmwmddr/android-ad-cleaner/issues/1). Weather warnings and abnormal-weather reminders are kept.

## 10. Marketing notifications

**Functional notifications kept**: user feedback says the 18 Pro series' "find photo spot" notification was once mistakenly turned off. Find photo spot, photo-spot recommendations, and recommended photo spots are not marketing notifications; even if the name or ID contains "recommend / recommend", they are kept. The latest source has added protection; the 0.2.3 installer does not yet include it. The real package name / channel ID is to be supplemented; mistakenly turned-off restore is in the [special guide](../11-screen-reading-conflicts-and-functional-notification-protection.md).

**Path**: Settings → Notifications & control center → Notification management → choose an app → tap a channel name

- 🔴 App Store "Platform activity notifications", Browser "News & news", Play "Special offers", Edge "Hot news" and "Breaking news", etc.
- ⚠️ Xiaomi channel IDs look like `mipush|包名|数字`, with vertical bars.

## 11. System ad component msa (needs adb, needs your consent)

`com.miui.systemAdSolution` handles splash and built-in ads in system apps like Weather, Calendar, and the Store.

The 0.2.1 client and `run.py -s S suspend com.miui.systemAdSolution` suspend it and, when the system provides the interface, try to block networking, reading back package rules and firewall state. Old systems like Android 13 may not have these commands; in that case it clearly shows "partially complete" and returns failure: the suspension is kept, but ads may still appear. 0.2.0 has no network-blocking handling; see [Changelog](../../../CHANGELOG.md). The manual commands below only apply to systems where `cmd connectivity help` lists the corresponding interfaces:

```bash
adb -s S shell pm suspend --user 0 com.miui.systemAdSolution
adb -s S shell cmd connectivity set-package-networking-enabled false com.miui.systemAdSolution
adb -s S shell cmd connectivity set-chain3-enabled true
```

- ⚠️ Suspension alone does not stop it: system apps pull it back up when they start, so network blocking is added.
- ⚠️ Network-blocking rules may lapse after a restart; re-run the last two lines after restarting.
- Xiaomi 18 Pro Max test: Store, Browser, Themes, and Weather open normally and content loads normally; this does not mean all Xiaomi systems provide that interface.

Restore:

```bash
adb -s S shell pm unsuspend --user 0 com.miui.systemAdSolution
adb -s S shell cmd connectivity set-package-networking-enabled true com.miui.systemAdSolution
```

---

## Xiaomi pitfalls

**Xiaomi 10 (umi, Android 13 / OS1.0.7.0)**: [Issue #21](https://github.com/rddmwmddr/android-ad-cleaner/issues/21) provides the old-version paths. The browser top settings icon may have no `clickable` mark; the recipe only recognizes it in the toolbar and does not tap "My" in news body text. The hot-list page may have both a "Recommend" switch and hot-search / entertainment / topic sub-pages, and sub-pages may go landscape; 0.2.1 fixed screen-read size and traversal, but the full flow still awaits retesting on that device. Weather "User experience program" items "Weather video card" and "Content promotion" can be turned off, weather warnings kept; Weather and Calendar first-launch agreements are decided by the owner, and the recipe does not agree on their behalf.

| Symptom | Fix |
|---|---|
| Recipe can read the screen but not tap | In Developer options, turn on "USB debugging (Security settings)" |
| Turning off a switch pops up "Confirm turn off" | Tap Confirm |
| Browser swallows taps | Use an 80-millisecond short press; the engine already handles this |
| Models with a rear screen report multi-screen screenshot errors | Add `-d <主屏 display id>` to `screencap` |

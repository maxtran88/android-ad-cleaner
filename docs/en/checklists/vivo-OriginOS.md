# vivo / OriginOS Manual Checklist

Paths tested on: vivo X300 Ultra (V2547DA, OriginOS 6, Android 16), 2026-10-22. iQOO structure is similar. Current source adds the model recipe `recipes/vivo-V2547DA/`; full automatic execution still awaits real-device verification. V2547A will also match it, and with a different version it goes into safe mode, which does not mean OriginOS 7 is adapted. Release and verification scope are in [Changelog](../../../CHANGELOG.md).
Symbols: 🔴 Turn off　🟢 Keep　⚠️ Note

---

## 1. System: Ads & privacy

**Path**: Settings → Security → More security settings → Ads & privacy

- 🔴 Personalized ads, personalized recommendations, smart recommendation service

## 2. Minus-one screen

**Path**: Swipe right from the left edge of the home screen → top-right gear icon → More settings → Personalized recommendations

- 🔴 Service recommendations, news recommendations
- 🔴 Featured content, hot news
- 🟢 Xiao V suggestions (flight, delivery reminders)
- ⚠️ Do not turn off Convenient life → Recommendation service: those 10 icons (scan, flashlight, calculator, etc.) rely on it to fill the space; turning it off leaves the whole block empty.

## 3. Global search

**Path**: Settings → System management & upgrade → Global search

- 🔴 Home display content → Search box recommended words, recommendation cards
- 🔴 Recommended hot-search rankings → Popular searches
- 🔴 Personalized content → Ad personalization
- 🟢 History, app suggestions, search-result personalization

## 4. App Store

**Path**: App Store → My → Settings

- 🔴 About → Personalized recommendations
- 🔴 Service management → Check-in rewards, top carousel, top columns, splash screen, shake, floating window, limited-time promotions
- 🟢 My services, space cleanup
- ⚠️ On the splash guide page, untick "Enable message push to receive activities".

## 5. Browser

**Path**: Browser → My → gear icon

- 🔴 Home settings → Minimal home page; swipe up on home page to show news
- 🔴 Privacy permission settings → Personalized content, third-party app source personalized recommendations
- 🔴 Web browsing settings → Web download-related recommendations
- 🔴 More settings → Jump to news & news on Wi-Fi connection
- ⚠️ Browser pages often jump to news, novels, and claim-coins pop-ups; check each step as you go.

## 6. Picture lock screen

**Path**: Settings → Desktop, lock screen & wallpaper → Lock screen settings → Picture lock screen

- 🔴 Picture lock screen (when turning off "Swipe on lock screen to enter pictures", the master switch turns off with it)
- 🟢 Lock-screen wallpaper unchanged

## 7. i Manager

**Path**: i Manager → Settings → About → Personalized settings

- 🔴 App personalized recommendations

## 8. Weather

**Path**: Weather → Settings → Weather service

- 🔴 Weather-related hot news notifications
- 🟢 Weather warnings, abnormal weather, earthquake warnings

## 9. Marketing notifications

vivo push-category channels: `VPushChannel_0` (operator messages), `VPushChannel_4` (featured messages), `VPushChannel_6` (recommended messages).

- 🔴 Alipay operator, featured; Douyin operator, recommended; Cloud service push; usage-tips smart push suggestions; Play special offers; Edge hot news, breaking news
- ⚠️ Latest OriginOS 7 community testing found that the `com.vivo.systemuiplugin` page's "Allow notifications" is an app-level master switch; turning it off turns off order and chat notifications too. Current source skips directly on this page and does not continue per-channel operations; it must not be treated as a safe channel fallback entry. Per [PR #20](https://github.com/rddmwmddr/android-ad-cleaner/pull/20), other versions await verification one by one.
- ⚠️ Channel pages are handled by `com.vivo.systemuiplugin`; do not force-stop it.

## 10. Ad packages and Quick Apps

This device suspended no packages; in-app switches were enough.

- ⚠️ Quick App `com.vivo.hybrid`: on X300 Ultra (V2547A, Android 17), the system refuses to suspend it ([Issue #7](https://github.com/rddmwmddr/android-ad-cleaner/issues/7)). Per the real-device evidence in [PR #20](https://github.com/rddmwmddr/android-ad-cleaner/pull/20), current source, when it can read `switch_quick_app_service`, closes it via the system service switch and verifies, first backing up the original value; `quickapp on` restores from this device's backup, and without a backup it does not write directly as on. This repo has not yet retested this implementation on a vivo real device.
- 🟢 Smart Life `com.vivo.vhome` is a smart-home function; even though it registers a `hap://` entry, it is not treated as a Quick App ad component.

---

## vivo pitfalls

| Symptom | Fix |
|---|---|
| Minus-one screen, global search, themes, i Manager settings pages won't launch | They can only be entered from the app or system Settings |
| A list row and a switch each have a state | Judge by the switch itself |

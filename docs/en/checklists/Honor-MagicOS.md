# Honor / MagicOS Manual Checklist

Tested model: PNM-AN10 (MagicOS 10), 2026-10-23. Model recipe: `recipes/honor-PNM-AN10/`, re-run about 4 minutes.
Symbols: 🔴 Turn off　🟢 Keep　⚠️ Note

---

## 1. System: Ads & privacy

**Path**: Settings → search "ads" → Ads & privacy

- 🔴 Top-right ⋮ → Show system programs → top-right ⋮ → Turn all off (all apps' ad identifier reading)
- 🔴 Smart recommendation service

## 2. YOYO Suggestions

**Path**: Settings → search "news & news"

- 🔴 News & news

## 3. Pull-down search

**Path**: Swipe down in the middle of the home screen → press Back to dismiss the keyboard → "More" next to the search box → Settings

- 🔴 Home display → Hot-search rankings, hot-search word recommendations
- 🔴 Personalized management → Turn all off

## 4. Minus-one screen

**Path**: Swipe right from the left edge of the home screen → avatar → Settings

- 🔴 Smart recommendations, personalized ads, personalized messages
- 🔴 News service → Featured news

## 5. Desktop folder recommendations

"Hot recommendations" and "Featured apps" folders recommend uninstalled apps at the bottom.

- 🔴 Open a folder → bottom "More recommendations" → Settings → Turn all off
- 🔴 "Hot recommendations" folder → Settings → Turn off

## 6. AppGallery

**Path**: AppGallery → My → Settings

- 🔴 Content recommendation service → Marketing service recommendations, personalized service recommendations (tap them separately; tapping the second in quick succession fails)
- 🔴 Message notification management → Message notifications; 🟢 App updates
- 🔴 Message center reminders → Activity benefits, game updates
- 🔴 Service mode → Basic service (home recommendation feed disappears, leaving only search, install, update)
- ⚠️ After switching to basic service, the settings entry disappears. Switching back to full service requires agreeing to the agreement again, and the agreement re-opens personalized recommendations.

## 7. Browser

**Path**: Classic home page: My → third icon at the top right; Simple home page: More → Settings

- 🔴 Mode selection → Simple home page
- 🔴 Message notifications → News hotspots, interest pushes
- 🔴 Privacy management → Personalized recommendations → Personalized content
- 🔴 Privacy management → Interactive ad management → Turn all off (including shake)
- ⚠️ There is no switch for hot words in the search box.

## 8. Themes

**Path**: Themes → My → Settings

- 🔴 Notifications → Turn all three off (content recommendations and activity information)
- 🔴 Personalized services → Turn all off

## 9. Video (Youku Honor edition)

**Path**: Video → Settings → Other settings

- 🔴 Personalized content, personalized ads, OAID

## 10. System Manager

**Path**: System Manager → top-right gear icon

- 🔴 App recommendations
- 🟢 Cleanup, virus scan, and blocking under extended services

## 11. Music (NetEase Cloud Honor edition)

**Path**: Music → My → top-right gear icon → More settings

- 🔴 Message & privacy settings → Friend page shows recommended updates
- 🔴 Third-party push service switches → Turn all off (activities, prize information)
- 🟢 Personalized services (daily recommendations, private radar, which are music functions)
- ⚠️ Do not scroll up and down in the drawer menu; you may accidentally tap "Scan".

## 12. Reading

**Path**: Reading → My → More settings

- 🔴 Receive new notifications
- 🔴 Ad recommendation service → Turn all off
- ⚠️ "Receive new notifications" turns itself back on every time the app restarts. What blocks push notifications is its notification channel; see item 14.

## 13. Magic Poster (lock-screen magazine)

**Path**: Settings → search "magazine" → Magic Poster

- 🔴 Lock-screen poster carousel, lock-screen entry into Magic Poster

## 14. Marketing notifications

Honor's marketing channels are called "Marketing notifications", with channel IDs like `com.hihonor.android.pushagent.LOW.<数字>pnc`.

- 🔴 Each app's "Marketing notifications", 26 tested
- 🟢 The same app's service notifications

## 15. Quick Apps (need adb, need your consent)

With a computer: `run.py quickapp` to detect, `quickapp off` to turn off. See [07-quick-apps](../07-quick-apps.md).

| Package | Function |
|---|---|
| `com.hihonor.quickengine` | Quick App Engine |
| `com.hihonor.quickgame` | Quick Game |
| `com.honor.quickgamecenter` | Quick Game Center |

---

## Not handled

| Item | Reason |
|---|---|
| Game Center, Honor Mall | Stuck on the agree-to-terms page; agreements are not agreed on your behalf |
| "Marketing service recommendations" under AppGallery basic service | Settings entry disappears; the server-side state cannot be changed |
| Browser search box hot words | No switch |

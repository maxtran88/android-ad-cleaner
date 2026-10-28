# 00 Enable Developer Mode and USB Debugging

Before using a computer to work on your phone (method 1), two things must be turned on on the phone:

| What to turn on | What it does |
|---|---|
| Developer mode | Makes the "Developer options" page appear in Settings |
| USB debugging | Allows the computer to read the phone screen, tap buttons, and change settings |

If you only use the phone and follow a checklist manually (methods 2 and 3), you do not need this page.

The screenshots below are from OPPO (ColorOS 16); the entry names for other brands are in the tables under each step.

---

## Step 1: Find "Version"

<p align="center"><img src="../../images/dev-1-about.png" width="420" alt="Version info in About phone"></p>

| Brand | Path |
|---|---|
| OPPO / OnePlus / realme | Settings → About phone → Version info |
| Xiaomi / Redmi | Settings → My device → All specs |
| vivo / iQOO | Settings → System management & upgrade → Version info |
| Honor | Settings → About phone |
| Huawei | Settings → About phone |

## Step 2: Tap 7 times in a row

<p align="center"><img src="../../images/dev-2-version.png" width="420" alt="Tapping the version number repeatedly"></p>

| Brand | Which item to tap repeatedly |
|---|---|
| OPPO / OnePlus / realme | Version number |
| Xiaomi / Redmi | OS version |
| vivo / iQOO | Software version |
| Honor / Huawei | Version number |

1. Tap 7 times in a row; a countdown appears at the bottom of the screen: "3 more taps", "2 more taps" …
2. A lock-screen password prompt appears; enter your lock-screen password.
3. When you see "You are now in developer mode", this step is done.

## Step 3: Open Developer options

<p align="center"><img src="../../images/dev-3-search.png" width="320" alt="Searching for Developer options in Settings"></p>

The fastest way: open Settings, type "Developer options" in the search box at the top, and tap the search result.

You can also follow the path:

| Brand | Path |
|---|---|
| OPPO / OnePlus / realme | Settings → System & updates → Developer options |
| Xiaomi / Redmi | Settings → Additional settings → Developer options |
| vivo / iQOO | Settings → System management & upgrade → Developer options |
| Honor / Huawei | Settings → System & updates → Developer options |

## Step 4: Confirm the master switch is on

<p align="center"><img src="../../images/dev-4-on.png" width="420" alt="Developer options master switch"></p>

The "Developer options" switch at the top of the page should be blue (on). If it is off, turn it on.

## Step 5: Turn on USB debugging

<p align="center"><img src="../../images/dev-5-usb.png" width="420" alt="USB debugging and wireless debugging"></p>

1. Scroll down to the "Debugging" section.
2. Turn on "USB debugging"; tap "OK" on the pop-up.
3. If you do not want to use a cable, turn on "Wireless debugging" below; for pairing, see [01-preparation](01-preparation.md#wireless-debugging-if-you-dont-want-a-cable).

**One extra step for Xiaomi / Redmi**: on the same page, turn on "USB debugging (Security settings)". This item requires a SIM card inserted and a Xiaomi account signed in. Without it, the computer can read the screen but cannot tap buttons.

## Step 6: Plug in the cable and tap Allow

1. Connect to the computer with a data cable. A charge-only cable will not work; use one that can transfer files.
2. Pull down the phone's notification shade, tap the USB notification, and choose "File transfer".
3. The phone asks "Allow USB debugging?"; tick "Always allow from this computer" and tap "Allow".

If you do not see the pop-up: unplug and plug the cable back in; if it still does not appear, tap "Revoke USB debugging authorizations" in Developer options, then plug in again.

---

## Should you turn it off when you are done?

Yes, it is recommended. `run.py finish` will remind you at the end.

| Reason | Explanation |
|---|---|
| App detection | Some banking, payment, and game apps warn or refuse to run when they detect USB debugging is on |
| Security | Once it is off, nobody else can connect your phone to a computer either |

Two ways to turn it off:

1. On the phone: Settings → search "Developer options" → turn off the master switch at the top of the page.
2. From the computer: `python3 tool/run.py -s <序列号> dev-off --yes`. Afterwards the computer and phone disconnect; that is normal. Without `--yes`, it will refuse to run.

`dev-off` test record (OPPO Find N3 Collector's Edition, ColorOS 16.0.5, 2026-10-24):

| Item | Before | After |
|---|---|---|
| Developer mode | On | Off (verify on the phone) |
| USB debugging | On | Off, computer disconnects immediately |
| Wireless debugging | On | Off |

Turning off Developer mode **does not undo** this work: switches that were turned off, packages that were suspended, and notifications that were turned off all stay as they are. To restore later, turn Developer mode and USB debugging back on. On some brands, after turning it off you need to tap the version number 7 times again; start over from step 1.

## Common problems

| Symptom | Fix |
|---|---|
| Tapped 7 times, nothing happened | You tapped the wrong item; switch to another item from the step 2 table |
| Message "You are now in developer mode" | It was already turned on before; skip to step 3 |
| No "USB debugging" in Developer options | Scroll to the "Debugging" section, in the middle-lower part of the page |
| Computer shows `unauthorized` | The "Allow" on the phone was not tapped; see step 6 |
| Computer shows nothing at all | Change the data cable; change the USB purpose to "File transfer" |

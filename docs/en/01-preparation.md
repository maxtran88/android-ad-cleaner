# 01 Preparation

This page is needed for method 1 (AI agent). Methods 2 and 3 only need a phone, so skip this page.

## What you need

| Item | Notes |
|---|---|
| Computer | macOS, Windows, or Linux all work |
| Data cable | A cable that can transfer data. With a charge-only cable, the computer will not recognize the phone |
| Python 3.9 or above | Built into macOS or installable via Homebrew; on Windows, download from python.org |
| adb | Google's official platform-tools |

## Step 1: Install adb

| System | How |
|---|---|
| macOS | `brew install android-platform-tools` |
| Windows | Download [platform-tools](https://developer.android.com/tools/releases/platform-tools), unzip to `C:\platform-tools`, and add that directory to PATH |
| Linux | `sudo apt install adb` |

After installing, type `adb version` in a terminal; seeing a version number is enough.

## Step 2: Install dependencies

```bash
pip3 install -r requirements.txt
```

## Step 3: Turn on Developer mode and USB debugging on the phone

Step-by-step tutorial with screenshots: [00-enabling-developer-mode](00-enabling-developer-mode.md). The entries for all five brands are in there.

## Step 4: Connect to the computer

1. Plug in the cable and tap "Allow" on the phone (see [00-enabling-developer-mode](00-enabling-developer-mode.md) step 6).
2. On the computer, run:

```bash
python3 tool/run.py devices
```

When you see a line like this, you are connected:

```text
7f386895   OPPO Find N3 典藏版   PHN110   PHN110_16.0.5.1201(CN01)   机型脚本：无（只能跑通用部分）
```

The first column is the serial number; later commands all use it.

## Wireless debugging, if you don't want a cable

1. Connect the phone and the computer to the same Wi-Fi.
2. Developer options → turn on "Wireless debugging" → tap into it → "Pair device with pairing code".
3. The pop-up shows a 6-digit pairing code and an "IP address:port". On the computer, run:

```bash
adb pair 192.168.31.100:37xxx      # The address and port from the pop-up
# Enter the 6-digit pairing code
adb connect 192.168.31.100:41xxx   # The address and port shown at the top of the wireless debugging page
```

The pairing port and the connection port are two different numbers. Pairing is done only once; afterwards, each time you turn on wireless debugging the connection port changes, so use the new port with `adb connect`.

## Foldable phones

Fold the phone closed and use the outer screen. When unfolded, system Settings and apps are in a two-column layout with a taskbar at the bottom, and the engine will look in the wrong place.

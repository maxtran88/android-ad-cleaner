# 05 Restore

| Change | How to restore |
|---|---|
| Suspended ad packages | `python3 tool/run.py -s S unsuspend` (removes all recorded suspensions) |
| A single package | `python3 tool/run.py -s S unsuspend com.opos.ads` |
| Marketing notification channels | `python3 tool/run.py -s S chan-on backups/<型号>-<时间>/channels.tsv` |
| Quick Apps | `python3 tool/run.py -s S quickapp on`; the vivo service switch is restored to the value saved for this device, and without a backup it is not turned on by default |
| Stay-on-while-charging | `python3 tool/run.py -s S finish` |
| Switches inside apps | Turn them back on manually following the paths in the [checklists](checklists/) |
| Xiaomi msa network blocking | See the end of [checklists/Xiaomi-HyperOS.md](checklists/Xiaomi-HyperOS.md) |

Restoring needs a computer. If Developer mode has been turned off, turn it back on following [00-enabling-developer-mode](00-enabling-developer-mode.md).

## Restoring suspended packages without a computer

A suspended app's icon is greyed out, and tapping it says "Paused". Suspension can only be lifted with adb, so without a computer:

1. A factory reset lifts suspension (data will be wiped, so back up first).
2. Or borrow a computer, install adb, and run `adb -s S shell pm unsuspend --user 0 包名`.

## The pre-change snapshot

The snapshot saved by `backup` is in `backups/<型号>-<时间>/`:

| File | Contents |
|---|---|
| `info.txt` | Brand, model, system version |
| `sys.txt` `user.txt` `disabled.txt` | System apps, user-installed apps, disabled apps |
| `settings-before.txt` | Full system settings |
| `notif.txt` | Full notification channels |
| `stay_on.txt` | Original stay-on-while-charging value |
| `channels.tsv` | Marketing notification channels turned off in this run |
| `suspended.txt` | Packages suspended in this run |
| `quickapp-setting.json` | Original vivo Quick App service-switch value and its device; deleted after a successful restore, and repeated closing or a new snapshot does not overwrite the initial record |

To find out whether a setting was changed, compare the changed `settings list` with `settings-before.txt`.

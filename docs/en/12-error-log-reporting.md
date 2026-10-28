# 12 Error Log Reporting

When the desktop client fails during a run, you can send this run's error log to the project maintainer, without needing a GitHub account.

## What the user sees

1. When the Done page shows "some steps did not succeed", tap "Report error log"; the "Feedback" window also has this button.
2. The pop-up window lists **all content to be sent**, shown exactly as it is; it is only sent after you confirm. If you do not tap "Confirm report", nothing is sent.
3. After success, a report number is shown. To delete that record, file a GitHub Issue including the number.

## What is sent

| Content | Notes |
|---|---|
| Client version, computer system | For example `0.2.5`, `Windows 11（AMD64）` |
| Phone brand, model, system version, Android version | From the detection page |
| Each step's result | Step name, success / failure / skipped, time taken |
| Tail of the log | At most 20,000 characters, from the same source as "Copy full diagnostics" |
| Install ID | Randomly generated on first report, stored in the client data directory's `install-id`, used only for rate limiting; no device or computer identifier is taken |

Before sending, replacements are made in the client, and again after the server receives it: phone serial number → `<序列号>`, computer user directory → `<用户目录>`, email addresses, 11-digit phone numbers, and IP addresses → `<邮箱>` `<手机号>` `<IP>`.

Not sent: app lists, notification content, account information, screenshots, backup files.

## How the server stores it

- Sent to the maintainer's own server, whose address is written in the client (`supabase.ahuamiao.com`).
- Kept for **90 days**, then automatically deleted on expiry.
- IPs are not stored verbatim, only as an irreversible encrypted hash, used to limit report frequency; the random install ID is likewise only stored as a hash.
- The reporting channel uses a separate low-privilege account that can only write new reports, not read any data.

## Rate limits

The client allows at most 3 reports per hour; the server additionally limits by IP and install ID, accepting only one report with completely identical content per hour. When exceeded, it prompts "Reporting too frequently, please try again in an hour".

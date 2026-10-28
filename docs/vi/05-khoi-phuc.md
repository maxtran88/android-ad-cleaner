# 05 Khôi phục

| Thay đổi | Cách khôi phục |
|---|---|
| Gói quảng cáo bị tạm ngưng | `python3 tool/run.py -s S unsuspend` (hủy toàn bộ ghi lại) |
| Một gói đơn lẻ | `python3 tool/run.py -s S unsuspend com.opos.ads` |
| Kênh thông báo tiếp thị | `python3 tool/run.py -s S chan-on backups/<型号>-<时间>/channels.tsv` |
| Quick App | `python3 tool/run.py -s S quickapp on`; công tắc dịch vụ vivo khôi phục theo giá trị gốc đã lưu của thiết bị này, không có bản sao lưu thì không mặc định bật |
| Cắm sạc luôn sáng | `python3 tool/run.py -s S finish` |
| Công tắc trong ứng dụng | Theo đường dẫn trong [danh sách](checklists/) bật lại thủ công |
| Xiaomi msa chặn mạng | Xem cuối [danh sách/Xiaomi-HyperOS.md](checklists/Xiaomi-HyperOS.md) |

Khôi phục cần máy tính. Chế độ nhà phát triển đã tắt thì theo [00-bat-che-do-nha-phat-trien](00-bat-che-do-nha-phat-trien.md) bật lại.

## Không có máy tính vẫn khôi phục gói bị tạm ngưng

Biểu tượng ứng dụng bị tạm ngưng có màu xám, bấm vào sẽ nhắc "Đã tạm dừng". Trạng thái tạm ngưng phải dùng adb mới hủy được, không có máy tính thì:

1. Khôi phục cài đặt gốc sẽ hủy tạm ngưng (dữ liệu sẽ bị xóa, cần sao lưu).
2. Hoặc mượn một máy tính, cài adb, chạy `adb -s S shell pm unsuspend --user 0 包名`.

## Ảnh chụp nhanh trước khi thay đổi

Ảnh chụp nhanh `backup` lưu tại `backups/<型号>-<时间>/`:

| Tệp | Nội dung |
|---|---|
| `info.txt` | Hãng, mẫu máy, phiên bản hệ thống |
| `sys.txt` `user.txt` `disabled.txt` | Ứng dụng hệ thống, ứng dụng tự cài, ứng dụng đã vô hiệu hóa |
| `settings-before.txt` | Toàn bộ mục cài đặt hệ thống |
| `notif.txt` | Toàn bộ kênh thông báo |
| `stay_on.txt` | Giá trị gốc cắm sạc luôn sáng |
| `channels.tsv` | Kênh thông báo tiếp thị đã tắt lần này |
| `suspended.txt` | Gói đã tạm ngưng lần này |
| `quickapp-setting.json` | Giá trị gốc công tắc dịch vụ Quick App vivo và thiết bị sở hữu; sau khi khôi phục thành công sẽ xóa, đóng lại nhiều lần và ảnh chụp nhanh mới không ghi đè bản ghi ban đầu |

Muốn biết một cài đặt có bị sửa không, dùng `settings list` sau khi thay đổi so sánh với `settings-before.txt`.

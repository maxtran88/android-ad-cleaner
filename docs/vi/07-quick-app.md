# 07 Quick App: Phát hiện và tắt

## Quick App là gì

Quick App là "tiểu chương trình không cần cài đặt" do các hãng điện thoại cùng ra mắt, bấm một liên kết là mở, không cần tới cửa hàng tải về. Điện thoại bản Trung Quốc của OPPO, Xiaomi, vivo, Honor, Huawei đều cài sẵn khung Quick App.

Vấn đề nằm ở quảng cáo: quảng cáo trong trang web, ứng dụng video ngắn, ứng dụng tiểu thuyết thường dùng liên kết bắt đầu bằng `hap://`, nhảy bạn vào một Quick App, mở các trang dạng "Đọc tiểu thuyết", "Nhận bao lì xì", "Trò chơi nhỏ". Bạn không bấm "Cài đặt", nó vẫn mở được, còn có thể gửi thông báo cho bạn.

## Tôi có dùng tới nó không?

`quickapp` sẽ tra bản ghi sử dụng của hệ thống, cho bạn biết gần đây đã mở mấy lần (liên kết mở thủ công lúc kiểm thử cũng tính vào). Một chiếc OPPO Find N3 kiểm chứng thực tế: hai thành phần Quick App luôn chạy nền, số lần mở gần đây là 0.

```text
$ python3 tool/run.py -s <序列号> quickapp
检测到 2 个快应用组件：
  快应用平台      com.nearme.instant.platform        未挂起  后台在跑  近期没打开过
  快应用本地服务    com.oppo.instant.local.service     未挂起  后台在跑  近期没打开过
hap:// 链接由 com.nearme.instant.platform/.dispatch.activity.HapDispatcherActivity 接管：网页或 App 里的广告可以用这类链接跳进快应用。
关闭：python3 tool/run.py -s <序列号> quickapp off（要机主同意，可还原）
```

Dịch nghĩa: phát hiện 2 thành phần Quick App — Nền tảng Quick App (`com.nearme.instant.platform`), chưa tạm ngưng, đang chạy nền, gần đây chưa mở; Dịch vụ cục bộ Quick App (`com.oppo.instant.local.service`), trạng thái tương tự. Liên kết `hap://` do `com.nearme.instant.platform/.dispatch.activity.HapDispatcherActivity` tiếp nhận: quảng cáo trong trang web hoặc ứng dụng có thể dùng liên kết loại này nhảy vào Quick App. Tắt: `python3 tool/run.py -s <序列号> quickapp off` (cần chủ máy đồng ý, có thể khôi phục). Đầu ra tiếng Trung gốc trên được giữ nguyên vì đó là đầu ra chương trình theo nghĩa đen.

| Kết quả | Đề xuất |
|---|---|
| Gần đây chưa mở | Tắt đi, không ảnh hưởng tới bạn |
| Gần đây đã mở | Nghĩ xem có phải mình chủ động dùng không. Nếu một dịch vụ thường dùng (ví dụ thanh toán, mã đi xe) mở từ Quick App, tắt rồi cổng vào này sẽ không mở được |

## Tắt và khôi phục

```bash
python3 tool/run.py -s <序列号> quickapp        # Phát hiện (chỉ đọc)
python3 tool/run.py -s <序列号> quickapp off    # Tắt
python3 tool/run.py -s <序列号> quickapp on     # Khôi phục
```

Sau khi tắt rồi phát hiện lại:

```text
$ python3 tool/run.py -s <序列号> quickapp
检测到 2 个快应用组件：
  快应用平台      com.nearme.instant.platform        已挂起  没在跑  近期没打开过
  快应用本地服务    com.oppo.instant.local.service     已挂起  没在跑  近期没打开过
快应用已全部关闭。广告里的 hap:// 链接会弹「应用无法使用」，不会跳进快应用。恢复：quickapp on
```

Dịch nghĩa: cả hai thành phần nay đã tạm ngưng, không chạy, gần đây chưa mở. Quick App đã tắt toàn bộ. Liên kết `hap://` trong quảng cáo sẽ hiện "Ứng dụng không dùng được", không nhảy vào Quick App. Khôi phục: `quickapp on`.

Quảng cáo lại muốn nhảy vào Quick App, hệ thống sẽ hiện nhắc này, bấm "Đồng ý" là quay lại trang gốc:

<p align="center"><img src="../../images/quickapp-blocked.png" width="480" alt="Sau khi Quick App tắt, liên kết hap hiện ứng dụng không dùng được"></p>

### Bản ghi kiểm chứng thực tế (OPPO Find N3 bản sưu tập, ColorOS 16.0.5, 2026-10-24)

| Bước | Kết quả |
|---|---|
| `quickapp off` | 2 thành phần tạm ngưng, dùng 2,6 giây, tiến trình nền thoát hết |
| Mở một liên kết `hap://` | Hiện "Ứng dụng không dùng được", Quick App không khởi động |
| `quickapp on` | 2 thành phần khôi phục, cùng liên kết đó mở Quick App |
| Lại `quickapp off` | 2 thành phần tạm ngưng, liên kết lại bị chặn |

Phần lớn mẫu máy dùng `pm suspend` (tạm ngưng); công tắc dịch vụ hệ thống của vivo xem mục sau:

- Thành phần ở lại trong điện thoại, không gỡ cài đặt, không vô hiệu hóa, cập nhật hệ thống không bị ảnh hưởng.
- Tạm ngưng hạn chế lần khởi động sau, nhưng tiến trình đã chạy chưa chắc thoát ngay lập tức; mã nguồn hiện tại sau khi tạm ngưng thành công thực thi `force-stop`. Biểu tượng có thể vẫn còn trong ngăn ứng dụng, không lấy việc biểu tượng có biến mất hay không để phán đoán thành công.
- `quickapp on` một lệnh khôi phục. Bản ghi tạm ngưng lưu tại `backups/<型号>-<时间>/suspended.txt`.

## Thành phần Quick App của từng hãng

| Hãng | Tên gói | Tên gọi | Kiểm chứng tạm ngưng |
|---|---|---|---|
| OPPO / OnePlus / realme | `com.nearme.instant.platform` | Nền tảng Quick App | ✅ Find N6, Find X10 Pro Max, Find N3 |
| | `com.oppo.instant.local.service` | Dịch vụ cục bộ Quick App | ✅ Find N6, Find N3 |
| | `com.nearme.instant.card` | Thẻ Quick App | ✅ Find X10 Pro Max |
| Honor | `com.hihonor.quickengine` | Công cụ Quick App | ✅ PNM-AN10 |
| | `com.hihonor.quickgame` | Trò chơi nhanh | ✅ |
| | `com.honor.quickgamecenter` | Trung tâm trò chơi nhanh | ✅ |
| Xiaomi / Redmi | `com.miui.hybrid` | Khung dịch vụ Quick App | Chưa kiểm chứng thực tế |
| | `com.miui.hybrid.accessory` | Phụ kiện khung dịch vụ Quick App | Chưa kiểm chứng thực tế |
| vivo / iQOO | `com.vivo.hybrid` | Quick App | ❌ Hệ thống từ chối tạm ngưng; mã nguồn hiện tại ưu tiên dùng công tắc dịch vụ hệ thống, xem mục sau |
| Huawei | `com.huawei.fastapp` | Trung tâm Quick App | Chưa kiểm chứng thực tế |

Gói "Chưa kiểm chứng thực tế", sau khi tạm ngưng vui lòng kiểm tra ứng dụng thường dùng có mở bình thường không, có vấn đề dùng `quickapp on` khôi phục, và gửi Issue cho chúng tôi biết.

## Công tắc dịch vụ hệ thống vivo / iQOO

Theo bản ghi máy thật trong [PR #20](https://github.com/rddmwmddr/android-ad-cleaner/pull/20) của V2547A / OriginOS 7, `switch_quick_app_service=0` có thể chặn cổng vào Quick App. Mã nguồn hiện tại chỉ dùng nó trên vivo / iQOO và khi đọc được công tắc này, không vô hiệu hóa hoặc gỡ cài đặt ứng dụng, không xử lý các bên nhận `hap://` khác như Smart Life.

- `quickapp off` lưu giá trị gốc trước, rồi ghi và đọc lại xác nhận; đóng lại nhiều lần không ghi đè giá trị gốc ban đầu.
- `quickapp on` tìm trong các bản sao lưu trước đây bản ghi của thiết bị này rồi khôi phục; không tìm thấy bản ghi thì báo thất bại, không mặc định ghi thành `1`.
- Tệp sao lưu là `quickapp-setting.json`, đặt trong `backups/` được bỏ qua, chứa định danh thiết bị, đừng tải lên công khai.
- Ứng dụng hiển thị theo trạng thái tắt thực tế, không còn coi công tắc dịch vụ tắt nhầm thành "chưa tạm ngưng, vẫn đang mở". Đợt này đã làm hồi quy tự động, vẫn chờ điện thoại vivo kiểm chứng lại; gói cài đặt 0.2.0 chưa bao gồm tính năng này.

## Không có máy tính thì làm sao

Tạm ngưng cần adb. Chỉ có điện thoại thì có thể làm hai việc:

1. Tắt thông báo Quick App: Cài đặt → Quản lý thông báo → tìm "Quick App" → tắt "Cho phép thông báo".
2. Sau khi nhảy vào Quick App, từ màn hình chính nhấn giữ biểu tượng của nó, xóa lối tắt.

Hai bước này không chặn được quảng cáo nhảy, chỉ chặn thông báo và biểu tượng màn hình chính.

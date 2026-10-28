# 10 Kiểm chứng hệ thống cũ OnePlus: Ace 2 Pro / ColorOS 14

Ngày kiểm chứng thực tế: 2026-10-25. Thiết bị là OnePlus Ace 2 Pro (PJA110), hệ thống `PJA110_14.0.0.812(CN01)`, Android 14, màn hình 1240 × 2772. Thực thi qua adb trên Mac; đây không phải kiểm thử Windows kết nối điện thoại này, cũng không thể thay thế kiểm chứng lại Xiaomi OS4.0.27.

Ban đầu cửa hàng hiện "Không có kết nối mạng", ngày điện thoại là 2026-02-05, ngày máy tính là 2026-10-25. Sau khi chủ máy lên mạng, ngày điện thoại cũng thành 2026-10-25; kịch bản không sửa mạng hoặc thời gian. Sau khi lên mạng danh sách quản lý dịch vụ tăng thêm mục, một phần mục tiêu chuyển sang màn hình tiếp theo, vì vậy bổ sung tìm kiếm qua trang, đọc lại mục tiêu và kiểm tra công tắc khác giữ nguyên.

## Phiên bản ứng dụng và phạm vi tùy chỉnh

Phiên bản hệ thống và phiên bản ứng dụng sẽ ảnh hưởng riêng tới cổng vào. Phiên bản thực tế cài đặt lần này như sau:

| Ứng dụng | Phiên bản | Kết quả lần này |
|---|---|---|
| Tìm kiếm kéo xuống | 11.31.4 | "Cài đặt → Tài khoản & quyền riêng tư → Quyền riêng tư → Đề xuất cá nhân hóa" đã tìm thấy và tắt |
| Cửa hàng phần mềm | 12.21.0 | "Của tôi → Cài đặt → Quyền riêng tư → Đề xuất cá nhân hóa" là trang cài đặt cấp hai; đề xuất cá nhân hóa đã tắt |
| Vị trí quảng cáo cửa hàng phần mềm | Như trên | Sau khi chủ máy lên mạng, sáu mục quảng cáo rõ ràng đã tắt và đọc lại qua trang; các công tắc dịch vụ khác giữ nguyên |
| Trình duyệt | 40.10.1.9 | "Của tôi → Cài đặt → Quyền riêng tư → Đề xuất cá nhân hóa" đã tìm thấy và tắt; cổng vào "Cài đặt trang chủ / Quản lý quảng cáo" của kịch bản tham khảo chưa khớp |
| Cửa hàng chủ đề | 11.6.3 | Sau khi sửa một ít chữ màn hình đầu bị phán đoán nhầm thành quảng cáo trống, có thể dừng bình thường ở trang chủ ứng dụng này; cổng vào cài đặt quảng cáo vẫn chờ tùy chỉnh |
| Video | 40.7.11.1 | Trang "Của tôi" cài đặt dùng biểu tượng không chữ, chưa hoàn tất xác minh công tắc quảng cáo |
| Trung tâm trò chơi | 14.27.1 | Trang hướng dẫn và cổng vào cài đặt khác kịch bản tham khảo, chưa hoàn tất xác minh công tắc quảng cáo |
| Màn hình -1 | 14.5.134 | "Từ gợi ý ô tìm kiếm / Dịch vụ đề xuất" của kịch bản tham khảo chưa khớp, không đánh dấu thành công |

Cổng vào quảng cáo hệ thống thực tế là "Cài đặt → Quyền & quyền riêng tư → Quyền riêng tư → Định danh thiết bị & quảng cáo → Theo dõi quảng cáo". Trang này dùng danh sách trạng thái từng ứng dụng, không phải một trang công tắc như kịch bản tham khảo dự kiến; lần này không tự động xử lý danh sách này. Trong Cài đặt hệ thống cũng chưa khớp "OPPO AI → Đề xuất Xiao Bu" của kịch bản tham khảo.

## Kịch bản tham khảo gốc và kịch bản chuyên dụng

Trước tiên sao lưu, rồi chạy đầy đủ kịch bản tham khảo cùng hãng ColorOS 16 bằng chế độ an toàn, dùng 324 giây, chỉ điều chỉnh 1 mục đề xuất cá nhân hóa của tìm kiếm kéo xuống. Các mục còn lại tồn tại cổng vào không khớp hoặc dừng bảo vệ, không thể coi mã thoát lệnh 0 thành toàn bộ thành công.

Sau đó theo trang máy thật bổ sung `recipes/oneplus-PJA110/recipe.py`, gồm bốn đoạn tìm kiếm kéo xuống, cửa hàng phần mềm, vị trí quảng cáo cửa hàng, trình duyệt. Chỉ xử lý công tắc liệt kê rõ ràng, trước khi thao tác xác nhận mục tiêu, sau khi thao tác đọc lại. Khi cổng vào thiếu hoặc công tắc vẫn bật thì ghi bước chưa hoàn tất, CLI trả về khác 0; nhật ký mục đã sửa thành công vẫn giữ.

Sau khi sửa chờ khởi động lạnh, cuối cùng chạy lại đầy đủ bốn đoạn khi bốn thành phần tùy chọn giữ tạm ngưng: **155 giây, 9 mục đọc lại là tắt, điều chỉnh 0 mục, bước chưa hoàn tất 0 cái, mã thoát 0**.

Vị trí quảng cáo cửa hàng chỉ chọn sáu mục sau: biểu tượng hoạt động nổi, hộp thoại hoạt động, thẻ quay vòng phía trên, khu vực hoạt động phía dưới, thẻ hoạt động trang chi tiết trò chơi, phúc lợi phần mềm. Tải cập nhật, bảo mật ứng dụng, phân loại trò chơi thông thường, cổng vào Quick App không nằm trong danh sách này. Đoạn tắt sau khi lên mạng dùng 96 giây, 6 mục toàn bộ đọc lại tắt, bước chưa hoàn tất là 0; đồng thời đối chiếu các công tắc khác trong danh sách với trước khi thao tác là nhất quán.

## Thông báo tiếp thị

Lần quét đầu tìm thấy 27 ứng viên, giữ kênh thanh toán hỗn hợp, hai nhắc phát trực tiếp và "Tin tức quan trọng" mục đích chưa rõ, chọn 23 kênh tiếp thị rõ ràng.

Công cụ cũ đã bỏ qua ứng dụng cài đặt thông báo độc lập của ColorOS 14. Sau khi sửa chỉ chấp nhận hai Activity đã kiểm chứng thực tế:

- `com.oplus.notificationmanager.ChannelNotificationSettingsActivity`
- `com.oplus.notificationmanager.AppNotificationSettingsActivity` (chỉ dùng để tìm cổng vào kênh, không cho phép coi công tắc tổng ứng dụng thành công tắc kênh)

Vẫn cần đối chiếu tiêu đề kênh và công tắc "Cho phép thông báo" rõ ràng. Sau khi 23 kênh tắt, đọc lại số lượng vẫn bật là 0. Khi lần đầu tắt hoàn tất, đối chiếu 368 kênh hiện có, trạng thái kênh còn lại và công tắc tổng thông báo của từng ứng dụng đều nhất quán với bản sao lưu, lúc đó thêm 2 kênh.

Sau khi lên mạng và hoàn tất chạy lại toàn bộ: 23 mục tiêu vẫn tắt, công tắc tổng thông báo của mọi ứng dụng vẫn nhất quán với bản sao lưu; kênh mới tổng cộng 13 cái. Ngoài ra có 1 kênh không phải mục tiêu thay đổi: mức độ quan trọng "Nhắc thời tiết" của Thời tiết từ 4 thành 3, `mUserLockedFields` từ 0 thành 34, vẫn ở trạng thái bật. Nó không nằm trong danh sách tắt lần này, nguyên nhân thay đổi chưa xác nhận; bản ghi công khai giữ khác biệt này, không thể viết kết quả cuối thành "mọi trạng thái không phải mục tiêu đều không đổi".

"Vấn đề thanh toán, thông tin ưu đãi và nội dung đề xuất" của Google Play đồng thời mang thông báo thanh toán, đã bổ sung vào quy tắc loại trừ quét; không thể chỉ vì tên mang "đề xuất" mà tắt nó.

## Bản sửa công cụ và ranh giới xác minh

- Màn hình đầu có một hai nhãn cũng có thể là trang bình thường, không thể coi thành quảng cáo trống mà bấm quay lại.
- Cửa hàng khởi động lạnh từng xuất hiện trống thoáng qua, logic cũ sau 3 giây bấm quay lại sẽ thoát ứng dụng bình thường. Nay chờ tối đa 8 giây, chỉ xử lý nút đóng / từ chối có thể nhận diện; vẫn không có trang thì báo thất bại, không bấm quay lại mù. Trước và sau khi đọc và xử lý hộp thoại đều đối chiếu gói tiền cảnh.
- Sau khi khởi động chậm hoàn tất vẫn dành thời gian xử lý hộp thoại cập nhật, hướng dẫn.
- Cửa hàng sẽ hiện đơn xin quyền thông báo hệ thống, che trang chủ ứng dụng; chỉ bấm "Từ chối / Không cho phép" rõ ràng, không có nút từ chối thì dừng. Hộp thoại quyền xuất hiện sau khi trang chủ xuất hiện cũng xử lý, không tự động cấp quyền. Công tắc tổng thông báo cửa hàng đó trước khi thao tác đã tắt, sau khi thao tác giữ tắt.
- Cửa hàng dùng cách "dừng ứng dụng mục tiêu, rồi khởi động từ cổng vào màn hình chính" của công cụ, trình duyệt dùng Activity công khai đã xác minh và dọn nhiệm vụ cũ, tránh thoát hoặc dùng lại trang con cài đặt lần trước. Cửa hàng khi bốn thành phần tùy chọn tạm ngưng vẫn có thể vào trang chủ bình thường; không xóa dữ liệu ứng dụng.
- Kịch bản chuyên dụng dùng Activity thực tế xác nhận trang cài đặt có mở không, xử lý trường hợp cú bấm đầu tiên bị hoạt ảnh chuyển đổi nuốt mất.
- Sau khi lên mạng danh sách dịch vụ cửa hàng dài ra, phải tìm đủ mọi mục tiêu chỉ định qua trang trước, rồi thao tác, đọc lại, và kiểm tra trạng thái công tắc khác. Chỉ tìm thấy năm mục ở màn hình đầu không thể giả định mục thứ sáu không tồn tại, cũng không thể mở rộng thành tắt toàn trang.

112 mục hồi quy không liên quan thiết bị qua, bao phủ trang thông báo độc lập, giữ kênh thanh toán hỗn hợp, màn hình đầu thưa, dừng sau khi rời tiền cảnh, quyền chỉ từ chối, mục tiêu qua trang và mục giữ, mục tiêu thiếu và mã thoát thất bại. Kiểm thử đơn vị không thể thay thế kiểm chứng thực tế từng mẫu máy.

[Windows CI](https://github.com/rddmwmddr/android-ad-cleaner/actions/runs/40204906189) của commit mã nguồn `d4ee2d2` cũng qua 112 mục hồi quy, và qua đóng gói PyInstaller, dòng lệnh và kiểm thử nhanh GUI gốc / hình ảnh / JS API, tạo gói portable và chương trình cài đặt. Lần này là xác minh xây dựng thủ công, chưa phát hành Release mới, cũng chưa bao phủ gói cài đặt 0.2.3.

Bản sao lưu gốc, danh sách ứng dụng, dữ liệu thông báo và nhật ký thực thi đầy đủ chỉ lưu trên máy này tại `backups/`, không tải lên GitHub. Tài liệu công khai chỉ giữ mẫu máy, phiên bản, phạm vi thao tác và kết luận xác minh.

## Thành phần đã đóng khi chủ máy đồng ý

Sau khi chủ máy lựa chọn rõ ràng đóng toàn bộ bốn mục, thực thi `pm suspend` và đọc lại trạng thái tạm ngưng; Quick App và dịch vụ quảng cáo vẫn chạy, tiến trình Glance sau đó dừng, lần kiểm tra đầu tiên cả bốn đều không chạy.

**Dừng nền chỉ có hiệu lực một phần**: sau khi chạy lại ứng dụng như cửa hàng, tiến trình dịch vụ quảng cáo, Glance, nền tảng Quick App xuất hiện lại, trạng thái tạm ngưng của bốn gói vẫn là đúng. Sau khi kết thúc dừng lại, Glance và hai tiến trình Quick App đều không chạy, nhưng `com.opos.ads` đã chạy lại. Cơ chế kéo lại cụ thể chưa xác định, vì vậy chỉ xác nhận "bốn gói đã tạm ngưng", không thể viết thành "bốn mục đóng vĩnh viễn" hoặc "dịch vụ quảng cáo dừng hoàn toàn".

| Thành phần | Tên gói | Ảnh hưởng |
|---|---|---|
| Dịch vụ quảng cáo OPPO | `com.opos.ads` | Tạm ngưng thành phần dịch vụ quảng cáo, không bằng xác minh mọi quảng cáo hệ thống biến mất |
| Khóa màn hình Glance | `com.heytap.pictorial` | Vô hiệu hóa chức năng tạp chí khóa màn hình |
| Nền tảng Quick App | `com.nearme.instant.platform` | Vô hiệu hóa Quick App không cần cài đặt |
| Dịch vụ cục bộ Quick App | `com.oppo.instant.local.service` | Vô hiệu hóa dịch vụ Quick App tương ứng |

Cửa hàng ứng dụng, tìm kiếm kéo xuống và màn hình -1 đều xác nhận chưa bị tạm ngưng. Tạm ngưng không gỡ cài đặt ứng dụng, cũng không xóa dữ liệu; tương lai hệ thống có kéo lại không vẫn cần quan sát thực tế.

## Khôi phục

Thông báo có thể dùng danh sách đã sàng lọc lần này để khôi phục:

```bash
python tool/run.py -s <序列号> chan-on backups/PJA110-<时间>/channels-approved.tsv
```

Ba công tắc đề xuất cá nhân hóa và sáu vị trí quảng cáo cửa hàng có thể mở lại dọc đường dẫn gốc trên. Khôi phục thành phần:

```bash
python tool/run.py -s <序列号> unsuspend com.opos.ads com.heytap.pictorial
python tool/run.py -s <序列号> quickapp on
```

Đã thực thi `run.py finish`, cắm sạc luôn sáng cuối cùng đọc lại là giá trị gốc sao lưu `0`. Máy này từ chối ghi cài đặt đó, không điều chỉnh quyền bảo mật để vòng qua giới hạn, cũng không thể tuyên bố trong thời gian kiểm thử luôn giữ luôn sáng. Khi không khắc phục nữa, tắt công tắc tổng Tùy chọn nhà phát triển trên điện thoại, cài đặt gỡ quảng cáo đã hoàn tất sẽ không vì vậy mà bị hủy.

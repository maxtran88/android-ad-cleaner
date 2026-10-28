# 11 Khắc phục xung đột đọc màn hình và bảo vệ thông báo chức năng "Tìm vị trí chụp"

Cập nhật: 2026-10-26. Các thay đổi mã dưới đây chưa vào gói cài đặt 0.2.3 đã phát hành; người dùng 0.2.3 có thể xử lý trước theo bước khắc phục và khôi phục.

## Phản hồi lần này nói rõ điều gì

Môi trường phản hồi gốc là Windows 11, Xiaomi 18 Pro Max / OS4.0.27, lỗi chứa `AccessibilityServiceAlreadyRegisteredError`. Người dùng nâng cấp lên 0.2.3 vẫn thất bại, sau đó đồng thời tắt GKD và ghi sổ tự động, phản hồi có thể bắt đầu xử lý.

Điều này cung cấp hướng khắc phục xung đột dùng được, nhưng chưa đối chiếu từng công cụ, từng chế độ, cũng chưa tái hiện độc lập. Vì vậy không thể khẳng định công cụ nào chiếm dịch vụ, càng không thể suy ra mọi dịch vụ trợ năng đều phải tắt. Việc dọn dẹp phiên và loại trừ lẫn nhau của 0.2.3 vẫn giữ; lần cải tiến này là khả năng khắc phục và nhắc nhở.

[Mã đăng ký UiAutomation của Android](https://android.googlesource.com/platform/frameworks/base/+/master/services/accessibility/java/com/android/server/accessibility/UiAutomationManager.java) giới hạn cùng lúc đăng ký một dịch vụ UiAutomation, điều này không bằng dịch vụ trợ năng thông thường chỉ bật được một cái. [Giải thích chính thức GKD](https://gkd.li/guide/faq) và [giải thích dự án ghi sổ tự động](https://github.com/AutoAccountingOrg/AutoAccounting) cũng cho thấy công cụ liên quan có thể dùng trợ năng hoặc Shizuku; bối cảnh kỹ thuật này không thể chứng minh người chiếm cụ thể trên điện thoại phản hồi.

## Thứ tự xử lý khi đọc màn hình thất bại

1. Giữ điện thoại mở khóa, thoát ứng dụng gỡ quảng cáo trùng lặp, cùng Appium, trình kiểm tra UI và các nhiệm vụ khác đang thao tác điện thoại này.
2. Kiểm tra GKD, ghi sổ tự động và các công cụ tương tự có bật tự động hóa, đọc màn hình hoặc chế độ Shizuku không. Chỉ tạm dừng chức năng bạn xác nhận có thể tạm dừng; khi cần, chính chủ tạm thời tắt dịch vụ trợ năng của ứng dụng tương ứng.
3. Giữ trình đọc màn hình và dịch vụ hỗ trợ mà mình phụ thuộc, đừng tắt toàn bộ trợ năng bằng một cú bấm. Sau khi tạm dừng bấm "Kiểm tra kết nối đọc màn hình", mỗi lần thay đổi một mục rồi kiểm tra lại, tiện xác định.
4. Vẫn thất bại thì chủ máy có thể tự khởi động lại điện thoại; sau khi mở khóa trước tiên không khởi động các công cụ tự động hóa trên, rồi kiểm tra. Tiếp tục thất bại thì sao chép chẩn đoán đầy đủ.
5. Sau khi gỡ quảng cáo kết thúc, phiên đọc màn hình thoát, khôi phục công cụ đã tạm dừng theo nhu cầu.

Ứng dụng sẽ không thay người dùng tắt công tắc tổng trợ năng, sửa danh sách dịch vụ, dừng mạnh công cụ khác hoặc khởi động lại điện thoại. Kiểm tra phụ trợ sau thất bại chỉ qua adb đọc công tắc tổng và số lượng dịch vụ đã cấu hình, chờ tối đa 3 giây; định danh dịch vụ và danh sách ứng dụng không ghi vào chẩn đoán. Đọc thất bại sẽ không ghi đè ngoại lệ gốc.

Công tắc tổng bật hoặc số lượng dịch vụ lớn hơn 0 chỉ là manh mối, không đại diện đã tìm thấy người chiếm; đọc được tắt hoặc 0 mục, cũng không thể loại trừ phiên tự động hóa / Shizuku độc lập. Kết quả kiểm tra đọc màn hình của giao diện và trang hoàn tất thực thi đều sẽ đưa nhắc khắc phục, tránh nhắc bị ngăn xếp dài chôn vùi.

## Phạm vi bảo vệ thông báo "tìm vị trí chụp"

Người dùng khác báo thông báo "tìm vị trí chụp" của dòng Xiaomi 18 Pro bị quy trình thông báo tiếp thị tắt nhầm. Chức năng này thuộc thông báo chức năng người dùng cần, không thể vì tên kênh hoặc ID mang từ "đề xuất / hoạt động / recommend" v.v. mà tắt.

Bảo vệ hiện tại tên chứa "找机位", "机位推荐", "推荐机位" của kênh, kiêm giản thể / phồn thể, khoảng trắng và ký tự độ rộng 0. Bảo vệ bao phủ:

- Ứng viên quét: loại trừ các thông báo chức năng này.
- Danh sách ứng dụng: ngay cả khi nhận kết quả quét cũ, cũng không đưa nó vào danh sách tiếp thị có thể chọn tất cả.
- Thực thi danh sách cũ: đối chiếu tên kênh hiện tại của điện thoại, ID kênh và mô tả danh sách, trúng quy tắc bảo vệ thì bỏ qua; chỉ có những mục này thì không khởi động đọc màn hình.
- Trước khi bấm thực tế: đọc lại tên hiện tại một lần nữa, tránh nhãn danh sách cũ hoặc đổi tên sau khi quét vòng qua bảo vệ.
- Thống kê kiểm tra lại: kênh được bảo vệ không tính vào "kênh tiếp thị vẫn bật", và ghi chú giữ lại; kênh tiếp thị thông thường vẫn xử lý bình thường.

Hiện tại vẫn chưa nhận được tên gói thật, tên kênh đầy đủ và ID kênh của chức năng này; hiện tại là bảo vệ theo tên, không phải tùy chỉnh ID chính xác đã xác minh trên điện thoại phản hồi. Nếu tên thực tế của nó khác với từ trên, vẫn cần bổ sung thông tin rồi hoàn thiện quy tắc.

## Kênh đã tắt nhầm khôi phục thế nào

Có thể vào cài đặt thông báo hệ thống của ứng dụng thuộc chức năng đó, tìm kênh tương ứng "找机位 / 机位推荐", chỉ mở lại mục này.

Khi có danh sách gốc, cũng có thể sao chép dòng tương ứng của kênh đó vào `restore-photo-spot.tsv` riêng, giữ tên gói gốc và ID kênh, rồi thực thi:

```bash
python tool/run.py -s "<序列号>" chan-on "backups/<原备份目录>/restore-photo-spot.tsv"
```

Sau khi thực thi xem kết quả đọc lại, xác nhận kênh đó là bật. Quy tắc bảo vệ mới chỉ ngăn tắt, không ngăn khôi phục thực thi rõ ràng. Quét hoặc gỡ quảng cáo lại sẽ không tự mở kênh trước đây đã tắt, để tránh ghi đè lựa chọn gốc của người dùng.

## Xác minh và mục chờ xác nhận

123 mục hồi quy không liên quan thiết bị qua, bao phủ kiểm tra chỉ đọc và hết thời gian chờ, danh sách dịch vụ không rò rỉ, ngoại lệ gốc giữ lại, nhắc lỗi GUI, loại trừ ứng viên thông báo chức năng, bảo vệ danh sách cũ, kiểm tra lại trước khi bấm, trạng thái đã tắt giữ lại và khôi phục có định hướng. Kiểm thử nhanh GUI gốc khác xác minh khi mô phỏng đọc màn hình thất bại thẻ khắc phục và nút thực tế xuất hiện.

Commit mã [`92a539f`](https://github.com/rddmwmddr/android-ad-cleaner/commit/92a539f07267b751fe0dfa9246dc1bba61e68fb7) đã qua hồi quy cục bộ Mac và kiểm thử nhanh GUI gốc, cùng [Actions #40213007991](https://github.com/rddmwmddr/android-ad-cleaner/actions/runs/40213007991) của Windows hồi quy, đóng gói PyInstaller, kiểm thử nhanh GUI gốc / CLI, tạo gói portable và chương trình cài đặt. Bản dựng Windows lần này là xác minh thủ công, chưa tải lên Release, cũng chưa thay thế gói cài đặt 0.2.3 đã phát hành; đóng gói qua không thể thay thế kiểm chứng lại trên điện thoại của người phản hồi.

Đợt này không tắt bất kỳ dịch vụ trợ năng máy thật nào, cũng không thay người phản hồi mở lại thông báo. Vẫn cần người phản hồi cung cấp siêu dữ liệu kênh, và trên thiết bị của họ xác minh sàng lọc mới và khôi phục có định hướng; đồng thời tắt hai công cụ rồi thành công, không thể ghi thành nguyên nhân gốc của một công cụ đã chứng minh.

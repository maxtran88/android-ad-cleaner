# 06 Câu hỏi thường gặp

## Có ảnh hưởng tới cập nhật hệ thống không?

Không. Không root, không mở khóa, không sửa phân vùng system. Tạm ngưng (`pm suspend`) chỉ tạm dừng một ứng dụng, việc nhận và cài đặt cập nhật hệ thống không bị ảnh hưởng.

## Có ảnh hưởng tới bảo hành không?

Không. Dùng tới là Tùy chọn nhà phát triển và mục cài đặt có sẵn của hệ thống.

## Tắt xong vẫn còn quảng cáo không?

Sẽ còn một số:

| Phần còn lại | Lý do |
|---|---|
| Từ khóa nóng quay vòng trong ô tìm kiếm trình duyệt | Trong cài đặt không có công tắc |
| Hộp thoại "Bắt buộc khi khởi động" của Cửa hàng phần mềm OPPO | Tắt hết Quản lý dịch vụ rồi vẫn hiện |
| Tìm kiếm kéo xuống chỉ dùng được Baidu | Cấu hình bản Trung Quốc chỉ phát xuống một công cụ tìm kiếm, không root thì không sửa được |
| Một số ứng dụng dừng ở trang "Đồng ý thỏa thuận" | Dự án này không thay bạn đồng ý, chưa vào được thì không tắt được |
| Ứng dụng mới cài | Theo dõi quảng cáo mặc định bật, thông báo tiếp thị mặc định bật; chạy lại một lần phần chung |

## Sau khi cập nhật hệ thống có cần chạy lại không?

Nên chạy lại. Cập nhật phiên bản lớn sẽ khôi phục một phần công tắc về mặc định, cũng có thể đổi vị trí trang cài đặt. Trước khi chạy lại chạy một lần `check`, xem phiên bản kịch bản theo mẫu máy có khớp không.

## Vì sao không gỡ cài đặt ứng dụng quảng cáo?

Ứng dụng hệ thống bản Trung Quốc không root thì không gỡ được; `pm disable-user` phần lớn bị hệ thống từ chối, số ít dừng được thì dừng rồi sẽ kéo theo hỏng chức năng. Tạm ngưng có thể khôi phục bằng một lệnh, nên chỉ dùng tạm ngưng.

## Tạm ngưng gói nào sẽ hỏng chức năng?

Đã kiểm chứng thực tế:

| Gói | Tác dụng | Kết quả tạm ngưng |
|---|---|---|
| `com.heytap.quicksearchbox` | Tìm kiếm kéo xuống OPPO | Tìm kiếm không mở được, không được tạm ngưng |
| `com.coloros.assistantscreen` | Màn hình -1 OPPO | Thẻ biến mất hết, không được tạm ngưng |
| `com.opos.ads` | Dịch vụ quảng cáo OPPO | Bình thường |
| `com.heytap.pictorial` | Khóa màn hình Glance OPPO | Bình thường, tạp chí khóa màn hình biến mất |
| `com.miui.systemAdSolution` | Quảng cáo hệ thống Xiaomi | Bình thường, cần phối hợp chặn mạng |
| `com.hihonor.quickengine` v.v. | Quick App, trò chơi nhanh Honor | Bình thường |

## Kịch bản báo "không tìm thấy" thì làm sao?

Phiên bản hệ thống của bạn khác với lúc ghi kịch bản theo mẫu máy, trang cài đặt đổi tên hoặc vị trí. Ba cách xử lý:

1. Để AI làm theo danh sách từng bước một, làm xong lưu thành kịch bản theo mẫu máy mới.
2. Làm theo [danh sách](checklists/) thủ công để tắt.
3. Gửi Issue, ghi rõ mẫu máy, phiên bản hệ thống, đoạn nào không tìm thấy.

## Trên Windows ứng dụng không nhận ra điện thoại?

Kiểm tra theo thứ tự (trường hợp [Issue #6](https://github.com/rddmwmddr/android-ad-cleaner/issues/6) kiểm tra xong là được):

1. Đổi dây truyền được dữ liệu, cắm cổng USB phía sau máy tính.
2. Kéo thanh thông báo trên điện thoại xuống, mục đích USB chọn "Truyền tệp".
3. Trong Tùy chọn nhà phát triển tắt rồi bật lại "Gỡ lỗi USB", hộp thoại trên điện thoại tích "Luôn cho phép", bấm "Cho phép". Không có hộp thoại thì bấm "Thu hồi ủy quyền gỡ lỗi USB" rồi cắm lại.
4. Honor, Huawei: trong Tùy chọn nhà phát triển bật thêm "Chỉ chế độ sạc mới cho phép gỡ lỗi ADB".
5. Cài trình điều khiển USB của hãng điện thoại, xem [08-ung-dung-desktop](08-ung-dung-desktop.md). Samsung cần cài Samsung Android USB Driver chính thức; Honor, Huawei có thể cài trợ lý điện thoại tương ứng để lấy trình điều khiển, cài xong thoát trợ lý điện thoại.
6. Tắt các trợ lý điện thoại và trình giả lập Android khác trên máy tính (chúng sẽ chiếm kết nối).

Từ 0.2.4, trên Windows khi không chờ được điện thoại, ứng dụng sẽ chỉ đọc truy vấn Trình quản lý thiết bị: điện thoại đang cắm không có giao diện gỡ lỗi, giao diện gỡ lỗi thiếu trình điều khiển, sẽ nhắc trực tiếp là loại nào. Trên máy tính chỉ có adb cũ loại 1.0.32, ứng dụng không dùng nó nữa, đổi thành nhắc tải adb chính thức.

## Xiaomi / Redmi: rất nhiều "không tìm thấy", "bấm xong trạng thái kênh không thay đổi", giữa chừng còn khóa màn hình?

Trong Tùy chọn nhà phát triển còn phải bật "Gỡ lỗi USB (cài đặt bảo mật)", mục này cần cắm SIM, đăng nhập tài khoản Xiaomi. Không bật nó, máy tính đọc được màn hình, nhưng cú bấm gửi đi sẽ bị hệ thống từ chối, cài đặt cũng không ghi vào được: mỗi đoạn kịch bản theo mẫu máy đều "không tìm thấy", mỗi thông báo tiếp thị đều "bấm xong trạng thái kênh không thay đổi", cắm sạc luôn sáng đặt không lên, chạy một lúc là khóa màn hình.

0.2.4 ở trang phát hiện thử trước một lần (gửi một phím trống không kích hoạt thao tác nào), bị từ chối thì nhắc bật mục này, tạm thời chưa vào bước tiếp theo.

## Chạy giữa chừng báo `device '<序列号>' not found`?

Kết nối adb giữa điện thoại và máy tính giữa chừng bị đứt. Thường gặp nhất là trên máy tính đồng thời mở trợ lý điện thoại, kho ứng dụng, 360 Mobile Assistant, Wandoujia, iTools, công cụ flash hoặc trình giả lập Android, chúng mang theo một phiên bản adb khác, sẽ tranh giành kết nối với công cụ này. Cũng có thể dây, cổng hoặc đế mở rộng tiếp xúc kém.

0.2.4 sẽ chờ điện thoại quay lại thử lại một lần; vẫn ngắt kết nối thì dừng ở bước này và nói rõ lý do, các bước sau không còn hiện "Thành công". 0.2.3 trở về trước, sau khi ngắt đọc được kết quả trống, tên thư mục ảnh chụp nhanh sẽ thành "-ngày", Quick App hiện "không phát hiện", những kết quả này đều không đáng tin, vui lòng cập nhật rồi chạy lại. Khi sao chép chẩn đoán, sẽ liệt kê các adb khác đang chạy trên máy tính.

## Thông báo tiếp thị báo "Công tắc trang thông báo vivo này sẽ ảnh hưởng toàn bộ ứng dụng"?

Đây là nhắc của 0.2.3. Trang tổng thông báo ứng dụng và trang kênh đơn lẻ của vivo / iQOO do cùng một trang `com.vivo.systemuiplugin` đảm nhiệm: "Cho phép thông báo" của trang tổng sẽ tắt thông báo toàn bộ ứng dụng, thông báo đơn hàng, trò chuyện cũng mất theo; trang kênh chỉ quản một kênh. 0.2.3 đã từ chối toàn bộ trang này.

0.2.4 vẫn không bấm trang tổng, chỉ thao tác trên trang kênh đi vào từ trang tổng, thanh trên là tên kênh, sau khi bấm đối chiếu công tắc tổng ứng dụng không thay đổi (X300 Ultra / OriginOS 6 kiểm chứng thực tế). Khi tên kênh và tên ứng dụng giống nhau thì không phân biệt được, sẽ bỏ qua, có thể vào kênh này trên điện thoại tắt thủ công; đừng dùng công tắc tổng ứng dụng thay thế.

## Chẩn đoán sao chép dán ra là ký tự loạn?

0.2.3 trở về trước trên Windows qua PowerShell ghi clipboard, hệ thống tiếng Trung giải mã theo GBK, dán ra là ký tự loạn dạng "鎻忚堪". 0.2.4 đổi thành ghi trực tiếp clipboard Unicode; khi chẩn đoán dài, trong địa chỉ phản hồi cũng sẽ mang theo mẫu máy, kết quả từng bước và đoạn nhật ký, không còn chỉ một câu "Vui lòng dán".

## Bản Mac Intel không mở được?

Gói cài đặt Intel 0.2.0–0.2.3 dùng nhầm Python biên dịch theo macOS 26, Mac Intel thấp hơn macOS 26 không mở được ([#103](https://github.com/rddmwmddr/android-ad-cleaner/issues/103)). 0.2.4 đổi dùng Python hỗ trợ tối thiểu macOS 11, khi đóng gói kiểm tra từng tệp về phiên bản hệ thống tối thiểu. macOS 10.15 trở về trước vẫn không hỗ trợ.

## Công tắc "Hạn chế theo dõi quảng cáo" là bật hay tắt?

Bật. Các công tắc dạng "Hạn chế theo dõi quảng cáo", "Ngăn chặn theo dõi quảng cáo" là ngược, bật lên mới là bảo vệ. Công cụ sẽ gạt chúng sang "bật", không coi là công tắc quảng cáo mà tắt đi.

## Điện thoại gập chạy không được?

Gập lại, dùng màn hình ngoài. Mở ra là bố cục hai cột, phía dưới có thanh tác vụ, công cụ sẽ tìm sai vị trí. 0.2.1 khi đọc màn hình làm mới kích thước và loại bỏ nút ngoài màn hình (Issue #2 / #21), tránh bỏ sót công tắc phía phải khi xoay ngang hoặc bấm ra ngoài màn hình, xem [Nhật ký thay đổi](../../CHANGELOG.md).

## Ô tìm kiếm Xiaomi cứ nhập `%` mãi?

Kịch bản theo mẫu máy Xiaomi của mã nguồn hiện tại đổi đi theo menu vào dịch vụ quảng cáo, tránh phụ thuộc tìm kiếm cài đặt. Tìm kiếm chung cũng tăng thêm sẵn sàng ô nhập, hết thời gian nhập và kiểm tra chữ, thất bại thì dừng nhập. Vui lòng nâng cấp lên 0.2.1, cũng có thể [chạy từ mã nguồn](08-ung-dung-desktop.md), hoặc làm thủ công theo [danh sách Xiaomi](checklists/Xiaomi-HyperOS.md).

## Liên kết danh sách vivo của ứng dụng không mở được?

Có thể mở trực tiếp [danh sách vivo / OriginOS](checklists/vivo-OriginOS.md). Mã nguồn hiện tại đã chọn tệp cụ thể theo hãng và mã hóa đường dẫn tiếng Trung, vivo và iQOO đều trỏ tới danh sách này; bản sửa đã vào 0.2.1, liên kết cũ của 0.2.0 cần cập nhật ứng dụng rồi mới thay đổi.

## Mở trên Windows hiện "127.0.0.1 phản hồi quá lâu"?

Xem [Issue #18](https://github.com/rddmwmddr/android-ad-cleaner/issues/18). Mã nguồn hiện tại dùng `file://` tải trực tiếp trang cục bộ, không còn phụ thuộc dịch vụ HTTP xảy ra hết thời gian chờ; máy tính Windows 11 của người báo cáo vẫn cần kiểm chứng lại. Vui lòng ưu tiên cập nhật lên 0.2.1; tạm thời chưa cập nhật được thì có thể dùng [dòng lệnh tích hợp của 0.2.0](08-ung-dung-desktop.md) để kiểm tra chỉ đọc, hoặc làm theo [danh sách thủ công](checklists/).

## Honor hiện "không nhận ra" hoặc "không hỗ trợ"?

Trước tiên phân biệt hai trường hợp: trang kết nối mãi không có thiết bị, kiểm tra dây dữ liệu, ủy quyền gỡ lỗi USB và trình điều khiển Windows; đã hiện mẫu máy nhưng không có kịch bản theo mẫu máy, tức là mẫu máy đó thiếu đường dẫn đã ghi. Mã nguồn hiện tại có thể chủ động chọn kịch bản tham khảo cùng hãng, mặc định không tích chọn; Magic5, Magic6, 100 Pro, Magic7 Pro vẫn chưa thể căn cứ vào đó mà tính là đã tùy chỉnh xong toàn máy. Khi phản hồi đính kèm mã mẫu máy, phiên bản hệ thống, giai đoạn phát hiện và thông tin lỗi.

## HarmonyOS gốc dùng được không?

Hiện tại chỉ thao tác được thiết bị Android kết nối qua adb, chưa thực hiện gỡ lỗi HDC và tự động hóa giao diện của HarmonyOS gốc. HDC là công cụ gỡ lỗi thiết bị độc lập, xem [tài liệu Huawei](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V13/hdc-V13). Nếu thiết bị chỉ cung cấp kết nối HDC, cài trình điều khiển USB Android hoặc mượn kịch bản Honor không làm nó tương thích được; đừng coi "Honor" và "HarmonyOS gốc" là cùng một hệ thống.

## Quét không có kênh tiếp thị, có phải đã hết quảng cáo không?

Không phải. Chỉ quét được kênh thông báo ứng dụng đã tạo, thiết bị mới hoặc vừa đặt lại có thể rất ít; số lượng cũng chịu ảnh hưởng của việc cài đặt và sử dụng ứng dụng. Ứng dụng cần tạo kênh trước rồi mới gửi thông báo, việc tạo không nhất thiết phải đợi tới lần đầu gửi thông báo mới xảy ra, xem [tài liệu thông báo Android](https://developer.android.google.cn/develop/ui/compose/notifications/create-notification?hl=en). Sau khi sử dụng bình thường có thể quét lại; ứng dụng hiện tại sẽ phân biệt rõ "không có ứng viên" và "quét thất bại".

## Báo cáo nhật ký lỗi sẽ gửi gì?

Chỉ gửi những nội dung hiện trong hộp thoại: phiên bản ứng dụng, hệ thống máy tính, mẫu máy và phiên bản hệ thống điện thoại, kết quả từng bước, cuối nhật ký, cùng một mã cài đặt ngẫu nhiên. Số sê-ri, thư mục người dùng, email, số điện thoại, IP đều đã thay thế, không có danh sách ứng dụng và nội dung thông báo. Máy chủ lưu 90 ngày, IP chỉ lưu băm. Xem chi tiết [Báo cáo nhật ký lỗi](12-bao-cao-nhat-ky-loi.md).

## Dữ liệu có an toàn không?

Kịch bản chạy trên máy tính của chính bạn, không tải lên mạng bất cứ thứ gì. Ảnh chụp nhanh lưu ở `backups/` cục bộ, trong đó có danh sách ứng dụng và bản ghi thông báo, đừng tải lên kho công khai. `.gitignore` đã loại trừ thư mục này.

## Lúc chạy có dùng được điện thoại không?

Không được. Kịch bản đang bấm màn hình, bạn chạm vào là loạn. Toàn bộ quá trình giữ sáng màn hình, mở khóa, cắm dây.

## Quét thông báo báo lỗi QueryController / UiDevice thì làm sao?

Vui lòng cập nhật lên 0.2.3. Bản quét cũ sẽ khởi động UiAutomation một cách không cần thiết, phía điện thoại khởi tạo thất bại thì không liệt kê được kênh; bản mới đổi thành quét chỉ đọc bằng adb. Việc tắt công tắc thực tế vẫn cần đọc màn hình, trước tiên bấm "Kiểm tra kết nối đọc màn hình", thất bại thì "Sao chép chẩn đoán đầy đủ" cung cấp ngoại lệ gốc. `Failed to execute script app` ở cuối ảnh chụp màn hình chỉ là kết quả thoát chương trình, không thể dùng nó để phán đoán nguyên nhân cụ thể phía điện thoại. Xem chi tiết [giải thích khắc phục sự cố của ứng dụng](08-ung-dung-desktop.md).

## Nhật ký đầy đủ nhắc already registered, quảng cáo và thông báo tiếp thị đều thất bại?

Dịch vụ đọc màn hình phía điện thoại đã được đăng ký, kết nối mới bị từ chối, người chiếm cụ thể không thể chỉ dựa vào ngăn xếp mà xác định. 0.2.3 đã bổ sung giải phóng phiên hiện tại, loại trừ lẫn nhau cùng máy và một lần thử lại có giới hạn; xung đột kéo dài sẽ bỏ qua các bước đọc màn hình sau đó và giữ lỗi đầu tiên. Vui lòng thoát ứng dụng cũ và các công cụ tự động hóa điện thoại khác; vẫn thất bại thì chủ máy tự khởi động lại điện thoại, mở khóa rồi chỉ mở một ứng dụng, trước tiên bấm "Kiểm tra kết nối đọc màn hình". Không cần tắt dịch vụ trợ năng hoặc xóa dữ liệu. Xem chi tiết [bước khôi phục và phạm vi xác minh](08-ung-dung-desktop.md).

## Đọc màn hình thất bại có thể liên quan tới GKD, ghi sổ tự động không?

Đã có phản hồi của người dùng đồng thời tạm dừng hai công cụ này rồi khôi phục thao tác, nhưng công cụ và chế độ cụ thể vẫn chưa xác định. Gặp UiAutomation đã đăng ký hoặc kết nối đọc màn hình thất bại, vui lòng kiểm tra từng mục theo [khắc phục xung đột đọc màn hình](11-xung-dot-doc-man-hinh-va-bao-ve-thong-bao-chuc-nang.md); chỉ do chính chủ tạm dừng chức năng tự động hóa có thể tạm dừng, giữ lại dịch vụ hỗ trợ phụ thuộc, hoàn tất rồi khôi phục theo nhu cầu. Giải thích này cũng bao gồm cách khôi phục một kênh sau khi thông báo tìm vị trí chụp bị tắt nhầm.

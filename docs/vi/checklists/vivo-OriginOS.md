# Danh sách thủ công vivo / OriginOS

Đường dẫn kiểm chứng thực tế mẫu máy: vivo X300 Ultra (V2547DA, OriginOS 6, Android 16), 2026-10-22. Cấu trúc iQOO tương tự. Mã nguồn hiện tại thêm kịch bản theo mẫu máy `recipes/vivo-V2547DA/`, thực thi tự động toàn đoạn vẫn chờ xác minh máy thật; V2547A cũng sẽ khớp nó, phiên bản khác nhau đi chế độ an toàn, không đại diện OriginOS 7 đã tùy chỉnh. Phạm vi phát hành và xác minh xem [Nhật ký thay đổi](../../../CHANGELOG.md).
Ký hiệu: 🔴 Tắt　🟢 Giữ lại　⚠️ Chú ý

---

## 1. Hệ thống: Quảng cáo & quyền riêng tư

**Đường dẫn**: Cài đặt → Bảo mật → Cài đặt bảo mật khác → Quảng cáo & quyền riêng tư

- 🔴 Quảng cáo cá nhân hóa, đề xuất cá nhân hóa, dịch vụ đề xuất thông minh

## 2. Màn hình -1

**Đường dẫn**: Màn hình chính từ cạnh trái vuốt sang phải → bánh răng góc trên bên phải → Cài đặt khác → Đề xuất cá nhân hóa

- 🔴 Đề xuất dịch vụ, đề xuất tin tức
- 🔴 Nội dung nổi bật, tin tức nóng
- 🟢 Gợi ý Xiao V (chuyến bay, nhắc giao hàng)
- ⚠️ Cuộc sống tiện lợi → Dịch vụ đề xuất đừng tắt: 10 biểu tượng đó (quét mã, đèn pin, máy tính v.v.) đều nhờ nó lấp vị trí, tắt rồi cả khối trống rỗng.

## 3. Tìm kiếm toàn cục

**Đường dẫn**: Cài đặt → Quản lý hệ thống & nâng cấp → Tìm kiếm toàn cục

- 🔴 Nội dung hiển thị trang chủ → Từ đề xuất ô tìm kiếm, thẻ đề xuất
- 🔴 Bảng xếp hạng tìm kiếm nóng đề xuất → Tìm kiếm phổ biến
- 🔴 Nội dung cá nhân hóa → Cá nhân hóa quảng cáo
- 🟢 Lịch sử, gợi ý ứng dụng, cá nhân hóa kết quả tìm kiếm

## 4. Cửa hàng ứng dụng

**Đường dẫn**: Cửa hàng ứng dụng → Của tôi → Cài đặt

- 🔴 Giới thiệu → Đề xuất cá nhân hóa
- 🔴 Quản lý dịch vụ → Điểm danh có quà, ảnh quay vòng phía trên, cột phía trên, mở đầu, lắc, cửa sổ nổi, quảng cáo có thời hạn
- 🟢 Dịch vụ của tôi, dọn dẹp dung lượng
- ⚠️ Trang hướng dẫn mở đầu bỏ tích "Bật nhận đẩy tin nhắn để nhận hoạt động".

## 5. Trình duyệt

**Đường dẫn**: Trình duyệt → Của tôi → bánh răng

- 🔴 Cài đặt trang chủ → Trang chủ cực giản; trang chủ vuốt lên hiển thị tin tức
- 🔴 Cài đặt quyền riêng tư → Nội dung cá nhân hóa, đề xuất cá nhân hóa từ nguồn ứng dụng bên thứ ba
- 🔴 Cài đặt duyệt web → Đề xuất liên quan tải về trên web
- 🔴 Cài đặt khác → Kết nối WiFi nhảy tới tin tức
- ⚠️ Trang trình duyệt thường nhảy tới tin tức, tiểu thuyết, hộp thoại nhận xu, từng bước xem một.

## 6. Khóa màn hình xem hình

**Đường dẫn**: Cài đặt → Màn hình chính, khóa màn hình & hình nền → Cài đặt khóa màn hình → Khóa màn hình xem hình

- 🔴 Khóa màn hình xem hình (khi tắt "Khóa màn hình vuốt ngang vào xem hình" thì công tắc tổng theo đó tắt)
- 🟢 Hình nền khóa màn hình không đổi

## 7. i Quản gia

**Đường dẫn**: i Quản gia → Cài đặt → Giới thiệu → Cài đặt cá nhân hóa

- 🔴 Đề xuất cá nhân hóa ứng dụng

## 8. Thời tiết

**Đường dẫn**: Thời tiết → Cài đặt → Dịch vụ thời tiết

- 🔴 Thông báo tin tức nóng liên quan thời tiết
- 🟢 Cảnh báo khí tượng, thời tiết bất thường, cảnh báo động đất

## 9. Thông báo tiếp thị

Kênh phân loại đẩy vivo: `VPushChannel_0` (tin nhắn vận hành), `VPushChannel_4` (tin nhắn đặc sắc), `VPushChannel_6` (tin nhắn đề xuất).

- 🔴 Alipay vận hành, đặc sắc; Douyin vận hành, đề xuất; đẩy dịch vụ đám mây; gợi ý đẩy thông minh mẹo sử dụng; ưu đãi Play; Edge tin tức nóng, tin tức đột phá
- ⚠️ Kiểm chứng thực tế cộng đồng OriginOS 7 mới nhất phát hiện, "Cho phép thông báo" của trang `com.vivo.systemuiplugin` là công tắc tổng cấp ứng dụng, tắt sẽ tắt cả thông báo đơn hàng, trò chuyện. Mã nguồn hiện tại ở trang này bỏ qua trực tiếp, không tiếp tục thao tác theo kênh; không thể coi nó thành cổng vào dự phòng kênh an toàn. Căn cứ [PR #20](https://github.com/rddmwmddr/android-ad-cleaner/pull/20), chờ các phiên bản khác xác minh từng cái một.
- ⚠️ Trang kênh do `com.vivo.systemuiplugin` xử lý, đừng dừng mạnh nó.

## 10. Gói quảng cáo và Quick App

Máy này không tạm ngưng gói nào, công tắc trong ứng dụng đủ dùng.

- ⚠️ Quick App `com.vivo.hybrid`: trên X300 Ultra (V2547A, Android 17) hệ thống từ chối tạm ngưng ([Issue #7](https://github.com/rddmwmddr/android-ad-cleaner/issues/7)). Theo bằng chứng máy thật của [PR #20](https://github.com/rddmwmddr/android-ad-cleaner/pull/20), mã nguồn hiện tại khi đọc được `switch_quick_app_service` thì qua công tắc dịch vụ hệ thống tắt và xác minh, lưu giá trị gốc trước; `quickapp on` theo sao lưu của thiết bị này khôi phục, không tìm thấy sao lưu sẽ không trực tiếp ghi thành bật. Kho này chưa dùng máy thật vivo kiểm chứng lại cách thực hiện này.
- 🟢 Cuộc sống thông minh `com.vivo.vhome` thuộc chức năng nhà thông minh, ngay cả khi đăng ký cổng vào `hap://` cũng không coi là thành phần quảng cáo Quick App.

---

## Cái bẫy của vivo

| Hiện tượng | Cách đối phó |
|---|---|
| Trang cài đặt màn hình -1, tìm kiếm toàn cục, chủ đề, i Quản gia không mở lên được | Chỉ có thể từ ứng dụng hoặc Cài đặt hệ thống bấm vào |
| Hàng danh sách và công tắc mỗi cái có một trạng thái | Lấy bản thân công tắc làm chuẩn |

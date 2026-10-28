# Danh sách thủ công Xiaomi / HyperOS

Mẫu máy kiểm chứng thực tế xem bảng dưới. Cấu trúc Redmi, POCO tương tự, không có kịch bản của mẫu máy này thì ứng dụng có thể mượn bản này làm tham khảo (chế độ an toàn).
Ký hiệu: 🔴 Tắt　🟢 Giữ lại　⚠️ Chú ý

| Mẫu máy | Hệ thống | Nguồn |
|---|---|---|
| Xiaomi 18 Pro Max (M154FF) | HyperOS OS4.0.24, Android 17 | Kiểm chứng thực tế 2026-10-22; kịch bản chín đoạn chạy lại qua ngày 2026-10-25 |
| Xiaomi 18 Fold (2608BPX34C) | CP2A.260605.016, Android 17 | Kiểm chứng thực tế cộng đồng 2026-10-24 ([Issue #2](https://github.com/rddmwmddr/android-ad-cleaner/issues/2)) |

Hai máy gói hệ thống nền giống nhau, khác nhau ở phiên bản ứng dụng: cửa hàng, trình duyệt, tìm kiếm toàn cục, quản gia điện thoại nâng cấp rồi cổng vào thay đổi. Mỗi mục dưới đây đều viết hai loại cổng vào "bản cũ / bản mới", theo cái bạn thấy trên điện thoại mà chọn.

---

## 1. Quảng cáo hệ thống

**Đường dẫn**: Cài đặt → Quyền riêng tư & bảo mật → (bản mới thêm một lớp "Bảo mật") → Cài đặt bảo mật khác → Dịch vụ quảng cáo

- 🔴 Đề xuất quảng cáo cá nhân hóa
- ⚠️ Công tắc dạng "Hạn chế theo dõi quảng cáo", "Ngăn chặn theo dõi quảng cáo" là ngược: phải **bật**.

## 2. Cửa hàng ứng dụng

**Đường dẫn**: Cửa hàng ứng dụng → Của tôi → bánh răng góc trên bên phải

- 🔴 Cài đặt quyền riêng tư (bản cũ gọi là "Quyền riêng tư") → Dịch vụ cá nhân hóa; cửa hàng 4.129.s.00 cần bấm vào trang con "Dịch vụ cá nhân hóa", rồi tắt công tắc bên trong
- 🔴 Chuyển chế độ → Chế độ cực giản (chỉ còn tìm kiếm, cài đặt, cập nhật). Cửa hàng bản mới không có mục này
- 🔴 Cài đặt thông báo → Trợ giúp người mới
- 🟢 Cài đặt thông báo → Cập nhật ứng dụng
- ⚠️ "Tin nhắn đẩy" trong Cài đặt thông báo đừng tắt: nó là công tắc cha, tắt rồi "Tin nhắn thích", "Tin nhắn bình luận" tắt cùng.

## 3. Quản gia điện thoại

**Đường dẫn**: Quản gia điện thoại → bánh răng góc trên bên phải

- 🔴 Cài đặt quyền riêng tư → Đề xuất cá nhân hóa
- 🔴 Dọn rác → Nội dung đề xuất
- ⚠️ Quản gia điện thoại bản mới (13.6.5) hai mục này đều không có, bỏ qua.

## 4. Quản lý tải về

**Đường dẫn**: Quản lý tải về → "Thêm" góc trên bên phải → Cài đặt → Cài đặt luồng thông tin (một phần phiên bản trực tiếp là bánh răng)

- 🔴 Đề xuất tài nguyên, đề xuất bảng nóng

## 5. Chủ đề

**Đường dẫn**: Chủ đề → Của tôi → bánh răng góc trên bên phải

- 🔴 Mỗi lần nối mạng thì thông báo
- 🟢 Tự động cập nhật (kề với mục trên, đừng bấm nhầm hàng)
- 🔴 Cài đặt quyền riêng tư → Đề xuất cá nhân hóa

## 6. Trình duyệt

**Đường dẫn**: Trình duyệt → Của tôi → bánh răng

- 🔴 Quyền riêng tư và bảo mật → Đề xuất nội dung cá nhân hóa, đề xuất quảng cáo cá nhân hóa (bản cũ mới đều có)
- 🔴 Bản cũ: Cài đặt trang chủ → Đẩy vị trí ô; Cài đặt tìm kiếm → Hiện mô-đun đoán bạn muốn tìm; Cài đặt chức năng → Tiểu thuyết (🟢 Đám mây của tôi)
- ⚠️ Bản mới ba mục này đều không có. Cài đặt trang chủ chỉ còn "Bản khám phá / Trang chủ tùy chỉnh", trang chủ tùy chỉnh cần điền địa chỉ web, `about:blank` điền không vào, có thể điền `https://www.bing.com`. Theo sở thích của bạn chọn, không chọn cũng được.
- ⚠️ Trình duyệt sẽ hiện hộp đăng nhập tài khoản Xiaomi, bấm "Hủy".

## 7. Tìm kiếm toàn cục

**Đường dẫn**: Màn hình chính vuốt xuống → bánh răng góc trên bên phải trang tìm kiếm

- 🔴 Mô-đun hiển thị trang chủ → Từ gợi ý tìm kiếm
- 🔴 Mô-đun hiển thị trang chủ → Đề xuất ứng dụng → Đề xuất ứng dụng chưa cài; 🟢 Hiển thị ứng dụng thường dùng
- 🔴 Bảng xếp hạng tìm kiếm nóng:
  - Bản cũ: bấm vào trực tiếp là công tắc, đề xuất, Weibo, tin tức, toàn mạng, phim ảnh, âm nhạc, tiểu thuyết, Zhihu, tắt hết
  - Bản mới: bấm vào là "Bảng nóng của tôi", chia ba trang: tìm kiếm nóng → tin tức, toàn mạng; cuộc sống → nổi bật; chủ đề → Zhihu. Tắt hết rồi khối bảng tìm kiếm nóng trên trang tìm kiếm biến mất toàn bộ

## 8. Màn hình -1

**Đường dẫn**: Màn hình chính từ cạnh trái vuốt sang phải → Cài đặt

- 🔴 Thẻ đề xuất, hoạt động phổ biến
- 🔴 Cài đặt quyền riêng tư → Đề xuất cá nhân hóa
- 🟢 Ô tìm kiếm, trợ lý đi lại

## 9. Thời tiết, Lịch

**Đường dẫn**: Thời tiết / Lịch → Cài đặt → Chương trình trải nghiệm người dùng. Thời tiết 18.0.0.27-R từ phía dưới "Quản lý thành phố → Cài đặt khác → Cài đặt" vào; Lịch từ góc trên bên phải "Thêm → Cài đặt" vào.

- 🔴 Bên trong nội dung đề xuất, đề xuất cá nhân hóa, quảng bá nội dung
- Ngày 2026-10-25 đã xác minh và tắt "Quảng bá nội dung" của Thời tiết, Lịch trên Xiaomi 18 Pro Max (Thời tiết 18.0.0.27-R, Lịch 18.0.1.30). Cổng vào Redmi K60 nguồn từ [phản hồi cộng đồng](https://github.com/rddmwmddr/android-ad-cleaner/issues/1). Cảnh báo thời tiết, nhắc thời tiết bất thường giữ lại.

## 10. Thông báo tiếp thị

**Thông báo chức năng giữ lại**: phản hồi người dùng dòng 18 Pro thông báo "tìm vị trí chụp" từng bị tắt nhầm. Tìm vị trí chụp, đề xuất vị trí chụp, vị trí chụp đề xuất không thuộc thông báo tiếp thị, ngay cả khi tên hoặc ID chứa "đề xuất / recommend" cũng giữ lại. Mã nguồn mới nhất đã thêm bảo vệ, gói cài đặt 0.2.3 chưa bao gồm; tên gói / ID kênh thật chờ bổ sung, khôi phục khi tắt nhầm xem [giải thích chuyên biệt](../11-xung-dot-doc-man-hinh-va-bao-ve-thong-bao-chuc-nang.md).

**Đường dẫn**: Cài đặt → Thông báo & trung tâm điều khiển → Quản lý thông báo → chọn ứng dụng → bấm tên kênh

- 🔴 Cửa hàng ứng dụng "Thông báo hoạt động nền tảng", trình duyệt "Tin tức", Play "Ưu đãi", Edge "Tin tức nóng", "Tin tức đột phá" v.v.
- ⚠️ ID kênh Xiaomi dạng `mipush|包名|数字`, mang dấu gạch đứng.

## 11. Thành phần quảng cáo hệ thống msa (cần adb, cần bạn đồng ý)

`com.miui.systemAdSolution` phụ trách quảng cáo mở đầu và quảng cáo tích hợp trong ứng dụng hệ thống như Thời tiết, Lịch, cửa hàng.

Ứng dụng 0.2.1 và `run.py -s S suspend com.miui.systemAdSolution` sẽ tạm ngưng nó, và khi hệ thống cung cấp giao diện thử cấm nối mạng, đọc lại quy tắc gói và trạng thái tường lửa. Hệ thống cũ như Android 13 có thể không có các lệnh này, lúc này hiện rõ "hoàn tất một phần" và trả về thất bại: tạm ngưng giữ lại, quảng cáo vẫn có thể xuất hiện. 0.2.0 không có xử lý chặn mạng, xem [Nhật ký thay đổi](../../../CHANGELOG.md). Lệnh thủ công dưới đây chỉ áp dụng cho hệ thống mà `cmd connectivity help` liệt kê giao diện tương ứng:

```bash
adb -s S shell pm suspend --user 0 com.miui.systemAdSolution
adb -s S shell cmd connectivity set-package-networking-enabled false com.miui.systemAdSolution
adb -s S shell cmd connectivity set-chain3-enabled true
```

- ⚠️ Chỉ tạm ngưng không chặn được: ứng dụng hệ thống khởi động sẽ kéo nó lên, nên thêm chặn mạng.
- ⚠️ Quy tắc chặn mạng sau khi khởi động lại có thể mất hiệu lực, sau khi khởi động lại chạy lại hai dòng sau.
- Xiaomi 18 Pro Max kiểm chứng thực tế: cửa hàng, trình duyệt, chủ đề, thời tiết mở bình thường, nội dung tải bình thường; không đại diện mọi hệ thống Xiaomi cung cấp giao diện đó.

Khôi phục:

```bash
adb -s S shell pm unsuspend --user 0 com.miui.systemAdSolution
adb -s S shell cmd connectivity set-package-networking-enabled true com.miui.systemAdSolution
```

---

## Cái bẫy của Xiaomi

**Xiaomi 10 (umi, Android 13 / OS1.0.7.0)**: [Issue #21](https://github.com/rddmwmddr/android-ad-cleaner/issues/21) cung cấp đường dẫn bản cũ. Biểu tượng cài đặt phía trên trình duyệt có thể không có dấu `clickable`; kịch bản chỉ nhận diện ở thanh công cụ, không bấm "Của tôi" trong chính văn tin tức. Trang bảng nóng có thể đồng thời có công tắc "Đề xuất" và trang con tìm kiếm nóng / giải trí / chủ đề, trang con còn xoay ngang; 0.2.1 đã sửa kích thước đọc màn hình và duyệt, nhưng toàn đoạn vẫn chờ máy đó kiểm chứng lại. "Thẻ video thời tiết", "Quảng bá nội dung" trong "Chương trình trải nghiệm người dùng" của Thời tiết có thể tắt, cảnh báo thời tiết giữ lại; thỏa thuận lần đầu khởi động Thời tiết, Lịch do chủ máy quyết định, kịch bản không thay đồng ý.

| Hiện tượng | Cách đối phó |
|---|---|
| Kịch bản đọc được màn hình, bấm không được | Trong Tùy chọn nhà phát triển bật "Gỡ lỗi USB (cài đặt bảo mật)" |
| Tắt công tắc hiện "Xác nhận tắt" | Bấm xác định |
| Trình duyệt nuốt cú bấm | Dùng bấm ngắn 80 mili giây, công cụ đã xử lý |
| Mẫu máy có màn hình sau báo nhiều màn hình khi chụp | `screencap` thêm `-d <主屏 display id>` |

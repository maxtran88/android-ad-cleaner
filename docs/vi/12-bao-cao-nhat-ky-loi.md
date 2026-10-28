# 12 Báo cáo nhật ký lỗi

Khi ứng dụng desktop thực thi thất bại, có thể gửi nhật ký lỗi lần này cho người duy trì dự án, không cần tài khoản GitHub.

## Người dùng thấy gì

1. Trang hoàn tất xuất hiện "có bước chưa thành công", bấm "Báo cáo nhật ký lỗi"; trong cửa sổ "Phản hồi" cũng có nút này.
2. Cửa sổ hiện ra liệt kê **toàn bộ nội dung sẽ gửi**, hiển thị nguyên văn, sau khi xác nhận mới gửi. Không bấm "Xác nhận báo cáo", sẽ không gửi gì đi.
3. Sau khi thành công hiện mã báo cáo. Muốn xóa bản ghi này, gửi GitHub Issue kèm mã.

## Gửi gì

| Nội dung | Giải thích |
|---|---|
| Phiên bản ứng dụng, hệ thống máy tính | Ví dụ `0.2.5`, `Windows 11（AMD64）` |
| Hãng, mẫu máy, phiên bản hệ thống, phiên bản Android của điện thoại | Từ trang phát hiện |
| Kết quả từng bước | Tên bước, thành công / thất bại / bỏ qua, thời gian dùng |
| Cuối nhật ký | Tối đa 2 vạn chữ, cùng nguồn với "Sao chép chẩn đoán đầy đủ" |
| Mã cài đặt | Lần báo cáo đầu tiên tạo ngẫu nhiên, lưu tại `install-id` trong thư mục dữ liệu ứng dụng, chỉ dùng để giới hạn tần suất; không lấy bất kỳ định danh thiết bị hoặc máy tính nào |

Trước khi gửi thay thế ở phía ứng dụng, máy chủ nhận được thay thế lại một lần: số sê-ri điện thoại → `<序列号>`, thư mục người dùng máy tính → `<用户目录>`, email, số điện thoại 11 chữ số, địa chỉ IP → `<邮箱>` `<手机号>` `<IP>`.

Không gửi: danh sách ứng dụng, nội dung thông báo, thông tin tài khoản, ảnh chụp màn hình, tệp sao lưu.

## Máy chủ lưu thế nào

- Gửi tới máy chủ tự xây của người duy trì dự án, địa chỉ ghi trong ứng dụng (`supabase.ahuamiao.com`).
- Lưu **90 ngày**, hết hạn tự động xóa.
- IP không lưu văn bản gốc, chỉ lưu băm mã hóa không thể khôi phục, dùng để giới hạn tần suất báo cáo; mã cài đặt ngẫu nhiên cũng chỉ lưu băm.
- Kênh báo cáo dùng tài khoản riêng quyền thấp, chỉ ghi báo cáo mới, không thể đọc bất kỳ dữ liệu nào.

## Giới hạn tần suất

Ứng dụng mỗi giờ tối đa 3 lần; máy chủ khác giới hạn theo IP và mã cài đặt, trong 1 giờ báo cáo nội dung hoàn toàn giống nhau chỉ nhận một lần. Vượt quá thì nhắc "Báo cáo quá thường xuyên, vui lòng thử lại sau một giờ".

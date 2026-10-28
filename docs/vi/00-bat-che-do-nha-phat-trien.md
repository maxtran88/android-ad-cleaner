# 00 Bật Chế độ nhà phát triển và Gỡ lỗi USB

Trước khi dùng máy tính xử lý điện thoại (cách 1), trên điện thoại cần bật hai thứ:

| Thứ cần bật | Tác dụng |
|---|---|
| Chế độ nhà phát triển | Để trong Cài đặt xuất hiện trang "Tùy chọn nhà phát triển" |
| Gỡ lỗi USB | Cho phép máy tính đọc màn hình điện thoại, bấm nút, sửa cài đặt |

Chỉ dùng điện thoại làm thủ công theo danh sách (cách 2, cách 3) thì không cần trang này.

Các ảnh chụp màn hình dưới đây từ OPPO (ColorOS 16), tên cổng vào của các hãng khác xem bảng dưới mỗi bước.

---

## Bước 1: Tìm "Phiên bản"

<p align="center"><img src="../../images/dev-1-about.png" width="420" alt="Thông tin phiên bản trong Giới thiệu về điện thoại"></p>

| Hãng | Đường dẫn |
|---|---|
| OPPO / OnePlus / realme | Cài đặt → Giới thiệu về điện thoại → Thông tin phiên bản |
| Xiaomi / Redmi | Cài đặt → Thiết bị của tôi → Tất cả thông số |
| vivo / iQOO | Cài đặt → Quản lý hệ thống & nâng cấp → Thông tin phiên bản |
| Honor | Cài đặt → Giới thiệu về điện thoại |
| Huawei | Cài đặt → Giới thiệu về điện thoại |

## Bước 2: Bấm liên tiếp 7 lần

<p align="center"><img src="../../images/dev-2-version.png" width="420" alt="Bấm liên tiếp số phiên bản"></p>

| Hãng | Bấm liên tiếp mục nào |
|---|---|
| OPPO / OnePlus / realme | Số phiên bản |
| Xiaomi / Redmi | Phiên bản hệ điều hành |
| vivo / iQOO | Số phiên bản phần mềm |
| Honor / Huawei | Số phiên bản |

1. Bấm liên tiếp 7 lần, phía dưới màn hình sẽ hiện đếm ngược: "Bấm thêm 3 lần", "Bấm thêm 2 lần" …
2. Hiện hộp mật khẩu khóa màn hình, nhập mật khẩu khóa màn hình của bạn.
3. Hiện "Bạn đã ở Chế độ nhà phát triển", bước này hoàn tất.

## Bước 3: Mở Tùy chọn nhà phát triển

<p align="center"><img src="../../images/dev-3-search.png" width="320" alt="Tìm Tùy chọn nhà phát triển trong Cài đặt"></p>

Cách nhanh nhất: mở Cài đặt, nhập "Tùy chọn nhà phát triển" vào ô tìm kiếm phía trên, bấm kết quả tìm kiếm.

Cũng có thể tìm theo đường dẫn:

| Hãng | Đường dẫn |
|---|---|
| OPPO / OnePlus / realme | Cài đặt → Hệ thống & cập nhật → Tùy chọn nhà phát triển |
| Xiaomi / Redmi | Cài đặt → Cài đặt khác → Tùy chọn nhà phát triển |
| vivo / iQOO | Cài đặt → Quản lý hệ thống & nâng cấp → Tùy chọn nhà phát triển |
| Honor / Huawei | Cài đặt → Hệ thống & cập nhật → Tùy chọn nhà phát triển |

## Bước 4: Xác nhận công tắc tổng đang bật

<p align="center"><img src="../../images/dev-4-on.png" width="420" alt="Công tắc tổng Tùy chọn nhà phát triển"></p>

Công tắc "Tùy chọn nhà phát triển" ở trên cùng trang phải có màu xanh (bật). Nếu đang tắt thì bấm mở.

## Bước 5: Bật Gỡ lỗi USB

<p align="center"><img src="../../images/dev-5-usb.png" width="420" alt="Gỡ lỗi USB và gỡ lỗi không dây"></p>

1. Kéo xuống mục "Gỡ lỗi".
2. Bật "Gỡ lỗi USB", hộp thoại hiện ra bấm "Đồng ý".
3. Không muốn cắm dây, bật "Gỡ lỗi không dây" phía dưới, cách ghép nối xem [01-chuan-bi](01-chuan-bi.md).

**Xiaomi / Redmi thêm một bước**: cùng trang bật "Gỡ lỗi USB (cài đặt bảo mật)". Mục này cần cắm SIM, đăng nhập tài khoản Xiaomi. Không bật nó, máy tính đọc được màn hình nhưng không bấm được nút.

## Bước 6: Cắm dây, bấm Cho phép

1. Dùng dây dữ liệu nối máy tính. Dây chỉ sạc được thì không được, đổi dây truyền được tệp.
2. Kéo thanh thông báo trên điện thoại xuống, bấm thông báo USB, chọn "Truyền tệp".
3. Điện thoại hiện "Cho phép gỡ lỗi USB?", tích "Luôn cho phép gỡ lỗi từ máy tính này", bấm "Cho phép".

Không thấy hộp thoại: rút dây cắm lại một lần; vẫn chưa có, trong Tùy chọn nhà phát triển bấm "Thu hồi ủy quyền gỡ lỗi USB", cắm lại một lần nữa.

---

## Dùng xong có cần tắt không?

Nên tắt. `run.py finish` khi kết thúc sẽ nhắc bạn.

| Lý do | Giải thích |
|---|---|
| Ứng dụng phát hiện | Một số ứng dụng ngân hàng, thanh toán, trò chơi phát hiện gỡ lỗi USB đang bật sẽ nhắc hoặc từ chối chạy |
| Bảo mật | Tắt rồi, người khác cầm điện thoại của bạn cắm vào máy tính cũng không kết nối được |

Hai cách tắt:

1. Trên điện thoại: Cài đặt → tìm "Tùy chọn nhà phát triển" → tắt công tắc tổng ở trên cùng trang.
2. Trên máy tính: `python3 tool/run.py -s <序列号> dev-off --yes`. Sau khi thực hiện máy tính và điện thoại ngắt kết nối, điều này là bình thường. Không thêm `--yes` sẽ từ chối thực hiện.

`dev-off` kiểm chứng thực tế (OPPO Find N3 bản sưu tập, ColorOS 16.0.5, 2026-10-24):

| Mục | Trước khi thực hiện | Sau khi thực hiện |
|---|---|---|
| Chế độ nhà phát triển | Bật | Tắt (đối chiếu trên điện thoại) |
| Gỡ lỗi USB | Bật | Tắt, máy tính ngắt ngay lập tức |
| Gỡ lỗi không dây | Bật | Tắt |

Tắt Chế độ nhà phát triển **không hủy** những thay đổi lần này: công tắc đã tắt, gói đã tạm ngưng, thông báo đã tắt đều giữ nguyên. Sau này muốn khôi phục, bật lại Chế độ nhà phát triển và Gỡ lỗi USB. Một số hãng sau khi tắt cần bấm lại 7 lần số phiên bản, làm lại từ bước 1.

## Vấn đề thường gặp

| Hiện tượng | Cách xử lý |
|---|---|
| Bấm 7 lần không phản ứng | Bấm sai vị trí, đối chiếu bảng bước 2 đổi mục khác bấm |
| Hiện "Bạn đã ở Chế độ nhà phát triển" | Trước đây đã bật, nhảy tới bước 3 |
| Trong Tùy chọn nhà phát triển không có "Gỡ lỗi USB" | Kéo tới mục "Gỡ lỗi", ở giữa dưới trang |
| Trên máy tính hiện `unauthorized` | Chưa bấm "Cho phép" trên điện thoại, xem bước 6 |
| Trên máy tính không có gì | Đổi dây dữ liệu; mục đích USB đổi thành "Truyền tệp" |

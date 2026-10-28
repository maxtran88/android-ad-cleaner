# 03 Dùng AI trò chuyện hướng dẫn bạn bấm

Phù hợp: chỉ có điện thoại, không có máy tính.
Nguyên lý: AI trò chuyện không thao tác được điện thoại của bạn, nó đọc danh sách, từng bước một cho bạn biết bấm vào đâu; bạn bấm xong trả lời nó, hoặc gửi ảnh chụp màn hình cho nó xem.

## Ba bước bắt đầu

1. Mở bất kỳ một trong DeepSeek, Doubao, ChatGPT. DeepSeek cần bật "Tìm kiếm trên web", Doubao và ChatGPT mặc định đọc được liên kết.
2. Sao chép toàn bộ đoạn văn trong khung tại [prompts/聊天AI提示词.md](../../prompts/聊天AI提示词.md), gửi cho AI.
3. Trả lời câu hỏi của AI: hãng, mẫu máy, phiên bản hệ thống.

Mẫu máy và phiên bản hệ thống xem tại đây:

| Hãng | Đường dẫn |
|---|---|
| OPPO / OnePlus / realme | Cài đặt → Giới thiệu về điện thoại |
| Xiaomi / Redmi | Cài đặt → Thiết bị của tôi |
| vivo / iQOO | Cài đặt → Quản lý hệ thống & nâng cấp → Thông tin phiên bản |
| Honor / Huawei | Cài đặt → Giới thiệu về điện thoại |

## Cuộc trò chuyện trông như thế này

```text
AI: Điện thoại của bạn hãng nào, mẫu máy nào? Phiên bản hệ thống là bao nhiêu?
Bạn: OPPO Find N6, ColorOS 16
AI: Bước 1: Mở "Cài đặt" → "Quyền riêng tư" → "Định danh thiết bị & quảng cáo" → "Theo dõi quảng cáo".
    Trang này mỗi ứng dụng có một công tắc, tắt hết. Tắt xong trả lời "Xong".
Bạn: Xong
AI: Bước 2: Từ cạnh trái màn hình chính vuốt sang phải, mở màn hình -1…
```

## Khi AI đọc không được liên kết

1. Mở [docs/checklists/](checklists/), tìm hãng của bạn.
2. Mở tệp danh sách, chọn tất cả và sao chép.
3. Dán cho AI, nói "Làm theo danh sách này hướng dẫn tôi làm".

## So với cách 1

| | Cách 1: Tác nhân AI | Cách 2: AI trò chuyện |
|---|---|---|
| Cần máy tính | Cần | Không cần |
| Ai bấm màn hình | Kịch bản | Bạn |
| Thời gian dùng | 4 đến 6 phút (có kịch bản theo mẫu máy) | 30 đến 60 phút |
| Có tạm ngưng được gói quảng cáo không | Được | Không được (cần adb) |
| Có tắt hàng loạt thông báo tiếp thị không | Được | Không được, tắt từng cái một |

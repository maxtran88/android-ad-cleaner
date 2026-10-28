# 02 Dùng tác nhân AI chạy thay bạn

Phù hợp: có máy tính, muốn giao toàn bộ việc cho AI.
Điều kiện: điện thoại bật Chế độ nhà phát triển và Gỡ lỗi USB ([hướng dẫn có ảnh chụp màn hình](00-bat-che-do-nha-phat-trien.md)), dùng dây dữ liệu nối máy tính. adb và Python chưa cài cũng không sao, AI sẽ giúp bạn cài.

## Những công cụ nào dùng được

Phải chọn công cụ AI **có thể thực thi lệnh trên máy tính của bạn**. Cửa sổ trò chuyện trên web không thực thi được lệnh, trường hợp đó xem [03-dung-ai-tro-chuyen](03-dung-ai-tro-chuyen.md).

| Công cụ | Nhà sản xuất | Có thực thi lệnh không | Ghi chú |
|---|---|---|---|
| WorkBuddy | Tencent | ✅ | Bản desktop, để nó thao tác trong thư mục làm việc cục bộ |
| Claude Code | Anthropic | ✅ | Chạy trong terminal, sẽ đọc `CLAUDE.md` |
| Codex | OpenAI | ✅ | Bản terminal hoặc desktop, sẽ đọc `AGENTS.md` |
| Trae | ByteDance | ✅ | Dùng chế độ Builder / SOLO |
| Cursor | Anysphere | ✅ | Dùng chế độ Agent |
| DeepSeek / Doubao / ChatGPT bản web | — | ❌ | Dùng [03-dung-ai-tro-chuyen](03-dung-ai-tro-chuyen.md) |

## Cách mở đầu

Gửi đoạn này cho AI:

```text
Hãy clone https://github.com/rddmwmddr/android-ad-cleaner , đọc AGENTS.md trong kho,
rồi giúp tôi gỡ quảng cáo cho chiếc điện thoại đang kết nối với máy tính này. Trước mỗi bước thay đổi, hãy cho tôi biết bạn sắp thay đổi gì.
```

AI sẽ lần lượt làm những việc này:

1. Clone kho, đọc `AGENTS.md`.
2. Kiểm tra adb và Python, thiếu gì cài nấy.
3. Chạy `run.py devices`, cho bạn biết đã nhận ra điện thoại nào, có kịch bản theo mẫu máy sẵn không.
4. Lưu một bản sao trạng thái trước khi thay đổi.
5. Chạy kịch bản theo mẫu máy, hoặc làm theo danh sách từng trang một để tắt.
6. Liệt kê kênh thông báo tiếp thị, cho bạn xem danh sách, bạn gật đầu rồi mới tắt.
7. Phát hiện Quick App, hỏi bạn có muốn tạm ngưng gói quảng cáo, tắt Quick App không.
8. Kết thúc, báo cáo đã tắt gì, chưa tắt gì.
9. Nhắc bạn tắt Chế độ nhà phát triển. Bạn nói "giúp tôi tắt", AI sẽ tắt từ máy tính, kết nối theo đó ngắt.

## Những việc AI sẽ hỏi bạn

| AI hỏi | Bạn trả lời thế nào |
|---|---|
| Điện thoại khóa màn hình rồi, vui lòng mở khóa | Mở khóa điện thoại, giữ màn hình sáng |
| Nhận ra nhiều thiết bị, xử lý thiết bị nào | Nói mẫu máy hoặc số sê-ri |
| Những kênh thông báo tiếp thị này có tắt không | Xem danh sách, có mục muốn giữ thì nói ra |
| Có tạm ngưng mấy gói quảng cáo này không | Bạn quyết định. Tạm ngưng có thể khôi phục |
| Trang chủ trình duyệt có đổi sang bản đơn giản không | Bạn quyết định |

## Trong lúc chạy

- Điện thoại giữ sáng màn hình, mở khóa, cắm dây.
- Đừng chạm vào điện thoại. Kịch bản đang bấm màn hình, bạn chạm vào là loạn.
- Mẫu máy có kịch bản theo mẫu máy, toàn bộ 4 đến 6 phút. Mẫu máy không có kịch bản, AI phải tìm từng trang một, lâu hơn.

## Sau khi chạy xong

1. Mở tìm kiếm kéo xuống, màn hình -1, cửa hàng ứng dụng, trình duyệt, xác nhận chức năng bình thường.
2. Bảo AI lưu đường dẫn lần này thành kịch bản theo mẫu máy, lần sau cùng mẫu máy vài phút chạy xong.
3. Sẵn lòng chia sẻ thì gửi kịch bản theo mẫu máy thành PR, xem [04-viet-kich-ban-cho-mau-may-moi](04-viet-kich-ban-cho-mau-may-moi.md).

## Các lệnh bổ sung thường dùng

```text
Chỉ chạy hai đoạn Trình duyệt và Chủ đề.
Lưu đường dẫn của điện thoại này thành kịch bản theo mẫu máy.
Khôi phục toàn bộ gói đã tạm ngưng.
Liệt kê thông báo tiếp thị hiện vẫn đang bật trên điện thoại này.
```

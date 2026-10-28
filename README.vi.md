# Gỡ quảng cáo trên điện thoại

Tắt quảng cáo hệ thống, từ khóa thịnh hành, đề xuất tin tức và thông báo tiếp thị trên điện thoại Android Trung Quốc.

Trang giới thiệu: **https://rddmwmddr.github.io/android-ad-cleaner/**

> Ngôn ngữ: [English](README.en.md) | [Tiếng Việt](README.vi.md) | [中文](README.md)

## Tải ứng dụng desktop

Cắm điện thoại vào, bấm vài nút. Không cần Python, cũng không cần công cụ AI.

> **v0.2.5 · 2026-10-27**: Thêm tính năng báo cáo nhật ký lỗi. Khi thực thi thất bại, bạn có thể gửi nhật ký cho người duy trì mà không cần tài khoản GitHub; toàn bộ nội dung được hiển thị nguyên văn trước khi gửi, và chỉ gửi sau khi bạn xác nhận. Số sê-ri, thư mục người dùng, email, số điện thoại, IP được thay thế một lần ở phía máy khách và một lần ở phía máy chủ, máy chủ lưu trữ 90 ngày. Mọi bản sửa của 0.2.4 đều được giữ lại. Bản cũ không tự động cập nhật, vui lòng tải lại; các bản sao lưu hiện có vẫn được giữ. Xem [Nhật ký thay đổi](CHANGELOG.md) và [Báo cáo nhật ký lỗi](docs/vi/12-bao-cao-nhat-ky-loi.md). Trang web chính thức: https://ahuamiao.com/sites/other/android-ad-removal-intro.html

Các phiên bản trước đã xử lý tình trạng hết thời gian chờ của trang cục bộ trên Windows, lỗi chụp màn hình vượt giới hạn trên Honor, rủi ro thao tác nhầm kênh thông báo, và vấn đề Quick App và sao lưu trên vivo. Phạm vi xử lý và các mục chờ xác minh của từng Issue xem tại [Xử lý vấn đề cộng đồng](docs/vi/09-xu-ly-van-de-cong-dong.md). Chỉ hỗ trợ thiết bị Android kết nối qua adb, tạm thời chưa hỗ trợ HarmonyOS gốc dùng HDC.

| Máy tính | Tải về | Ghi chú |
|---|---|---|
| Mac · chip Apple (M1 trở lên) | [AndroidAdCleaner-0.2.5-mac-arm64.dmg](https://github.com/rddmwmddr/android-ad-cleaner/releases/download/v0.2.5/AndroidAdCleaner-0.2.5-mac-arm64.dmg) | Đã ký, đã qua kiểm chứng của Apple, nhấp đúp là mở được |
| Mac · chip Intel (macOS 11 trở lên) | [AndroidAdCleaner-0.2.5-mac-intel.dmg](https://github.com/rddmwmddr/android-ad-cleaner/releases/download/v0.2.5/AndroidAdCleaner-0.2.5-mac-intel.dmg) | Như trên |
| Windows 10 / 11 · bản cài đặt | [AndroidAdCleaner-0.2.5-windows-setup.exe](https://github.com/rddmwmddr/android-ad-cleaner/releases/download/v0.2.5/AndroidAdCleaner-0.2.5-windows-setup.exe) | Khi hiện "Windows đã bảo vệ máy tính của bạn", bấm "Thêm thông tin" → "Vẫn chạy" |
| Windows 10 / 11 · bản portable | [AndroidAdCleaner-0.2.5-windows-portable.zip](https://github.com/rddmwmddr/android-ad-cleaner/releases/download/v0.2.5/AndroidAdCleaner-0.2.5-windows-portable.zip) | Sau khi giải nén, nhấp đúp `AndroidAdCleaner.exe` |

Không biết Mac dùng chip nào: biểu tượng Apple ở góc trên bên trái → Giới thiệu về máy Mac này, mục "Chip" ghi bắt đầu bằng Apple M thì chọn chip Apple. Mọi phiên bản: [Releases](https://github.com/rddmwmddr/android-ad-cleaner/releases). Cách dùng: [docs/vi/08-ung-dung-desktop.md](docs/vi/08-ung-dung-desktop.md).

| | |
|---|---|
| <img src="images/gui-1-connect.png" alt="Kết nối điện thoại"><br>**1 Kết nối điện thoại**: cắm dây là nhận ra điện thoại, có hướng dẫn bằng hình ảnh để bật gỡ lỗi USB | <img src="images/gui-3-detect.png" alt="Phát hiện"><br>**2 Phát hiện**: mẫu máy, phiên bản hệ thống, kịch bản theo mẫu máy, Quick App, thành phần quảng cáo |
| <img src="images/gui-4-choose.png" alt="Lựa chọn"><br>**3 Chọn mục cần tắt**: thông báo tiếp thị được tích chọn theo từng kênh, các mục thuộc loại dịch vụ mặc định không được tích | <img src="images/gui-6-run.png" alt="Thực thi"><br>**4 Thực thi**: thanh tiến trình và nhật ký trực tiếp |
| <img src="images/gui-7-done.png" alt="Hoàn tất"><br>**5 Hoàn tất**: kết quả từng bước, cuối cùng nhắc tắt Chế độ nhà phát triển | <img src="images/gui-8-feedback.png" alt="Phản hồi"><br>**Phản hồi**: tự động đính kèm thông tin chẩn đoán, gửi GitHub Issue bằng một cú nhấp |

---

- Không root, không mở khóa bootloader, không flash ROM, cập nhật hệ thống không bị ảnh hưởng.
- Chỉ dùng các công tắc có sẵn trong hệ thống và ứng dụng. Bước tạm ngưng gói quảng cáo cần chủ máy đồng ý, một lệnh là khôi phục được.
- Tìm kiếm, thẻ màn hình -1, cài đặt và cập nhật từ cửa hàng ứng dụng, cảnh báo thời tiết, nhắc giao hàng đều được giữ lại.

<p align="center"><img src="images/store-before.png" width="560" alt="Trước khi sửa: trang chủ cửa hàng phần mềm đầy đề xuất"></p>
<p align="center">Trước khi sửa: trang chủ Cửa hàng phần mềm OPPO. Ảnh quay vòng, mục bắt buộc, mục nên chơi, thẻ ưu đãi — toàn là vị trí quảng cáo.</p>

---

## Xử lý những gì

| Hạng mục | Ví dụ | Cách xử lý |
|---|---|---|
| Quảng cáo hệ thống | Quảng cáo cá nhân hóa, theo dõi quảng cáo (OAID), dịch vụ đề xuất thông minh | Công tắc trong cài đặt hệ thống |
| Từ khóa thịnh hành và tin tức | Bảng xếp hạng nóng trong tìm kiếm kéo xuống, tin tức màn hình -1, luồng tin tức trình duyệt | Công tắc trong cài đặt từng ứng dụng, trình duyệt chuyển sang trang chủ đơn giản |
| Vị trí quảng cáo | Ảnh quay vòng, màn hình mở đầu, hoạt động nổi, ưu đãi điểm danh trong cửa hàng | Công tắc trong "Quản lý dịch vụ" của cửa hàng |
| Thông báo tiếp thị | Thông báo "Nội dung & tiếp thị", "Ưu đãi sự kiện" của từng ứng dụng | Tắt theo từng kênh, giữ lại thông báo đơn hàng, giao hàng, cập nhật của cùng ứng dụng đó |
| Thành phần quảng cáo | `com.opos.ads`, `com.miui.systemAdSolution`, v.v. | `pm suspend` để tạm ngưng, cần chủ máy đồng ý |
| Quick App | "Tiểu chương trình không cần cài đặt" mà quảng cáo bấm vào là nhảy tới | `quickapp` để phát hiện, `quickapp off` để tắt, xem [docs/vi/07-quick-app.md](docs/vi/07-quick-app.md) |

## Những việc không làm

- Không gỡ cài đặt, không vô hiệu hóa ứng dụng hệ thống (không dùng `pm uninstall`, cũng không dùng `pm disable-user`).
- Không sửa phân vùng system, không cài module.
- Không thay bạn đồng ý bất kỳ thỏa thuận người dùng nào của ứng dụng. Gặp trang thỏa thuận, bấm "Hủy" hoặc "Để sau".
- Không chụp màn hình trang tài khoản và trang số điện thoại.

---

## Bốn cách sử dụng

<p align="center"><img src="images/ways.png" width="460" alt="Ba cách sử dụng"></p>

> Cách 1 cần bật Chế độ nhà phát triển và gỡ lỗi USB trên điện thoại trước, hướng dẫn có ảnh chụp màn hình tại: [docs/vi/00-bat-che-do-nha-phat-trien.md](docs/vi/00-bat-che-do-nha-phat-trien.md).

| Cách dùng | Phù hợp với ai | Cần chuẩn bị gì | Tài liệu |
|---|---|---|---|
| **1: Tác nhân AI chạy thay bạn** | Có máy tính, muốn đỡ vất vả | Máy tính, dây dữ liệu, một công cụ AI có thể thực thi lệnh | [docs/vi/02-dung-tac-nhan-ai.md](docs/vi/02-dung-tac-nhan-ai.md) |
| **2: AI trò chuyện hướng dẫn bạn bấm** | Chỉ có điện thoại | Bất kỳ một trong DeepSeek, Doubao, ChatGPT | [docs/vi/03-dung-ai-tro-chuyen.md](docs/vi/03-dung-ai-tro-chuyen.md) |
| **3: Làm thủ công theo danh sách** | Muốn tự nắm từng bước | Chỉ cần điện thoại | [docs/vi/checklists/](docs/vi/checklists/) |
| **4: Ứng dụng desktop** | Không muốn gõ lệnh | Mac (chip Apple / Intel) hoặc Windows 10/11, dây dữ liệu | [Tải về](#tai-ung-dung-desktop) · [Hướng dẫn](docs/vi/08-ung-dung-desktop.md) |

Câu mở đầu cho cách 1, sao chép gửi cho AI:

```text
Hãy clone https://github.com/rddmwmddr/android-ad-cleaner , đọc AGENTS.md trong kho,
rồi giúp tôi gỡ quảng cáo cho chiếc điện thoại đang kết nối với máy tính này. Trước mỗi bước thay đổi, hãy cho tôi biết bạn sắp thay đổi gì.
```

---

## Các mẫu máy đã kiểm chứng thực tế

**Kịch bản theo mẫu máy**: các bước thao tác tự động của một mẫu máy, ghi rõ "mở ứng dụng nào, bấm những chữ nào để vào trang cài đặt, tắt những công tắc nào, giữ lại những công tắc nào". Máy tính làm theo đó và bấm trên điện thoại, vài phút là xong. Trang cài đặt khác nhau theo mẫu máy và phiên bản hệ thống, nên mỗi mẫu máy có một kịch bản riêng.

| Hãng | Mẫu máy (mã máy) | Hệ thống | Kịch bản theo mẫu máy | Danh sách thủ công | Thông báo tiếp thị |
|---|---|---|---|---|---|
| Honor | PNM-AN10 | MagicOS 10 | ✅ Đã kiểm chứng thực tế, chạy lại trong 4 phút | ✅ | ✅ 26 kênh |
| OnePlus | Ace 2 Pro (PJA110) | ColorOS 14.0.0.812 / Android 14 | Mới thêm trong mã nguồn: 3 mục cá nhân hóa + 6 vị trí quảng cáo trong cửa hàng đã tắt và đọc lại | Một phần, xem bản ghi kiểm chứng | ✅ 23 kênh tổng cộng, công tắc tổng không đổi; khác biệt về nhắc thời tiết xem bản ghi kiểm chứng |
| OPPO | Find N6 (PLP120) | ColorOS 16.0.9 | ⚠️ Đường dẫn đã kiểm chứng thực tế, toàn bộ quy trình chờ xác minh | ✅ | ✅ 30 kênh |
| OPPO | Find X10 Pro Max (PMX110) | ColorOS 17 | — | ✅ | ✅ |
| OPPO | Find X9 Ultra (PMA120) | ColorOS 16.0.10 | ❌ Trang khác với N6, chờ bổ sung | Một phần | ✅ 27 kênh |
| OPPO | Find N3 bản sưu tập (PHN110) | ColorOS 16.0.5 | ❌ Chờ bổ sung | Một phần | ✅ 27 kênh |
| Xiaomi | 18 Pro Max (M154FF) | HyperOS 4.0.24 | ✅ Trước 10-25 chín đoạn đầu đã qua, thay đổi tương thích mới thêm chờ kiểm chứng lại | ✅ | ✅ |
| vivo | X300 Ultra (V2547DA) | OriginOS 6 | ⚠️ Kịch bản đã bổ sung, toàn bộ quy trình chờ xác minh trên máy thật | ✅ | ✅ |

Bảng phản ánh kịch bản và phạm vi xác minh hiện tại. Xiaomi 10, Honor Magic7 Pro và các phản hồi khác đã sửa những lỗi chung có thể xác định, nhưng vẫn cần kiểm chứng lại trên máy thật tương ứng; kịch bản tham khảo cùng hãng không tương đương với bản tùy chỉnh riêng, xem chi tiết tại [Nhật ký thay đổi](CHANGELOG.md).

- Có thể chạy phát hiện chung trước; kênh thông báo có tắt an toàn được hay không phụ thuộc vào trang hệ thống và quyền, một số trang vivo sẽ bị bỏ qua. Cổng vào theo dõi quảng cáo cũng thay đổi theo hãng.
- Cùng một hãng, phiên bản nhỏ của hệ thống khác nhau thì tên và cấp bậc của trang cài đặt cũng thay đổi. Kịch bản theo mẫu máy được lưu theo mã máy và phiên bản hệ thống, khi phiên bản không khớp, công cụ sẽ cảnh báo, các bước không tìm thấy cổng vào sẽ bị bỏ qua, không bấm lung tung.
- Mẫu máy của bạn không có trong bảng: làm theo [docs/vi/04-viet-kich-ban-cho-mau-may-moi.md](docs/vi/04-viet-kich-ban-cho-mau-may-moi.md) để làm một bản, hoan nghênh gửi PR.

---

## Một quy trình đầy đủ

<p align="center"><img src="images/flow.png" width="340" alt="Quy trình xử lý"></p>

Cách viết lệnh:

```bash
pip3 install -r requirements.txt
python3 tool/run.py devices                 # Xem số sê-ri, mẫu máy, có kịch bản theo mẫu máy hay không
python3 tool/run.py -s <序列号> check        # Chỉ kiểm tra, không sửa
python3 tool/run.py -s <序列号> backup       # Ảnh chụp nhanh trước khi thay đổi
python3 tool/run.py -s <序列号> recipe       # Chạy kịch bản theo mẫu máy
python3 tool/run.py -s <序列号> chan-scan    # Liệt kê kênh thông báo tiếp thị
python3 tool/run.py -s <序列号> chan-off backups/<型号>-<时间>/channels.tsv
python3 tool/run.py -s <序列号> quickapp     # Phát hiện Quick App; quickapp off để tắt
python3 tool/run.py -s <序列号> finish       # Kết thúc, nhắc tắt Chế độ nhà phát triển
python3 tool/run.py -s <序列号> dev-off --yes  # Tắt Chế độ nhà phát triển từ máy tính (bước cuối, sau khi thực hiện sẽ ngắt kết nối)
```

<p align="center"><img src="images/channel-off.png" width="420" alt="Diện mạo kênh thông báo tiếp thị sau khi tắt"></p>
<p align="center">Thông báo tiếp thị tắt theo từng kênh: "Nội dung & tiếp thị" của Thời tiết tắt đi, cảnh báo thời tiết vẫn giữ.</p>

---

## Cấu trúc kho

```text
AGENTS.md            Quy tắc thao tác dành cho tác nhân AI đọc
CHANGELOG.md         Cập nhật mã nguồn, kết quả xác minh và trạng thái phát hành gói cài đặt
docs/
  00-打开开发者模式.md Hướng dẫn từng bước có ảnh chụp màn hình
  01-准备工作.md      Cài adb, kết nối máy tính, gỡ lỗi không dây
  02-用AI智能体.md    WorkBuddy, Claude Code, Codex, Trae, Cursor
  03-用聊天AI.md      DeepSeek, Doubao, ChatGPT
  04-给新机型写脚本.md
  05-还原.md
  06-常见问题.md
  07-快应用.md        Quick App là gì, cách phát hiện và tắt
  08-桌面客户端.md     Cách dùng, vị trí dữ liệu, đóng gói ứng dụng Mac / Windows
  09-社区问题处理.md   Phạm vi xử lý Issue / PR và các mục chờ xác minh
  清单/               Danh sách thủ công theo từng hãng
prompts/             Lời nhắc sao chép gửi cho AI trò chuyện
tool/
  run.py             Cổng vào chính
  fast.py            Công cụ đọc màn hình, tìm cổng vào, bật/tắt công tắc (uiautomator2)
  chan_fast.py       Kênh thông báo tiếp thị
  explore.py         Dò đường cho mẫu máy mới (thử nghiệm)
gui/                 Ứng dụng desktop (giao diện pywebview + đóng gói PyInstaller)
recipes/<品牌>-<型号>/recipe.py   Kịch bản theo mẫu máy của từng mẫu
images/              Hình minh họa tài liệu
tests/               Kiểm thử hồi quy của công cụ, không kết nối điện thoại
```

## Phản hồi

Gặp vấn đề, muốn tính năng mới, muốn hỗ trợ điện thoại của bạn, hãy gửi tại [Issues](https://github.com/rddmwmddr/android-ad-cleaner/issues/new/choose), chọn mẫu tương ứng.

Nếu dùng ứng dụng desktop, bấm "Phản hồi" ở góc dưới bên trái: tự động đính kèm phiên bản ứng dụng, mẫu máy, phiên bản hệ thống và nhật ký gần đây (số sê-ri đã được thay thế, không có danh sách ứng dụng và nội dung thông báo), mở trang GitHub rồi bấm gửi là xong. Gửi cần tài khoản GitHub.

## Khôi phục

Xem [docs/vi/05-khoi-phuc.md](docs/vi/05-khoi-phuc.md). Gói bị tạm ngưng và kênh thông báo mỗi thứ một lệnh; công tắc trong ứng dụng bật lại thủ công theo đường dẫn trong danh sách.

## Tuyên bố

Dự án này chỉ gọi các mục cài đặt mà Android và ứng dụng của hãng công khai cung cấp. Giao diện của từng hãng thay đổi theo cập nhật hệ thống, vui lòng sao lưu trước khi dùng, kết quả lấy điện thoại của bạn làm chuẩn. Mọi vấn đề phát sinh do sử dụng dự án này do người dùng tự chịu trách nhiệm.

Giấy phép: MIT

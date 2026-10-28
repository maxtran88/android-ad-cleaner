# 08 Ứng dụng desktop (Mac / Windows)

Không muốn gõ lệnh, không muốn dùng công cụ AI, dùng ứng dụng desktop: cắm điện thoại vào, bấm vài nút.
Ứng dụng gọi cùng một bộ công cụ (`tool/`), dòng lệnh làm được gì nó cũng làm được.

> **Ghi chú phiên bản (2026-10-27)**: phiên bản hiện tại là **0.2.5**, thêm báo cáo nhật ký lỗi gửi sau khi người dùng xác nhận, giữ lại khả năng tương thích trang thông báo tiếp thị, phát hiện cài đặt bảo mật Xiaomi, dừng khi ngắt kết nối và nhắc kết nối, lỗi mã chẩn đoán và bản sửa phiên bản hệ thống tối thiểu của Mac Intel của 0.2.4. Bản cũ không tự động cập nhật, vui lòng tải lại; dữ liệu gốc và thư mục sao lưu tiếp tục giữ. Phạm vi kiểm thử và giới hạn tương thích xem [Nhật ký thay đổi](../../CHANGELOG.md).

| Nền tảng | Gói cài đặt | Trạng thái |
|---|---|---|
| macOS (chip Apple) | `AndroidAdCleaner-<版本>-mac-arm64.dmg` | Đã ký, đã kiểm chứng; giao diện gốc, hình ảnh, JS API và dòng lệnh tích hợp đã xác minh qua |
| macOS (chip Intel) | `AndroidAdCleaner-<版本>-mac-intel.dmg` | Đã ký, đã kiểm chứng; đã thử dưới Rosetta trên Mac chip Apple, máy thật Intel chờ thử |
| Windows 10 / 11 (64-bit) | `AndroidAdCleaner-<版本>-windows-setup.exe` (bản cài đặt)<br>`AndroidAdCleaner-<版本>-windows-portable.zip` (bản portable) | Đóng gói trên đám mây GitHub Actions, kiểm thử nhanh qua (dòng lệnh, đầu ra tiếng Trung, GUI gốc, hình ảnh và JS API); kết nối điện thoại và máy tính của người báo cáo chờ thử |

## Tải và cài đặt

Tại [trang Releases](https://github.com/rddmwmddr/android-ad-cleaner/releases/latest) tải gói cài đặt tương ứng.

Không biết Mac của mình là chip nào: bấm biểu tượng Apple ở góc trên bên trái màn hình → Giới thiệu về máy Mac này, mục "Chip" ghi bắt đầu bằng Apple M là chip Apple, ghi Intel là chip Intel.

**Mac**

1. Nhấp đúp dmg, kéo "安卓去广告" sang thư mục "Ứng dụng" bên cạnh.
2. Mở "安卓去广告". Gói cài đặt đã qua kiểm chứng của Apple, nhấp đúp là mở được.

**Windows**

1. Nhấp đúp `…-windows-setup.exe` để cài đặt. Không muốn cài đặt, tải `…-windows-portable.zip`, giải nén rồi nhấp đúp `AndroidAdCleaner.exe`.
2. Chương trình cài đặt không có chữ ký mã, Windows sẽ hiện màu xanh "Windows đã bảo vệ máy tính của bạn": bấm "Thêm thông tin" → "Vẫn chạy".
3. Sau khi mở nhắc thiếu WebView2: bấm "Đồng ý" tới trang web chính thức của Microsoft, tải cài đặt "Evergreen Bootstrapper", rồi mở lại chương trình này. Windows 11 có sẵn, một phần Windows 10 cần cài.
4. Cắm điện thoại rồi ứng dụng không nhận ra: máy tính này thiếu trình điều khiển USB của điện thoại, xem "Trình điều khiển Windows" phía dưới.

Không cần cài Python, cũng không cần bất kỳ công cụ AI nào. Trên máy tính không có adb, lần đầu mở ứng dụng sẽ nhắc tải từ trang web chính thức của Google (khoảng 10 MB, chỉ tải một lần).

## Năm bước

**1. Kết nối điện thoại**: cắm dây dữ liệu, ứng dụng sẽ nhận ra điện thoại. Chưa bật gỡ lỗi USB, trong trang có hướng dẫn bằng hình ảnh. Trên máy tính không có adb, ứng dụng sẽ nhắc tải từ trang web chính thức của Google.

<p align="center"><img src="../../images/gui-1-connect.png" width="640" alt="Kết nối điện thoại"></p>
<p align="center"><img src="../../images/gui-2-tutorial.png" width="640" alt="Hướng dẫn bằng hình ảnh bật gỡ lỗi USB"></p>

**2. Phát hiện**: đọc ra mẫu máy, phiên bản hệ thống, có kịch bản theo mẫu máy không, trạng thái Quick App và thành phần quảng cáo. Chỉ đọc, không sửa gì. Điện thoại khóa màn hình, điện thoại gập mở ra sẽ nhắc.

<p align="center"><img src="../../images/gui-3-detect.png" width="640" alt="Phát hiện"></p>

**3. Chọn mục cần tắt**:

| Mục | Mặc định |
|---|---|
| Công tắc quảng cáo trong từng ứng dụng (khi có kịch bản theo mẫu máy) | Tích chọn, có thể hủy tích theo từng ứng dụng |
| Thông báo tiếp thị | Loại tiếp thị rõ ràng tích chọn; loại dịch vụ, hoạt động thời gian thực, bảo vệ mắt, sự kiện, cảnh báo và các loại mơ hồ như "Khác / Thông báo chung" mặc định giữ lại |
| Quick App | Không tích, bạn quyết định |
| Thành phần quảng cáo hệ thống | Không tích, bạn quyết định |

<p align="center"><img src="../../images/gui-4-choose.png" width="640" alt="Chọn thông báo tiếp thị"></p>
<p align="center"><img src="../../images/gui-5-choose-more.png" width="640" alt="Chọn Quick App và thành phần quảng cáo"></p>

Trước khi thực thi nếu cần khắc phục kết nối điện thoại, có thể bấm "Kiểm tra kết nối đọc màn hình". Nó chỉ kiểm tra dịch vụ và khả năng đọc trang, không bấm công tắc; thành công không có nghĩa đã xác minh mọi đường dẫn ứng dụng.

**4. Thực thi**: thanh tiến trình cộng nhật ký trực tiếp. Trong lúc thực thi đừng chạm điện thoại.

<p align="center"><img src="../../images/gui-6-run.png" width="640" alt="Thực thi"></p>

**5. Hoàn tất**: liệt kê kết quả từng bước. Thẻ cuối cùng là "Tắt Chế độ nhà phát triển": bấm "Giúp tôi tắt", ứng dụng tắt từ máy tính; hoặc tự tắt trên điện thoại. Tắt đi không hủy thay đổi lần này.

<p align="center"><img src="../../images/gui-7-done.png" width="640" alt="Hoàn tất"></p>

## Phản hồi

Góc dưới bên trái "💬 Phản hồi", hoặc trong trang hoàn tất có "Phản hồi vấn đề này" (khi có bước thất bại xuất hiện).

1. Chọn loại: gặp vấn đề / đề xuất tính năng / tùy chỉnh mẫu máy mới.
2. Viết một câu đã xảy ra gì.
3. Mặc định đính kèm thông tin chẩn đoán: phiên bản ứng dụng, hệ thống máy tính, mẫu máy và phiên bản hệ thống điện thoại (gồm phiên bản HyperOS), kết quả thực thi, 60 dòng nhật ký gần nhất, cùng nguyên nhân đầy đủ của lần thất bại gần nhất. Thư mục người dùng hiện tại và số sê-ri điện thoại trong lỗi đã thay thế, không có nội dung thông báo. Mở rộng "Xem / sửa thông tin chẩn đoán" có thể xóa sửa.
4. Bấm "Gửi tới GitHub", trình duyệt mở trang tạo Issue mới, nội dung đã điền sẵn. Đăng nhập GitHub rồi bấm "Submit new issue".

Nhật ký quá dài, thông tin chẩn đoán sẽ sao chép vào clipboard, dán vào trang đã mở là được.

<p align="center"><img src="../../images/gui-8-feedback.png" width="640" alt="Phản hồi"></p>

## Khôi phục

Góc dưới bên trái "Khôi phục thay đổi": khôi phục Quick App, khôi phục thành phần quảng cáo bị tạm ngưng, mở lại thông báo tiếp thị đã tắt.

<p align="center"><img src="../../images/gui-9-restore.png" width="640" alt="Khôi phục"></p>
Khôi phục cần nối điện thoại, Chế độ nhà phát triển tắt rồi thì theo [00-bat-che-do-nha-phat-trien](00-bat-che-do-nha-phat-trien.md) bật lại.

## Dữ liệu đặt ở đâu

Thư mục dữ liệu Mac:

| Nội dung | Vị trí |
|---|---|
| Ảnh chụp nhanh trước thay đổi, danh sách thông báo tiếp thị, bản ghi tạm ngưng | `~/Library/Application Support/AndroidAdCleaner/backups/` |
| Chẩn đoán đầy đủ của lần thất bại gần nhất (từ 0.2.2, gồm đầu ngoại lệ) | `~/Library/Application Support/AndroidAdCleaner/logs/last-error.txt` |
| adb do ứng dụng tải về | `~/Library/Application Support/AndroidAdCleaner/platform-tools/` |

Thư mục tương ứng trên Windows là `%APPDATA%\AndroidAdCleaner\`; lỗi đầy đủ tại `logs\last-error.txt`, trong đó `backups\` chứa ảnh chụp nhanh và bản ghi, `platform-tools\` chứa adb đã tải. Góc dưới bên trái "Mở thư mục sao lưu" có thể mở trực tiếp.

## Chạy từ mã nguồn và đóng gói

Khi phát triển hoặc tự xây dựng, trước tiên lấy mã nguồn hiện tại:

```bash
git clone https://github.com/rddmwmddr/android-ad-cleaner.git
cd android-ad-cleaner
```

Đã có kho và vùng làm việc sạch thì chuyển sang `main` rồi thực thi `git pull --ff-only`. Có thay đổi của riêng mình thì lưu trước, tránh ghi đè. Gói cài đặt hiện có sẽ không tự động dùng mã nguồn này; cần chạy cổng vào mã nguồn phía dưới.

**Mac chip Apple** (cần cài `uv` trước):

```bash
uv venv --python cpython-3.12-macos-aarch64 gui/.venv
uv pip install --python gui/.venv/bin/python pywebview pyinstaller uiautomator2 pillow
gui/.venv/bin/python gui/app.py          # Chạy
```

**Các nền tảng khác** có thể dùng Python 3.12 đã cài để tạo môi trường ảo, cài `pywebview uiautomator2 pillow` rồi chạy `gui/app.py`; Windows còn cần WebView2. Mã nguồn Windows hiện tại đã qua đóng gói trên đám mây và xác minh GUI gốc, trang khởi động đổi thành đọc trực tiếp tệp cục bộ; kết nối điện thoại, máy tính của người báo cáo và hồi quy Mac Intel của phiên bản mới vẫn chờ hoàn tất, xem Vấn đề đã biết phía dưới. Chỉ cần dòng lệnh, theo README gốc [README](../../README.md) cài `requirements.txt` và chạy `tool/run.py` là được.

Đóng gói Mac cục bộ:

```bash
gui/build_mac.sh                        # Đóng gói tới gui/dist/
```

Đóng gói có ký và kiểm chứng (trước tiên trong keychain chuẩn bị sẵn chứng chỉ Developer ID Application, và dùng `xcrun notarytool store-credentials` lưu thông tin kiểm chứng):

```bash
SIGN_ID="Developer ID Application: 名字 (TEAMID)" NOTARY_PROFILE=公证配置名 gui/build_mac.sh
```

Gói phát hành chỉ chứa chương trình, kịch bản theo mẫu máy và tài nguyên hình ảnh được liệt kê rõ ràng; sẽ không đóng gói nhật ký chạy cục bộ, sao lưu hoặc mẫu máy kiểm thử vào gói. Chương trình chính Intel theo [tài liệu ký PyObjC](https://pyobjc.readthedocs.io/en/latest/notes/codesigning.html) thêm quyền bộ nhớ thực thi cần cho callback; đợt này chỉ bật `allow-jit` vẫn kẹt ở libffi, đổi sang entitlement Intel chuyên dụng rồi qua kiểm thử GUI. Quyền này chỉ cấp cho chương trình chính, giữ hardened runtime và kiểm tra chữ ký thư viện. Kiểm tra phát hành đầy đủ xem nhật ký thay đổi.

## Trình điều khiển Windows

Mac không cần trình điều khiển. Windows không nhận ra điện thoại thì cài trình điều khiển theo hãng:

| Hãng | Trình điều khiển |
|---|---|
| Xiaomi / Redmi | Trợ lý điện thoại Xiaomi hoặc [Google USB Driver](https://developer.android.com/studio/run/win-usb) |
| OPPO / OnePlus / realme | Trợ lý điện thoại OPPO, hoặc Google USB Driver |
| vivo / iQOO | Trợ lý điện thoại vivo |
| Honor / Huawei | Trợ lý điện thoại Huawei / Trợ lý điện thoại Honor (cài xong tắt nó, tránh chiếm kết nối) |
| Khác | Google USB Driver |

Cài xong cắm lại dây, trên điện thoại bấm "Cho phép gỡ lỗi USB".

## Vấn đề đã biết

| Hiện tượng | Giải thích |
|---|---|
| Cửa sổ ở nền, cú bấm đầu tiên chỉ chuyển cửa sổ lên trước | Hành vi mặc định của cửa sổ web macOS, bấm lại một lần |
| Windows hiện "Windows đã bảo vệ máy tính của bạn" | Chương trình cài đặt không có chữ ký mã, bấm "Thêm thông tin" → "Vẫn chạy" |
| Điện thoại gập mở ra không chạy được kịch bản theo mẫu máy | Gập lại dùng màn hình ngoài; thông báo tiếp thị, Quick App, thành phần quảng cáo không bị ảnh hưởng |
| 0.2.0 bấm thực thi rồi lại mở một cửa sổ, hoặc nhiệm vụ con chưa bắt đầu | 0.2.1 đã sửa cổng vào `--cli` của tiến trình con đóng gói, vui lòng cập nhật gói cài đặt |
| Liên kết danh sách vivo / iQOO của 0.2.0 không mở được | Mở trước [danh sách vivo](checklists/vivo-OriginOS.md); 0.2.1 đã sửa chuyển hãng và mã hóa đường dẫn tiếng Trung |
| Mở trên Windows hiện "127.0.0.1 phản hồi quá lâu" | [Issue #18](https://github.com/rddmwmddr/android-ad-cleaner/issues/18): 0.2.1 đổi thành đọc trực tiếp tệp cục bộ, tránh dịch vụ HTTP; vui lòng cập nhật gói cài đặt, máy tính của người báo cáo chờ kiểm chứng lại. Tạm thời chưa cập nhật được thì dùng cổng vào dòng lệnh cũ phía dưới |

### Khi giao diện Windows 0.2.0 không mở được dùng dòng lệnh tích hợp

Giải nén bản portable, trong thư mục chứa `aac-cli.exe` mở PowerShell, không cần cài Python riêng:

```powershell
.\aac-cli.exe --cli run.py --help
.\aac-cli.exe --cli run.py devices
.\aac-cli.exe --cli run.py -s <序列号> check
```

Ở đây vẫn chạy **công cụ 0.2.0**, sẽ không nhận được bản sửa mã nguồn mới nhất. Đừng sao chép thao tác kênh hàng loạt có vấn đề đã biết; có thể kiểm tra chỉ đọc trước, rồi làm thủ công theo [danh sách](checklists/). Cần công cụ mới thì tải 0.2.3, hoặc chạy từ mã nguồn như trên.

### Xác minh giao diện cục bộ

Mã nguồn có thể chạy `python gui/app.py --smoke-gui`; sau khi đóng gói chạy `python gui/smoke_test.py <可执行文件> --gui`. Kiểm tra này xác minh trang, hình ảnh hướng dẫn, giao tiếp JS API và việc không tạo dịch vụ HTTP cục bộ, không kết nối điện thoại. Quy trình Windows sẽ thực thi kiểm tra này với chương trình đã đóng gói, [xác minh trên đám mây 2026-10-25 đã qua](https://github.com/rddmwmddr/android-ad-cleaner/actions/runs/40198943037); qua không có nghĩa đã bao phủ mọi phần mềm bảo mật Windows và môi trường máy tính.

### Quét thông báo xuất hiện ngăn xếp QueryController / UiDevice / UiAutomation

0.2.1 sẽ khởi động dịch vụ đọc màn hình điện thoại trước khi quét thông báo, khởi tạo thất bại thì chặn quét; giao diện chỉ hiện cuối ngoại lệ, không phán đoán được nguyên nhân cụ thể. Vui lòng cập nhật lên 0.2.3: quét và kiểm tra lại trạng thái đọc trực tiếp adb, tắt công tắc vẫn cần đọc màn hình bình thường.

Sau khi kết nối, phát hiện rồi bấm "Kiểm tra kết nối đọc màn hình". Thất bại thì mở rộng "Xem chẩn đoán đầy đủ" hoặc bấm "Sao chép chẩn đoán đầy đủ"; ngay cả khi chưa bắt đầu thực thi, góc dưới bên trái "Phản hồi" cũng sẽ đính kèm lỗi đầy đủ lần này. Vui lòng giữ `Exception` / `Caused by` ở đầu ngoại lệ, đừng chỉ chụp vài dòng cuối.

Kiểm tra chỉ đọc bằng dòng lệnh (trong thư mục bản portable Windows):

```powershell
.\aac-cli.exe --cli run.py -s <序列号> ui-check
```

### Nhắc AccessibilityServiceAlreadyRegisteredError / already registered

Nhật ký đầy đủ 0.2.2 đã xác nhận: Windows 11, Xiaomi 18 Pro Max, OS4.0.27.0.XEOCNXM / Android 17 khi thực tế tắt công tắc, dịch vụ UiAutomation phía điện thoại đã đăng ký, phiên mới bị từ chối. Quảng cáo ứng dụng và bấm thông báo tiếp thị đều cần nó, nên có thể cùng thất bại; bản thân quét thông báo vẫn chạy được. Đây không phải do nhắc `SLF4J` hoặc chữ cuối PyInstaller gây ra lỗi, cũng không thể căn cứ vào đó xác định người chiếm cụ thể.

Phản hồi bổ sung ngày 2026-10-26: cùng người dùng nói 0.2.3 vẫn thất bại, đồng thời tắt GKD và ghi sổ tự động rồi có thể bắt đầu xử lý. Đây là manh mối khắc phục, vẫn chưa xác định công cụ hoặc chế độ cụ thể; không còn dùng nhắc tuyệt đối "không cần tắt dịch vụ trợ năng".

Thứ tự xử lý:

1. Thoát ứng dụng gỡ quảng cáo cũ, Appium, trình kiểm tra UI và các nhiệm vụ tự động hóa khác đang thao tác cùng điện thoại, chỉ giữ một ứng dụng.
2. Kiểm tra GKD, ghi sổ tự động và các công cụ tương tự có bật tự động hóa, đọc màn hình hoặc chế độ Shizuku không. Chỉ tạm dừng chức năng bạn xác nhận có thể tạm dừng; khi cần, chính chủ tạm thời tắt dịch vụ trợ năng của ứng dụng tương ứng, giữ trình đọc màn hình và dịch vụ hỗ trợ mà mình phụ thuộc.
3. Giữ điện thoại mở khóa, sau khi tạm dừng từng mục bấm "Kiểm tra kết nối đọc màn hình". Vẫn nhắc đã đăng ký thì chủ máy có thể tự khởi động lại, trước tiên không khởi động các công cụ tự động hóa trên rồi kiểm tra.
4. Sau khi kiểm tra qua thử lại mục chưa hoàn tất; vẫn thất bại thì sao chép chẩn đoán đầy đủ. Sau đó khôi phục công cụ đã tạm dừng theo nhu cầu, không cần xóa dữ liệu hoặc cài lại ứng dụng nhiều lần.

Mã nguồn mới nhất khi thất bại sẽ kiểm tra chỉ đọc có giới hạn thời gian công tắc tổng và số lượng dịch vụ, và hiện nhắc khắc phục trong tóm tắt lỗi và trang hoàn tất; sẽ không tự động vô hiệu hóa trợ năng. Gói cài đặt 0.2.3 vẫn chưa bao gồm các nhắc mới này, nhưng có thể thực hiện khắc phục thủ công như trên. Thông báo tìm vị trí chụp bị tắt nhầm khôi phục và phạm vi bảo vệ xem [hướng dẫn chuyên biệt](11-xung-dot-doc-man-hinh-va-bao-ve-thong-bao-chuc-nang.md).

0.2.3 trên máy này dùng khóa thiết bị để tránh nhiều tiến trình gỡ quảng cáo cùng đọc màn hình; khởi động thất bại, ngoại lệ thao tác và kết thúc bình thường đều đóng kết nối đã khởi động lần này, đợi nó thoát rồi mới giải phóng khóa. Lỗi đã đăng ký chỉ thử lại một lần; thất bại kéo dài thì thoát rõ ràng, không chờ vô hạn, không dừng mạnh công cụ khác. Nhiệm vụ sau cần đọc màn hình sẽ đánh dấu "Bỏ qua", lỗi đầu tiên vẫn sao chép được, kết thúc chỉ biểu thị thao tác kết thúc như khôi phục luôn sáng, không đại diện mọi mục thành công. Nếu còn cần khắc phục hoặc thử lại, trước tiên giữ gỡ lỗi USB, kết thúc rồi mới tắt.

Cơ sở kỹ thuật: [logic đăng ký UiAutomation của Android](https://android.googlesource.com/platform/frameworks/base/+/master/services/accessibility/java/com/android/server/accessibility/UiAutomationManager.java) giới hạn đồng thời đăng ký một dịch vụ; [mã vòng đời uiautomator2 3.7.1](https://github.com/openatx/uiautomator2/blob/3.7.1/uiautomator2/core.py) mặc định chỉ sau khi khởi tạo thành công mới đăng ký dọn dẹp khi thoát, và dùng cách không chờ thoát. Dự án bổ sung các xử lý dọn dẹp và tiếp nối này, không thể căn cứ vào đó khẳng định người chiếm trên điện thoại phản hồi nhất định do ứng dụng cũ tạo ra.

### Kiểm chứng thực tế mã nguồn OnePlus Ace 2 Pro / ColorOS 14

Mã nguồn mới nhất đã bổ sung kịch bản giới hạn của mẫu máy này và khả năng tương thích trang cài đặt thông báo độc lập, chi tiết xem [bản ghi kiểm chứng thực tế](10-kiem-chung-he-thong-cu-oneplus.md). Những cập nhật này chưa vào gói cài đặt 0.2.3; khi chạy từ mã nguồn cài gói phụ thuộc theo `requirements.txt` gốc. Sau khi máy này lên mạng, 3 đề xuất cá nhân hóa và 6 vị trí quảng cáo cửa hàng đã tắt và đọc lại, 23 thông báo tiếp thị đã tắt. Các ứng dụng khác vẫn có khác biệt cổng vào, không thể viết phạm vi giới hạn thành toàn máy gỡ quảng cáo hoàn tất.

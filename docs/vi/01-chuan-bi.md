# 01 Chuẩn bị

Cách 1 (tác nhân AI) cần trang này. Cách 2, cách 3 chỉ cần điện thoại, bỏ qua trang này.

## Những thứ cần chuẩn bị

| Thứ | Giải thích |
|---|---|
| Máy tính | macOS, Windows, Linux đều được |
| Dây dữ liệu | Dây truyền được dữ liệu. Dây chỉ sạc được cắm vào máy tính sẽ không nhận ra điện thoại |
| Python 3.9 trở lên | macOS có sẵn hoặc cài bằng Homebrew; Windows tải từ python.org |
| adb | platform-tools chính thức của Google |

## Bước một: Cài adb

| Hệ thống | Cách làm |
|---|---|
| macOS | `brew install android-platform-tools` |
| Windows | Tải [platform-tools](https://developer.android.com/tools/releases/platform-tools), giải nén tới `C:\platform-tools`, thêm thư mục này vào PATH |
| Linux | `sudo apt install adb` |

Cài xong nhập `adb version` trong terminal, thấy số phiên bản là được.

## Bước hai: Cài gói phụ thuộc

```bash
pip3 install -r requirements.txt
```

## Bước ba: Trên điện thoại bật Chế độ nhà phát triển và Gỡ lỗi USB

Hướng dẫn từng bước có ảnh chụp màn hình: [00-bat-che-do-nha-phat-trien](00-bat-che-do-nha-phat-trien.md). Cổng vào của năm hãng đều ở trong đó.

## Bước bốn: Kết nối máy tính

1. Cắm dây, trên điện thoại bấm "Cho phép" (xem [00-bat-che-do-nha-phat-trien](00-bat-che-do-nha-phat-trien.md) bước 6).
2. Trên máy tính chạy:

```bash
python3 tool/run.py devices
```

Thấy một dòng như thế này là đã kết nối:

```text
7f386895   OPPO Find N3 典藏版   PHN110   PHN110_16.0.5.1201(CN01)   机型脚本：无（只能跑通用部分）
```

Cột đầu tiên là số sê-ri, các lệnh sau đều dùng nó.

## Không muốn cắm dây: Gỡ lỗi không dây

1. Điện thoại và máy tính nối cùng một Wi-Fi.
2. Tùy chọn nhà phát triển → bật "Gỡ lỗi không dây" → bấm vào → "Ghép nối thiết bị bằng mã ghép nối".
3. Hộp thoại có mã ghép nối 6 chữ số và một "Địa chỉ IP:Cổng", trên máy tính chạy:

```bash
adb pair 192.168.31.100:37xxx      # Địa chỉ và cổng trong hộp thoại
# Nhập mã ghép nối 6 chữ số
adb connect 192.168.31.100:41xxx   # Địa chỉ và cổng hiển thị phía trên trang gỡ lỗi không dây
```

Cổng ghép nối và cổng kết nối là hai số khác nhau. Ghép nối chỉ làm một lần; sau này mỗi lần bật gỡ lỗi không dây, cổng kết nối sẽ thay đổi, dùng cổng mới để `adb connect`.

## Điện thoại gập

Gập điện thoại lại, dùng màn hình ngoài thao tác. Mở ra rồi Cài đặt hệ thống và ứng dụng là bố cục hai cột, phía dưới còn có thanh tác vụ, công cụ sẽ tìm sai vị trí.

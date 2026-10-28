# 04 Viết kịch bản cho mẫu máy mới

Kịch bản theo mẫu máy là một tệp Python, ghi lại "ở ứng dụng nào, bấm những chữ nào, tắt những công tắc nào". Có kịch bản theo mẫu máy, điện thoại cùng mẫu máy vài phút chạy xong.

## Kịch bản theo mẫu máy đặt ở đâu

```text
recipes/<品牌>-<型号>/recipe.py
```

`<型号>` dùng đầu ra của `adb shell getprop ro.product.model`, ví dụ `PLP120`, `M154FF`, `PNM-AN10`. `run.py` tự động khớp theo tên này.

Cùng một kịch bản dùng cho nhiều mẫu máy thì trong kịch bản viết `MODELS = ["M154FF", "2608BPX34C"]`, những mẫu máy này đều sẽ dùng nó.

Khi không có kịch bản của mẫu máy này, `run.py` sẽ tìm kịch bản cùng hãng làm tham khảo, chỉ `recipe --ref` mới chạy, trong ứng dụng mặc định không tích chọn. Kịch bản tham khảo, kịch bản không khớp phiên bản đều chạy bằng **chế độ an toàn**: chỉ tắt công tắc được nêu tên trong `only=[…]`, không tắt toàn trang. Vì vậy trong kịch bản cố gắng viết `only`.

## Vì sao mỗi mẫu máy phải làm riêng

Cùng một hãng, phiên bản nhỏ của hệ thống khác nhau, trang cài đặt cũng sẽ thay đổi. Ví dụ kiểm chứng thực tế:

| Mẫu máy | Hệ thống | Cổng vào cài đặt trình duyệt | Cổng vào cài đặt video |
|---|---|---|---|
| Find N6 | ColorOS 16.0.9 | Dưới cùng ☰ → bánh răng | Của tôi → Cài đặt → Quản lý nội dung cá nhân hóa |
| Find X9 Ultra | ColorOS 16.0.10 | Dưới cùng "Của tôi" → Cài đặt | Không tìm thấy "Của tôi" |

Vì vậy đầu kịch bản theo mẫu máy viết rõ phiên bản hệ thống lúc ghi lại (`BUILD`, so sánh với phần đầu của `ro.build.display.id` hoặc số phiên bản HyperOS của Xiaomi `ro.mi.os.version.incremental`), phiên bản khác nhau công cụ sẽ nhắc và vào chế độ an toàn.

Tên cổng vào giữa phiên bản cũ và mới sẽ thay đổi, trong kịch bản có thể viết thành "có thì bấm, không có thì bỏ qua", tham khảo `maybe()` trong `recipes/xiaomi-M154FF/recipe.py`.

**Công tắc loại bảo vệ**: các công tắc như "Hạn chế theo dõi quảng cáo", "Ngăn chặn theo dõi quảng cáo", "Tắt đề xuất cá nhân hóa" — bắt đầu bằng "Hạn chế / Ngăn chặn / Chặn / Cấm / Tắt" và liên quan tới quảng cáo — bật lên mới là bảo vệ. `p.off()` sẽ gạt chúng sang "bật", kịch bản không cần xử lý thêm.

## Một đoạn kịch bản theo mẫu máy trông như thế nào

```python
# OPPO Find N6（PLP120，ColorOS 16.0.9）机型脚本
BUILD = "PLP120_16.0.9"          # ro.build.display.id 的开头

@step("软件商店")
def _():
    p.start("com.heytap.market")                 # 拉起 App，关掉开屏弹窗
    p.go("我的", "设置")                          # 点「我的」，直到屏幕上出现「设置」
    p.tap("设置", exact=True, scrolls=0)
    if p.tap("隐私", exact=True):                 # 找到「隐私」就点，找不到会翻页
        p.off(only=["个性化推荐"], page="商店·隐私")   # 只关标题含「个性化推荐」的开关
        p.back()
    if p.tap("服务管理", exact=True):
        p.off(keep=["帮助与客服", "应用安全"], page="商店·服务管理")   # 全关，保留这两项
        p.back()
```

Định nghĩa `@step` sao chép đoạn đầu của kịch bản theo mẫu máy có sẵn là được. (Chú thích mã và chuỗi giao diện trong khối trên giữ nguyên tiếng Trung gốc, vì đó là nhãn bấm theo nghĩa đen và chú thích từ kịch bản nguồn.)

## Các thao tác công cụ cung cấp

| Thao tác | Tác dụng |
|---|---|
| `p.start(包名, activity=None)` | Mở ứng dụng hoặc trang chỉ định |
| `p.setting(关键词, 结果)` | Tìm từ khóa trong Cài đặt hệ thống, bấm kết quả tìm kiếm |
| `p.tap(文字, exact=True, scrolls=6)` | Tìm thấy chữ thì bấm; `scrolls=0` chỉ nhìn màn hình hiện tại, trong 3 giây vừa chờ vừa đóng hộp thoại |
| `p.go(文字, 期望)` | Bấm chữ, cho tới khi chữ mong đợi xuất hiện |
| `p.off(keep=[], only=None, page="")` | Tắt công tắc đang bật trên trang hiện tại; `only` chỉ tắt những cái này, `keep` giữ lại những cái này |
| `p.back(n)` | Bấm quay lại n lần |
| `p.find(文字)` | Chỉ tìm không bấm, trả về tọa độ hoặc None |
| `p.confirm()` | Khi tắt công tắc hiện hộp xác nhận, bấm xác nhận |
| `p.d.shell(命令)` | Thực thi lệnh shell bất kỳ |

Trong một đoạn, cổng vào đầu tiên không tìm thấy, các cổng vào sau chỉ nhìn màn hình hiện tại, không lật trang nữa, đoạn này vài giây kết thúc, không bấm lung tung.

## Các bước viết kịch bản theo mẫu máy

1. Đi thủ công một lượt:

   ```bash
   python3 tool/fast.py -s S ls            # 看当前屏幕上有什么字、什么开关
   python3 tool/fast.py -s S tap 我的 设置   # 一步一步点进去
   python3 tool/fast.py -s S scan          # 到了设置页，列出所有开关
   ```

   (Các lệnh trên giữ nguyên, kể cả từ bấm ví dụ tiếng Trung `我的 设置` là nhãn hiển thị theo nghĩa đen trên điện thoại tiếng Trung; chú thích dịch là: xem trên màn hình hiện tại có chữ gì, công tắc gì / bấm từng bước vào / tới trang cài đặt rồi liệt kê tất cả công tắc.)

2. Viết đường dẫn đã đi thông thành `@step`.
3. Trang nào có thể mở bằng activity thì viết bằng activity, nhanh nhất và ổn định nhất:

   ```bash
   adb -s S shell dumpsys window | grep mCurrentFocus   # 停在设置页时查当前 activity
   ```

   Viết thành `p.start("包名", ".settings.XxxActivity")`.

4. Chạy một lượt: `python3 tool/run.py -s S recipe 软件商店`.
5. Chạy toàn bộ, ghi lại thời gian dùng, điền vào bảng mẫu máy trong README.

## Công cụ dò đường (thử nghiệm)

```bash
python3 tool/explore.py -s S com.heytap.market com.heytap.browser
```

Lần lượt mở trang cài đặt và trang con của ứng dụng, liệt kê công tắc giống quảng cáo, xuất ra `探路-<型号>.tsv`. Chỉ đọc, không gạt công tắc. Hiện tại ở một số ứng dụng vào trang con rồi không quay lại được, kết quả chỉ để tham khảo.

## Gửi PR

1. Tạo mới `recipes/<品牌>-<型号>/recipe.py`.
2. Trong danh sách của hãng tương ứng tại `docs/checklists/` bổ sung khác biệt của mẫu máy này.
3. Trong bảng mẫu máy của README thêm một dòng, ghi rõ ngày kiểm chứng thực tế và thời gian dùng.
4. Không gửi thư mục `backups/`, trong đó có danh sách ứng dụng và bản ghi thông báo của điện thoại bạn.


# 📊 Phân Tích Cảm Xúc Đánh Giá Sản Phẩm

Dự án này thực hiện phân tích cảm xúc trên dữ liệu đánh giá sản phẩm (reviews) bằng Python. Sử dụng thư viện **TextBlob** để xác định cảm xúc (tích cực / trung lập / tiêu cực), và trực quan hóa kết quả bằng **Matplotlib**, **Seaborn** và **WordCloud**.

---

## 📁 1. Dữ liệu

* **Tên file:** `data.csv`
* **Cột bắt buộc:**

  * `reviews.text`: nội dung đánh giá sản phẩm.
  * `name`: tên sản phẩm (để tổng hợp theo sản phẩm).
  * `reviews.rating`: điểm đánh giá từ 1 đến 5 sao (nếu có).

---

## 🛠️ 2. Các bước thực hiện

### ✅ Tiền xử lý:

* Đọc dữ liệu từ CSV.
* Loại bỏ các dòng không có nội dung đánh giá (`NaN` trong `reviews.text`).

### ✅ Phân tích cảm xúc:

* Sử dụng **TextBlob** để tính `sentiment.polarity`.

  * > 0.1 → `Tích cực`
  * < -0.1 → `Tiêu cực`
  * còn lại → `Trung lập`

### ✅ Trực quan hóa:

1. **Phân phối cảm xúc:** Biểu đồ cột số lượng đánh giá theo loại cảm xúc.
2. **Phân phối điểm sao:** Biểu đồ cột điểm đánh giá từ 1–5 (nếu có cột `reviews.rating`).
3. **Tương quan cảm xúc – điểm đánh giá:** Biểu đồ hộp giữa cảm xúc và điểm sao.
4. **Top 10 sản phẩm có nhiều đánh giá:** Biểu đồ cột chồng thể hiện số đánh giá tích cực và tiêu cực theo sản phẩm.
5. **WordCloud:** Từ khóa phổ biến trong các đánh giá tích cực và tiêu cực.

---

## 🧰 3. Yêu cầu thư viện

```bash
pip install pandas matplotlib seaborn textblob wordcloud
python -m textblob.download_corpora
```

---

## 🚀 4. Hướng dẫn chạy

Đảm bảo file `data.csv` có định dạng đúng và nằm cùng thư mục với file `.py`. Sau đó, chỉ cần chạy script Python:

```bash
python script_phan_tich_cam_xuc.py
```

---

## 📌 5. Ghi chú

* Dữ liệu cần có định dạng văn bản rõ ràng. Cần lọc spam, ký tự đặc biệt nếu cần chất lượng WordCloud cao.
* Có thể thay đổi ngưỡng cảm xúc (±0.1) tùy theo bài toán cụ thể.

---

## 📷 Ví dụ kết quả

* 📈 Biểu đồ phân phối cảm xúc
* ⭐ Biểu đồ điểm đánh giá sao
* 📊 Tương quan cảm xúc và điểm
* 🔝 Top 10 sản phẩm được nhắc đến nhiều
* ☁️ WordCloud từ khóa nổi bật theo cảm xúc

---

## 🧠 Tác giả

Phân tích cảm xúc đơn giản với TextBlob, phù hợp với bài toán đánh giá sản phẩm thương mại điện tử, app store, nhà hàng, v.v.

---

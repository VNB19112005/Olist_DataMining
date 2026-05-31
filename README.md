# Dự án Khai phá dữ liệu Olist (Olist Data Mining Project)

## Phần việc đảm nhận: Tiền xử lý & Thiết kế Kho dữ liệu
**Thành viên thực hiện:** Nguyên Bảo

### 1. Tiền xử lý dữ liệu (preprocessing.py)
- Gộp các bảng dữ liệu gốc: Orders, Order_Items, Customers, Products, Sellers.
- Chuẩn hóa các cột thời gian sang định dạng `datetime`.
- Xử lý loại bỏ các dòng dữ liệu trùng lặp (`drop_duplicates`).
- Tính toán 2 biến mới: Doanh thu (`revenue` = price + freight_value) và Số ngày giao hàng thực tế (`delivery_days`).

### 2. Thiết kế Kho dữ liệu (warehouse.py)
Áp dụng mô hình hình sao (Star Schema) để tách dữ liệu sạch thành các bảng phục vụ phân tích EDA:
- **Bảng Fact:** `fact_sales.csv` (chứa các khóa ngoại và chỉ số đo lường).
- **Bảng Dim:** `dim_customer.csv`, `dim_product.csv`, `dim_seller.csv`, `dim_date.csv` (tách chi tiết theo ngày, tháng, năm, quý, thứ).

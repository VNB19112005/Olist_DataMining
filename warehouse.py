import os
import pandas as pd

# tao thu muc chua kho du lieu neu chua co
os.makedirs('data/warehouse', exist_ok=True)

# doc file sach da lam tu buoc truoc
print("Dang doc file final_sales.csv...")
df = pd.read_csv('data/processed/final_sales.csv')
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])

# tao bang dim_customer
print("Dang tao dim_customer...")
dim_customer = df[['customer_id', 'customer_unique_id', 'customer_zip_code_prefix', 'customer_city', 'customer_state']].drop_duplicates()
dim_customer.to_csv('data/warehouse/dim_customer.csv', index=False)

# tao bang dim_product
print("Dang tao dim_product...")
dim_product = df[['product_id', 'product_category_name', 'product_name_lenght', 'product_description_lenght', 'product_photos_qty']].drop_duplicates()
dim_product.to_csv('data/warehouse/dim_product.csv', index=False)

# tao bang dim_seller
print("Dang tao dim_seller...")
dim_seller = df[['seller_id', 'seller_zip_code_prefix', 'seller_city', 'seller_state']].drop_duplicates()
dim_seller.to_csv('data/warehouse/dim_seller.csv', index=False)

# tao bang dim_date de phuc vu phan tich theo thoi gian
print("Dang tao dim_date...")
dim_date = pd.DataFrame({'order_purchase_timestamp': df['order_purchase_timestamp'].unique()})
dim_date['date_key'] = dim_date['order_purchase_timestamp']
dim_date['year'] = dim_date['order_purchase_timestamp'].dt.year
dim_date['month'] = dim_date['order_purchase_timestamp'].dt.month
dim_date['day'] = dim_date['order_purchase_timestamp'].dt.day
dim_date['quarter'] = dim_date['order_purchase_timestamp'].dt.quarter
dim_date['day_of_week'] = dim_date['order_purchase_timestamp'].dt.dayofweek
dim_date.to_csv('data/warehouse/dim_date.csv', index=False)

# tao bang fact_sales chinh
print("Dang tao fact_sales...")
fact_sales = df[[
    'order_id', 'customer_id', 'product_id', 'seller_id', 'order_purchase_timestamp',
    'price', 'freight_value', 'revenue', 'delivery_days', 'order_status'
]]
fact_sales.to_csv('data/warehouse/fact_sales.csv', index=False)

print("Done! Da tach xong cac bang fact va dim.")
import os
import pandas as pd

# doc du lieu goc
print("Dang doc cac file csv...")
orders = pd.read_csv('olist_orders_dataset.csv')
order_items = pd.read_csv('olist_order_items_dataset.csv')
customers = pd.read_csv('olist_customers_dataset.csv')
products = pd.read_csv('olist_products_dataset.csv')
sellers = pd.read_csv('olist_sellers_dataset.csv')
payments = pd.read_csv('olist_order_payments_dataset.csv')

# gop cac bang lai voi nhau
print("Dang merge du lieu...")
df = pd.merge(orders, customers, on='customer_id', how='inner')
df = pd.merge(df, order_items, on='order_id', how='inner')
df = pd.merge(df, products, on='product_id', how='left')
df = pd.merge(df, sellers, on='seller_id', how='left')
df = pd.merge(df, payments, on='order_id', how='left')

# chuan hoa dinh dang ngay thang
date_columns = [
    'order_purchase_timestamp', 
    'order_approved_at', 
    'order_delivered_carrier_date', 
    'order_delivered_customer_date', 
    'order_estimated_delivery_date'
]
for col in date_columns:
    df[col] = pd.to_datetime(df[col], errors='coerce')

# tinh toan cac bien moi (delivery_days va revenue)
df['delivery_days'] = (df['order_delivered_customer_date'] - df['order_delivered_carrier_date']).dt.days
df['revenue'] = df['price'] + df['freight_value']

# xoa cac dong trung nhau
df = df.drop_duplicates()

# xuat file ket qua
os.makedirs('data/processed', exist_ok=True)
df.to_csv('data/processed/final_sales.csv', index=False)

print("Done! Luu file final_sales.csv thanh cong.")
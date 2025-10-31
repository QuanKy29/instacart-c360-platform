import pandas as pd
from sqlalchemy import create_engine
import os

# --- Thông tin kết nối Postgres ---
PG_USER = "admin"
PG_PASS = "admin"
PG_HOST = "localhost"
PG_PORT = "5432"
PG_DB = "instacart"

# Tạo kết nối tới Postgres
engine = create_engine(f"postgresql://{PG_USER}:{PG_PASS}@{PG_HOST}:{PG_PORT}/{PG_DB}")

# --- Danh sách bảng GOLD cần export ---
gold_tables = [
    "mart_user_summary",
    "mart_product_summary",
    "mart_user_product_features"
]

output_dir = "ml/exported_data"
os.makedirs(output_dir, exist_ok=True)

# --- Export từng bảng ---
for table in gold_tables:
    print(f"🔹 Exporting {table} ...")
    df = pd.read_sql(f"SELECT * FROM gold.{table}", engine)
    out_path = f"{output_dir}/{table}.csv"
    df.to_csv(out_path, index=False)
    print(f"✅ Saved: {out_path}")

print("\n🎉 All gold tables exported successfully!")
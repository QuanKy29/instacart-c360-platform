import os
import pandas as pd
from sqlalchemy import create_engine, text
from tqdm import tqdm

DB_URL = "postgresql+psycopg2://admin:admin@localhost:5432/instacart"

# path tới thư mục data/raw trong project
DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "raw"))

FILES = {
    "raw.aisles": "aisles.csv",
    "raw.departments": "departments.csv",
    "raw.products": "products.csv",
    "raw.orders": "orders.csv",
    "raw.order_products_prior": "order_products__prior.csv",
    "raw.order_products_train": "order_products__train.csv",
}

DDL = {
    "raw.aisles": """
        CREATE TABLE IF NOT EXISTS raw.aisles (
            aisle_id INT PRIMARY KEY,
            aisle TEXT
        );
    """,
    "raw.departments": """
        CREATE TABLE IF NOT EXISTS raw.departments (
            department_id INT PRIMARY KEY,
            department TEXT
        );
    """,
    "raw.products": """
        CREATE TABLE IF NOT EXISTS raw.products (
            product_id INT PRIMARY KEY,
            product_name TEXT,
            aisle_id INT,
            department_id INT
        );
    """,
    "raw.orders": """
        CREATE TABLE IF NOT EXISTS raw.orders (
            order_id INT PRIMARY KEY,
            user_id INT,
            eval_set TEXT,
            order_number INT,
            order_dow INT,
            order_hour_of_day INT,
            days_since_prior_order INT
        );
    """,
    "raw.order_products_prior": """
        CREATE TABLE IF NOT EXISTS raw.order_products_prior (
            order_id INT,
            product_id INT,
            add_to_cart_order INT,
            reordered INT
        );
    """,
    "raw.order_products_train": """
        CREATE TABLE IF NOT EXISTS raw.order_products_train (
            order_id INT,
            product_id INT,
            add_to_cart_order INT,
            reordered INT
        );
    """,
}

DTYPES = {
    "raw.aisles": {"aisle_id": "Int64", "aisle": "string"},
    "raw.departments": {"department_id": "Int64", "department": "string"},
    "raw.products": {
        "product_id": "Int64",
        "product_name": "string",
        "aisle_id": "Int64",
        "department_id": "Int64",
    },
    "raw.orders": {
        "order_id": "Int64",
        "user_id": "Int64",
        "eval_set": "string",
        "order_number": "Int64",
        "order_dow": "Int64",
        "order_hour_of_day": "Int64",
        "days_since_prior_order": "Int64",
    },
    "raw.order_products_prior": {
        "order_id": "Int64",
        "product_id": "Int64",
        "add_to_cart_order": "Int64",
        "reordered": "Int64",
    },
    "raw.order_products_train": {
        "order_id": "Int64",
        "product_id": "Int64",
        "add_to_cart_order": "Int64",
        "reordered": "Int64",
    },
}

INDEX_SQL = [
    "CREATE INDEX IF NOT EXISTS idx_orders_user ON raw.orders(user_id);",
    "CREATE INDEX IF NOT EXISTS idx_op_prior_order ON raw.order_products_prior(order_id);",
    "CREATE INDEX IF NOT EXISTS idx_op_prior_product ON raw.order_products_prior(product_id);",
    "CREATE INDEX IF NOT EXISTS idx_op_train_order ON raw.order_products_train(order_id);",
    "CREATE INDEX IF NOT EXISTS idx_products_aisle ON raw.products(aisle_id);",
    "CREATE INDEX IF NOT EXISTS idx_products_dept ON raw.products(department_id);",
]

def load_table(engine, fqtn, csv_name, chunksize=200_000):
    csv_path = os.path.join(DATA_DIR, csv_name)
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"{csv_path} not found")
    print(f"\n==> Loading {fqtn} from {csv_path}")

    # create table
    with engine.begin() as conn:
        conn.execute(text(DDL[fqtn]))

    # empty before load (idempotent)
    with engine.begin() as conn:
        conn.execute(text(f"TRUNCATE TABLE {fqtn};"))

    dtype = DTYPES[fqtn]
    total_rows = 0
    for chunk in pd.read_csv(csv_path, dtype=dtype, chunksize=chunksize):
        chunk = chunk.where(pd.notnull(chunk), None)  # NaN -> NULL
        chunk.to_sql(fqtn.split(".")[1], engine, schema=fqtn.split(".")[0],
                     if_exists="append", index=False, method="multi")
        total_rows += len(chunk)
        print(f"  inserted +{len(chunk):,} rows (total {total_rows:,})")

    print(f"Done {fqtn}: {total_rows:,} rows")

def main():
    print(f"DATA_DIR = {DATA_DIR}")
    engine = create_engine(DB_URL, pool_pre_ping=True)

    # ensure schema
    with engine.begin() as conn:
        conn.execute(text("CREATE SCHEMA IF NOT EXISTS raw;"))

    order = [
        "raw.aisles",
        "raw.departments",
        "raw.products",
        "raw.orders",
        "raw.order_products_prior",
        "raw.order_products_train",
    ]
    for fqtn in order:
        load_table(engine, fqtn, FILES[fqtn])

    print("\nCreating indexes…")
    with engine.begin() as conn:
        for sql in INDEX_SQL:
            conn.execute(text(sql))
    print("All done ✅")

if __name__ == "__main__":
    main()

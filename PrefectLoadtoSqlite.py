from prefect import task, flow
import pandas as pd
import sqlite3


# --------------------
# 1. Task: Extract
# --------------------
@task
def extract_data(file_path: str) -> pd.DataFrame:
    """
    ดึงข้อมูลจากไฟล์ CSV
    """
    print(f"Extracting data from {file_path}...")
    df = pd.read_csv(file_path)
    return df


# --------------------
# 2. Task: Transform
# --------------------
@task
def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    แปลงข้อมูล (Clean & Feature Engineering)
    """
    print("Transforming data...")

    # ลบแถวที่มี Missing Values
    df = df.dropna()

    # สร้างคอลัมน์ใหม่
    df['total_sales'] = df['price'] * df['quantity']

    # แปลง Categorical เป็น Numeric
    if 'category' in df.columns:
        df['category_encoded'] = df['category'].astype('category').cat.codes

    return df


# --------------------
# 3. Task: Load
# --------------------
@task
def load_data(df: pd.DataFrame, db_path: str, table_name: str):
    """
    โหลดข้อมูลลง SQLite Database
    """
    print(f"Loading data into {db_path}...")
    conn = sqlite3.connect(db_path)

    # เขียนข้อมูลลง Table
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()
    print(f"Data successfully loaded into table: {table_name}")


# --------------------
# 4. Flow: Orchestrate ETL
# --------------------
@flow
def etl_flow(file_path: str, db_path: str, table_name: str):
    """
    กระบวนการ ETL Flow
    """
    # Step 1: Extract
    raw_data = extract_data(file_path)

    # Step 2: Transform
    transformed_data = transform_data(raw_data)

    # Step 3: Load
    load_data(transformed_data, db_path, table_name)


# --------------------
# 5. Run ETL Flow
# --------------------
if __name__ == "__main__":
    # ระบุพารามิเตอร์
    FILE_PATH = "cleaned_data.csv"  # ไฟล์ CSV ที่จะใช้
    DB_PATH = "etl_data.db"  # ไฟล์ SQLite Database
    TABLE_NAME = "cleaned_table"  # ชื่อ Table

    # เรียกใช้งาน ETL Flow
    etl_flow(FILE_PATH, DB_PATH, TABLE_NAME)

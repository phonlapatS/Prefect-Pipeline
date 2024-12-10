from prefect import task, flow
import pandas as pd
import sqlite3


# ------------------------------
# 1. Task: Extract
# ------------------------------
@task
def extract_data(file_path: str) -> pd.DataFrame:
    """
    ดึงข้อมูลจากไฟล์ CSV
    """
    print(f"Extracting data from {file_path}...")
    df = pd.read_csv(file_path)
    return df


# ------------------------------
# 2. Task: Transform
# ------------------------------
@task
def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    แปลงข้อมูล: แทน Missing Values ด้วย Mean
    """
    print("Transforming data: Filling missing values with mean...")

    # แทน Missing Values ด้วยค่าเฉลี่ยของแต่ละคอลัมน์
    for column in df.select_dtypes(include=['float64', 'int64']).columns:
        if df[column].isnull().sum() > 0:  # ตรวจสอบว่ามี Missing Values หรือไม่
            mean_value = df[column].mean()  # คำนวณค่าเฉลี่ย
            df[column] = df[column].fillna(mean_value)  # แทนค่าที่หายไปด้วย Mean

            print(f"Filled missing values in column '{column}' with mean value: {mean_value}")

    return df


# ------------------------------
# 3. Task: Load
# ------------------------------
@task
def load_data(df: pd.DataFrame, db_path: str, table_name: str):
    """
    โหลดข้อมูลลง SQLite Database
    """
    print(f"Loading data into {db_path}...")
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists="replace", index=False)  # โหลดข้อมูลลง Table
    conn.close()
    print(f"Data successfully loaded into table: {table_name}")


# ------------------------------
# 4. Flow: Orchestrate ETL
# ------------------------------
@flow
def etl_flow_test(file_path: str, db_path: str, table_name: str):
    """
    กระบวนการ ETL Workflow ด้วย Prefect
    """
    # Step 1: Extract
    raw_data = extract_data(file_path)

    # Step 2: Transform
    transformed_data = transform_data(raw_data)

    # Step 3: Load
    load_data(transformed_data, db_path, table_name)


# ------------------------------
# 5. Run the Flow
# ------------------------------
if __name__ == "__main__":
    # กำหนดพารามิเตอร์
    FILE_PATH = "cleaned_data.csv"  # ไฟล์ CSV ที่จะใช้
    DB_PATH = "wine_quality.db"  # SQLite Database ที่จะสร้าง
    TABLE_NAME = "redwine_data"  # ชื่อ Table

    # เรียกใช้งาน ETL Flow
    etl_flow_test(FILE_PATH, DB_PATH, TABLE_NAME)

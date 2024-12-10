import sqlite3

# เชื่อมต่อกับฐานข้อมูล
conn = sqlite3.connect("wine_quality.db")  # ใช้ชื่อฐานข้อมูลที่สร้างโดย Prefect
cursor = conn.cursor()

# ตรวจสอบว่าตาราง 'wine_data' มีข้อมูลหรือไม่
cursor.execute("SELECT COUNT(*) FROM redwine_data")  # นับจำนวนแถวในตาราง
row_count = cursor.fetchone()[0]

if row_count > 0:
    print(f"Data has been successfully loaded into 'wine_data'. Total rows: {row_count}")
else:
    print("No data found in 'wine_data'. Please check your ETL pipeline.")

# ปิดการเชื่อมต่อ
conn.close()

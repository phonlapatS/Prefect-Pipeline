import sqlite3
import pandas as pd

# -----------------------------
# 1. สร้าง Database และ Table
# -----------------------------
# สร้างการเชื่อมต่อไปยังฐานข้อมูล SQLite
conn = sqlite3.connect("wine_quality.db")

# # สร้าง Cursor สำหรับรันคำสั่ง SQL
# cursor = conn.cursor()
#
# # สร้าง Table ชื่อ `wine_data` ให้ตรงกับโครงสร้างข้อมูล
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS wine_data (
#     fixed_acidity REAL,
#     volatile_acidity REAL,
#     citric_acid REAL,
#     residual_sugar REAL,
#     chlorides REAL,
#     free_sulfur_dioxide REAL,
#     total_sulfur_dioxide REAL,
#     density REAL,
#     pH REAL,
#     sulphates REAL,
#     alcohol REAL,
#     quality INTEGER
# )
# """)
#
# print("Table 'wine_data' has been created successfully!")
#
# # ปิดการเชื่อมต่อ
# conn.close()

# -----------------------------
# 2. โหลดข้อมูลจาก CSV ลงใน Table
# -----------------------------

# โหลดข้อมูลจากไฟล์ CSV
# df = pd.read_csv("cleaned_data.csv")
#
# # เขียนข้อมูลลงใน Table
# df.to_sql("redwine_data", conn, if_exists="replace", index=False)
#
# print("Data has been successfully loaded into 'wine_data' table!")
#
# # ปิดการเชื่อมต่อ
# conn.close()

# -----------------------------
# 3. ตรวจสอบข้อมูลใน Table
# -----------------------------
# สร้างการเชื่อมต่อไปยังฐานข้อมูล
cursor = conn.cursor()

# ดึงข้อมูลทั้งหมดจากตาราง (ตัวอย่าง 5 แถวแรก)
cursor.execute("SELECT * FROM redwine_data LIMIT 10")  # จำกัดการแสดงผลแค่ 5 แถว
rows = cursor.fetchall()

# แสดงข้อมูลที่ดึงมา
print("Sample data from 'redwine_data' table:")
for row in rows:
    print(row)

# ปิดการเชื่อมต่อ
conn.close()

# Data Pipeline with Prefect using Python and Sqlite3 based on ETL Process

ETL Process concept : 

<p align="center">
  <img src="https://github.com/user-attachments/assets/9a5b806a-52cd-443b-b9cc-a94e1a19ce07" alt="ETL Process Concept 1" />
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/90c963ca-7216-4392-b76c-6607d354ea23" alt="ETL Process Concept 2" />
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/57886215-0b1f-4611-8bd5-b7d5679805b0" alt="ETL Process Concept 3" />
</p>

## Library that use in this project
![Library that used in this project](images/library.png)

### Working step:
1. Extract
   ![Extract step](images/extract.png)
2. Transform
   ![Transform step](images/transform.png)
3. Load
   ![Load step](images/load.png)

---

## See task and flow status in Prefect Dashboard
type 'prefect start server' to check out the dashboard at http://127.0.0.1:4200

## Dashboard
![Prefect Dashboard](images/Dashboard.png)

### 1. ดูสถานะ Flow
![ภาพ Flow Overview](images/flow_overview.png)

### 2. การทำงานของ Task
![ภาพ Task Details](images/Task.png)

---

### ตรวจสอบใน Sqlite3
เข้า DB ผ่าน Terminal
![Use database](images/use_winedata_db.png)

### ตรวจสอบโครงสร้างของตาราง
.schema redwine_data
![See table structure](images/table_structure.png)

### ดูข้อมูลในตาราง
SELECT * FROM redwine_data
![See table data](images/see_data.png)

### ปรับให้มีหัวตารางและแสดงออกมาเป็น column ด้วย 2 คำสั่งนี้

.headers on

.mode column

SELECT * FROM redwine_data อีกครั้ง

![Justify Table](images/justify_table.png)
  



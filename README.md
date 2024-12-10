# Try to do pipeline with Prefect using python and sqlite3 to understand about ETL Process
![Library that used in this project](images/library.png)

ETL Process :
![ETL Process Concept 1](https://example.com/path/to/your/image.png](https://www.google.com.hk/url?sa=i&url=https%3A%2F%2Fwww.geeksforgeeks.org%2Fetl-process-in-data-warehouse%2F&psig=AOvVaw2to_QSLnOPKnGATKXk2TLp&ust=1733921034594000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCJjMhK2dnYoDFQAAAAAdAAAAABAE)


![ETL Process Concept 2](https://www.google.com.hk/url?sa=i&url=https%3A%2F%2Fwww.informatica.com%2Fresources%2Farticles%2Fwhat-is-etl.html&psig=AOvVaw2to_QSLnOPKnGATKXk2TLp&ust=1733921034594000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCJjMhK2dnYoDFQAAAAAdAAAAABAJ)

Working step:
1. Extract
   ![Extract step](images/extract.png)
2. Transform
   ![Transform step](images/transform.png)
3. Load
   ![Load step](images/load.png)


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
  



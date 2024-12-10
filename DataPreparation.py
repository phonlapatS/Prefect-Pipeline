import pandas as pd
import matplotlib.pyplot as plt
# import matplotlib.pyplot as plt

# pd.set_option('display.max_rows', None)  # แสดงจำนวนแถวทั้งหมด
# pd.set_option('display.max_columns', None)  # แสดงจำนวนคอลัมน์ทั้งหมด
# pd.set_option('display.width', None)  # ปรับความกว้างเพื่อให้แสดงข้อมูลทั้งหมดในแนวนอน


#data = pd.read_csv('money.csv')
data = pd.read_csv('winequality-red.csv', sep=';')
# data = pd.read_csv('cleaned_data.csv')


print(data) #ดูข้อมูลทั้งหมด

# data['alcohol'].plot(kind='hist', bins=20, title='Distribution of Alcohol')
# plt.xlabel('Alcohol')
# plt.show()

# ตัวอย่างความสัมพันธ์ระหว่าง alcohol และ quality
# data.plot(kind='scatter', x='alcohol', y='quality', title='Alcohol vs Quality')
# plt.show()


#print(data.head())
#print(data.info())  # ตรวจสอบชนิดข้อมูลและ Missing Values
#print(data.describe())  # สถิติเบื้องต้น
#print(data.duplicated().sum())  # จำนวนแถวที่ซ้ำกัน
#print(data.unique()) # ตรวจสอบค่าที่ไม่ซ้ำกันในแต่ละคอลัมน์

#data.to_csv('cleaned_data.csv', index=False) # สร้างไฟล์ csv ใหม่ที่ผ่านการคลีนแล้ว

# print(data.isnull().sum()) # ตรวจสอบจำนวนค่าว่างในแต่ละคอลัมน์
#data = data.dropna() #ลบแถวที่มีค่าว่าง
#data['fixed acidity'] = data['fixed acidity'].fillna(data['fixed acidity'].mean()) # เติมค่าแทน เช่น ค่าเฉลี่ย หรือ ค่ากลาง





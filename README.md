# 🌧️ OutRain - Rainfall Monitoring Dashboard

**OutRain** เป็นโปรเจกต์ต้นแบบสำหรับการแสดงผลข้อมูลปริมาณน้ำฝนจากสถานีตรวจวัดของประเทศไทย รองรับการกรองตามจังหวัด ลุ่มน้ำ และเลือกสถานีเฉพาะ เพื่อแสดงแผนที่และกราฟปริมาณฝนย้อนหลัง ใช้สำหรับการตรวจสอบข้อมูลฝนเบื้องต้น

> **Project Status**: 🚧 In Development


## 🔧 Tech Stack

- Python
- Streamlit
- PostgreSQL
- Pandas
- PyDeck (Map visualization)
- SQLAlchemy / psycopg2

---

## 📁 โครงสร้างโปรเจกต์

```
outrain_app/
├── app.py               # Entry point ของแอป Streamlit
├── db/
│   └── connection.py    # ฟังก์ชันเชื่อมต่อ PostgreSQL
├── data/
│   ├── stations.py      # โหลดข้อมูลสถานี
│   └── rainfall.py      # โหลดข้อมูลฝน
├── ui/
│   └── map_view.py      # ส่วน UI - map และกราฟ
└── utils/
    └── helpers.py       # ฟังก์ชันช่วยเหลืออื่น ๆ
```

---

## 🚀 วิธีใช้งาน

### 1. ติดตั้งไลบรารีที่จำเป็น

```bash
pip install -r requirements.txt
```

> ไฟล์ `requirements.txt` ตัวอย่าง:
```txt
streamlit
pandas
psycopg2-binary
pydeck
```

### 2. ตั้งค่าการเชื่อมต่อฐานข้อมูล

แก้ไขไฟล์ `db/connection.py` ให้ตรงกับการตั้งค่าของคุณ เช่น:

```python
return psycopg2.connect(
    host="localhost",
    port="5432",
    database="flowcast",
    user="postgres",
    password="1234"
)
```

### 3. เตรียมฐานข้อมูล PostgreSQL

สร้างตาราง (หรือ import จาก CSV) ให้มีโครงสร้างดังนี้:

#### ตาราง `station_info`

| station_code | station_name | latitude | longitude | province | basin |
|--------------|--------------|----------|-----------|----------|-------|

#### ตาราง `rainfalltimeseries`

| station_code | time                | rainfall |
|--------------|---------------------|----------|
| ST001        | 2024-04-01 10:00:00 | 5.0 mm   |

---

### 4. รันระบบ

```bash
streamlit run app.py
```

---

## ✅ ฟีเจอร์

- แผนที่สถานีตรวจวัดฝน (PyDeck)
- กรองข้อมูลตามจังหวัด/ลุ่มน้ำ/สถานี
- แสดงกราฟปริมาณฝนย้อนหลังตามช่วงวันที่เลือก
- ออกแบบสไตล์เรียบง่ายใช้งานง่าย

---

## 🖼️ ตัวอย่างหน้าจอแอป

ภาพตัวอย่างแอป Rainfall Time Series Viewer ขณะใช้งาน:

![screenshot](images/Example_OutRain.gif)

---

## 📌 หมายเหตุ

- ระบบนี้เป็น **ต้นแบบ (Prototype)** สำหรับการพัฒนา Dashboard ตรวจสอบข้อมูลฝนแบบ Near Real-Time
- มีแผนพัฒนาเพิ่มเติม เช่น การแสดง shapefile, ตรวจสอบค่าผิดปกติ (Outlier)

---

## 👨‍💻 ผู้พัฒนา: hphummar

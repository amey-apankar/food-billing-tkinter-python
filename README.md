# 🍴 Food Billing System — Tkinter + Python + MySQL

A beginner-friendly GUI-based food billing system built using **Python’s Tkinter** module. It allows users to select food items, calculate the total bill, generate a simple bill preview, and optionally save the billing data into a **MySQL database**.

---

## 🚀 Features

- Clean and simple GUI with Tkinter
- Itemized selection
- Automatic total price calculation
- Bill preview generation
- Option to save billing data to MySQL

---

## 🛠 Tech Stack

- Python 3.x  
- Tkinter (GUI)  
- MySQL  
- mysql-connector-python  

---

## 📁 Repository Contents

```
├── foodbilling.py     # Main Python GUI app
├── food_world_tkinter.sql     # MySQL database and table structure
└── README.md          # Project documentation
```

---

## ⚙️ How to Run

### 1. Install Required Package

Install the MySQL connector for Python:

```bash
pip install mysql-connector-python
```

---

### 2. Set Up the MySQL Database

This app stores billing records in a MySQL database.  
To set it up:

- Use the provided `database.sql` file  
- Open your MySQL tool (Workbench, phpMyAdmin, or terminal)
- Import `database.sql` to automatically create:
  - A database: `food_world`
  - A table: `bills`

Example using terminal:
```bash
mysql -u your_username -p < database.sql
```

> ✅ You only need to do this once during setup.

---

### 3. Update Your Database Credentials

In `tkinter billing system (1).py`, make sure to enter your MySQL credentials:
```python
mysql.connector.connect(
  host="localhost",
  user="your_username",
  password="your_password",
  database="food_world"
)
```

---

### 4. Run the App

Once setup is done, start the application:

```bash
python tkinter billing system (1).py
```

---

## 📸 Screenshots



---




**Made with ❤️ using Python by Amey Apankar**

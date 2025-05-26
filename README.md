# 🏨 Hotel Management System

A professional Python-based Hotel Management System with a Tkinter GUI and MySQL database integration. This project allows hotel staff to manage customers, employees, rooms, and bookings through an intuitive desktop interface — with no terminal input required.

---

## 📌 Features

### 🔹 Customer Management
- Add, view, delete, and search customer records
- Store full names and addresses
- Clean and centered input forms

### 🔹 Employee Management
- Add, view, delete, and update employee information
- Assign roles and shifts
- Add dependents (relatives) for each employee

### 🔹 Room & Booking Management
- Check room availability
- Calculate total bill for bookings based on food & beverage items

---

## 🖼️ GUI Highlights
- Fully built with **Tkinter**
- Modular window-based interface (Customer, Employee, Room)
- No command-line input — all interactions through forms and buttons
- Responsive, centered layout

---

## 🗃️ Database Schema

Uses a MySQL database named `HotelManagment` with the following tables:

- `customer(customer_ID, fname, mname, lname, address)`
- `employee(emp_ID, fname, mname, lname, role, shifts)`
- `dependents(emp_ID, dependent_name, DoB, gender, relation)`
- `room(room_ID, availability)`
- `food_and_beverage(booking_ID, item_name, quantity, item_price)`

You can modify the schema in `MySQL` Workbench or import from a `.sql` dump (optional).

---

## ⚙️ Installation

### 🔧 Requirements
- Python 3.x
- Tkinter (comes pre-installed)
- `mysql-connector-python`

Install dependencies:
```bash
pip install mysql-connector-python
💻 Run the App
Make sure your MySQL server is running.
Set up the HotelManagment database and tables.
Clone this repo and open the main script:
python hotel_gui.py
🔐 Configuration

You can adjust the MySQL connection settings in the script:
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="HotelManagment"
)
📁 Project Structure

hotel-management/
│
├── hotel_gui.py         # Main application file
├── README.md            # Project documentation
└── requirements.txt     # Optional: list dependencies
✨ Future Improvements

Add login/authentication system
Export reports to PDF or Excel
Connect to a cloud MySQL instance
Dark/light theme toggle
🧑‍💻 Author

Zainab Ali Taha
Effat University
Course Project – Python GUI + MySQL Integration

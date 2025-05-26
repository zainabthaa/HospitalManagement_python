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

---

## ⚙️ Installation

### 🔧 Requirements
- Python 3.x
- Tkinter (comes pre-installed)
- `mysql-connector-python`

You can adjust the MySQL connection settings in the script:
`mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="HotelManagment"
)`

##🧑‍💻 Author

Zainab Ali Taha
Effat University
GCS182 Project – Python GUI + MySQL Integration

import tkinter as tk
from tkinter import messagebox, simpledialog, Toplevel
import mysql.connector

# MySQL connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="HotelManagment"
)
cursor = mydb.cursor()

# Helper: Center a window on screen
def center_window(win, width=400, height=400):
    win.update_idletasks()
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    win.geometry(f"{width}x{height}+{x}+{y}")

# GUI Sections 

def open_customer_menu():
    win = Toplevel()
    win.title("Customer Menu")
    center_window(win)
    
    tk.Button(win, text="Show All Customers", command=show_all_customer).pack(pady=5)
    tk.Button(win, text="Add Customer", command=add_customer_gui).pack(pady=5)
    tk.Button(win, text="Delete Customer", command=delete_customer_gui).pack(pady=5)
    tk.Button(win, text="Find Customer", command=find_customer_gui).pack(pady=5)
    tk.Button(win, text="Back", command=win.destroy).pack(pady=10)

def open_employee_menu():
    win = Toplevel()
    win.title("Employee Menu")
    center_window(win)

    tk.Button(win, text="Show All Employees", command=show_all_employee).pack(pady=5)
    tk.Button(win, text="Add Employee", command=add_employee_gui).pack(pady=5)
    tk.Button(win, text="Add Dependent", command=add_relative_to_employee_gui).pack(pady=5)
    tk.Button(win, text="Delete Employee", command=delete_employee_gui).pack(pady=5)
    tk.Button(win, text="Find Employee", command=find_employee_gui).pack(pady=5)
    tk.Button(win, text="Update Role", command=update_employee_gui).pack(pady=5)
    tk.Button(win, text="Back", command=win.destroy).pack(pady=10)

def open_room_menu():
    win = Toplevel()
    win.title("Room Menu")
    center_window(win)

    tk.Button(win, text="Check Room Availability", command=check_room_availability_gui).pack(pady=5)
    tk.Button(win, text="Total Bill for Booking", command=umm_gui).pack(pady=5)
    tk.Button(win, text="Back", command=win.destroy).pack(pady=10)

# GUI Implementations 

from tkinter import ttk

def show_all_customer():
    # Create a new top-level window
    top = tk.Toplevel()
    top.title("All Customers")
    top.geometry("700x400")

    # Manually center the window
    top.update_idletasks()
    width = top.winfo_width()
    height = top.winfo_height()
    x = (top.winfo_screenwidth() // 2) - (width // 2)
    y = (top.winfo_screenheight() // 2) - (height // 2)
    top.geometry(f"+{x}+{y}")

    # Create a Treeview widget
    columns = ("ID", "First Name", "Middle Name", "Last Name", "Address")
    tree = ttk.Treeview(top, columns=columns, show="headings")

    # Define headings
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=130)

    # Insert customer data
    cursor.execute("SELECT * FROM customer")
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)

    # Add a scrollbar
    scrollbar = ttk.Scrollbar(top, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)

    # Layout
    tree.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")


from tkinter import ttk

def show_all_employee():
    # Create a new top-level window
    top = tk.Toplevel()
    top.title("All Employees")
    top.geometry("800x400")

    # Manually center the window
    top.update_idletasks()
    width = top.winfo_width()
    height = top.winfo_height()
    x = (top.winfo_screenwidth() // 2) - (width // 2)
    y = (top.winfo_screenheight() // 2) - (height // 2)
    top.geometry(f"+{x}+{y}")

    # Create a Treeview widget
    columns = ("ID", "First Name", "Middle Name", "Last Name", "Role", "Shifts")
    tree = ttk.Treeview(top, columns=columns, show="headings")

    # Define headings
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=120)

    # Insert employee data
    cursor.execute("SELECT * FROM employee")
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)

    # Add a scrollbar
    scrollbar = ttk.Scrollbar(top, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)

    # Layout
    tree.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

def add_customer_gui():
    form_popup("Add Customer", ["Customer ID", "First Name", "Middle Name", "Last Name", "Address"],
               lambda vals: execute_query(
                   "INSERT INTO customer (customer_ID, fname, mname, lname, address) VALUES (%s, %s, %s, %s, %s)", vals,
                   "Customer Added"))

def add_employee_gui():
    form_popup("Add Employee", ["Employee ID", "First Name", "Middle Name", "Last Name", "Role", "Shifts"],
               lambda vals: execute_query(
                   "INSERT INTO employee (emp_ID, fname, mname, lname, role, shifts) VALUES (%s, %s, %s, %s, %s, %s)", vals,
                   "Employee Added"))

def add_relative_to_employee_gui():
    form_popup("Add Dependent", ["Employee ID", "Dependent Name", "DOB", "Gender", "Relation"],
               lambda vals: execute_query(
                   "INSERT INTO dependents (emp_ID, dependent_name, DoB, gender, relation) VALUES (%s, %s, %s, %s, %s)", vals,
                   "Dependent Added"))

def delete_customer_gui():
    single_input_popup("Delete Customer", "Customer ID",
                       lambda cid: delete_entity("customer", "customer_ID", cid))

def delete_employee_gui():
    single_input_popup("Delete Employee", "Employee ID",
                       lambda eid: delete_entity("employee", "emp_ID", eid))

def find_customer_gui():
    single_input_popup("Find Customer", "Customer ID", lambda cid: show_customer_info(cid))

def find_employee_gui():
    single_input_popup("Find Employee", "Employee ID", lambda eid: show_employee_info(eid))

def update_employee_gui():
    form_popup("Update Employee Role", ["Employee ID", "New Role", "New Shift"],
               lambda vals: execute_query("UPDATE employee SET role = %s, shifts = %s WHERE emp_ID = %s",
                                          (vals[1], vals[2], vals[0]), "Employee Updated"))

def check_room_availability_gui():
    single_input_popup("Check Room Availability", "Room ID", check_room_availability)

def umm_gui():
    single_input_popup("Get Booking Total", "Booking ID", get_booking_total)

# Utility Functions 

def execute_query(query, values, success_msg):
    try:
        cursor.execute(query, values)
        mydb.commit()
        messagebox.showinfo("Success", success_msg)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_entity(table, id_field, value):
    cursor.execute(f"SELECT * FROM {table} WHERE {id_field} = %s", (value,))
    if not cursor.fetchone():
        messagebox.showwarning("Not Found", f"No {table} found with that ID.")
    else:
        cursor.execute(f"DELETE FROM {table} WHERE {id_field} = %s", (value,))
        mydb.commit()
        messagebox.showinfo("Deleted", f"{table.capitalize()} deleted successfully.")

def show_customer_info(cid):
    cursor.execute("SELECT * FROM customer WHERE customer_ID = %s", (cid,))
    customer = cursor.fetchone()
    if customer:
        info = f"Customer ID: {customer[0]}\nFirst Name: {customer[1]}\nMiddle: {customer[2]}\nLast: {customer[3]}\nAddress: {customer[4]}"
        messagebox.showinfo("Customer Info", info)
    else:
        messagebox.showwarning("Not Found", "No Customer found with this ID.")

def show_employee_info(eid):
    cursor.execute("SELECT * FROM employee WHERE emp_ID = %s", (eid,))
    emp = cursor.fetchone()
    if emp:
        info = f"Employee ID: {emp[0]}\nFirst Name: {emp[1]}\nMiddle: {emp[2]}\nLast: {emp[3]}\nRole: {emp[4]}\nShifts: {emp[5]}"
        messagebox.showinfo("Employee Info", info)
    else:
        messagebox.showwarning("Not Found", "No Employee found with this ID.")

def check_room_availability(room_id):
    cursor.execute("SELECT availability FROM room WHERE room_ID = %s", (room_id,))
    result = cursor.fetchone()
    if result:
        status = "Available" if result[0] else "Not Available"
        messagebox.showinfo("Room Status", f"Room {room_id} is {status}.")
    else:
        messagebox.showwarning("Not Found", "Room not found.")

def get_booking_total(bid):
    cursor.execute(
        "SELECT booking_ID, item_name, SUM(quantity * item_price) AS total FROM food_and_beverage WHERE booking_ID = %s GROUP BY booking_ID",
        (bid,))
    result = cursor.fetchone()
    if result:
        messagebox.showinfo("Booking Total", f"Booking ID: {result[0]}\nItem: {result[1]}\nTotal Bill: {result[2]}")
    else:
        messagebox.showwarning("Not Found", "No booking found.")

def form_popup(title, fields, on_submit):
    popup = Toplevel()
    popup.title(title)
    center_window(popup, 300, 400)
    entries = []
    for field in fields:
        tk.Label(popup, text=field).pack()
        entry = tk.Entry(popup)
        entry.pack(pady=2)
        entries.append(entry)

    def submit():
        values = [e.get() for e in entries]
        if all(values):
            on_submit(values)
            popup.destroy()
        else:
            messagebox.showwarning("Incomplete", "Please fill all fields.")

    tk.Button(popup, text="Submit", command=submit).pack(pady=10)

def single_input_popup(title, prompt, on_submit):
    popup = Toplevel()
    popup.title(title)
    center_window(popup, 300, 150)
    tk.Label(popup, text=prompt).pack(pady=5)
    entry = tk.Entry(popup)
    entry.pack(pady=5)

    def submit():
        val = entry.get()
        if val:
            on_submit(val)
            popup.destroy()
        else:
            messagebox.showwarning("Input Required", "Please enter a value.")

    tk.Button(popup, text="Submit", command=submit).pack(pady=10)

# Main Menu 
def main():
    root = tk.Tk()
    root.title("Welcome to XYZ Hotel")
    center_window(root, 400, 300)

    tk.Label(root, text="XYZ Hotel Management System", font=("Arial", 14)).pack(pady=20)

    tk.Button(root, text="Customer Menu", command=open_customer_menu, width=25).pack(pady=5)
    tk.Button(root, text="Employee Menu", command=open_employee_menu, width=25).pack(pady=5)
    tk.Button(root, text="Room Menu", command=open_room_menu, width=25).pack(pady=5)
    tk.Button(root, text="Exit", command=root.quit, width=25).pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()

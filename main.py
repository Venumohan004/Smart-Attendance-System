import tkinter as tk
from tkinter import messagebox, ttk

# Import backend functions
from attendance import (
    mark_attendance,
    view_attendance,
    search_attendance,
    update_attendance,
    delete_attendance,
    total_attendance,
    delete_all_attendance
)

# Create Main Window
root = tk.Tk()
root.title("Smart Attendance System")
root.geometry("500x750")
root.resizable(False, False)

# ------------------ Heading ------------------

title = tk.Label(
    root,
    text="SMART ATTENDANCE SYSTEM",
    font=("Arial", 20, "bold"),
    fg="blue"
)
title.pack(pady=20)

# ------------------ Name ------------------

name_label = tk.Label(root, text="Student Name", font=("Arial", 12))
name_label.pack()

name_entry = tk.Entry(root, width=35)
name_entry.pack(pady=5)

# ------------------ Roll ------------------

roll_label = tk.Label(root, text="Roll Number", font=("Arial", 12))
roll_label.pack()

roll_entry = tk.Entry(root, width=35)
roll_entry.pack(pady=5)


# ------------------ Save Attendance ------------------

def save_attendance():

    name = name_entry.get().strip()
    roll = roll_entry.get().strip()

    if name == "" or roll == "":
        messagebox.showerror("Error", "Please fill all fields")
        return

    success = mark_attendance(name, roll)

    if success:
        messagebox.showinfo("Success", "Attendance Marked Successfully")

        name_entry.delete(0, tk.END)
        roll_entry.delete(0, tk.END)

    else:
        messagebox.showwarning(
            "Warning",
            "Attendance already marked today."
        )

def show_attendance():

    records = view_attendance()

    view_window = tk.Toplevel(root)
    view_window.title("Attendance Records")
    view_window.geometry("700x400")

    tree = ttk.Treeview(
        view_window,
        columns=("Roll", "Name", "Date", "Time"),
        show="headings"
    )

    tree.heading("Roll", text="Roll")
    tree.heading("Name", text="Name")
    tree.heading("Date", text="Date")
    tree.heading("Time", text="Time")

    tree.column("Roll", width=100, anchor="center")
    tree.column("Name", width=200, anchor="center")
    tree.column("Date", width=150, anchor="center")
    tree.column("Time", width=150, anchor="center")

    for record in records:
        tree.insert("", tk.END, values=record)

    tree.pack(fill="both", expand=True, padx=10, pady=10)
    
def search_record():

    roll = roll_entry.get().strip()

    if roll == "":
        messagebox.showerror(
            "Error",
            "Enter Roll Number"
        )
        return

    record = search_attendance(roll)

    if record:

        messagebox.showinfo(
            "Attendance Found",
            f"Roll : {record[0]}\n"
            f"Name : {record[1]}\n"
            f"Date : {record[2]}\n"
            f"Time : {record[3]}"
        )

    else:

        messagebox.showerror(
            "Not Found",
            "Attendance Record Not Found"
        )

def update_record():

    update_window = tk.Toplevel(root)
    update_window.title("Update Attendance")
    update_window.geometry("350x220")
    update_window.resizable(False, False)

    tk.Label(
        update_window,
        text="Roll Number",
        font=("Arial", 11)
    ).pack(pady=5)

    roll_entry_update = tk.Entry(update_window, width=30)
    roll_entry_update.pack()

    tk.Label(
        update_window,
        text="New Student Name",
        font=("Arial", 11)
    ).pack(pady=5)

    name_entry_update = tk.Entry(update_window, width=30)
    name_entry_update.pack()

    def update_data():

        roll = roll_entry_update.get().strip()
        name = name_entry_update.get().strip()

        if roll == "" or name == "":
            messagebox.showerror(
                "Error",
                "Please fill all fields"
            )
            return

        success = update_attendance(roll, name)

        if success:

            messagebox.showinfo(
                "Success",
                "Attendance Updated Successfully"
            )

            update_window.destroy()

        else:

            messagebox.showerror(
                "Error",
                "Record Not Found"
            )

    tk.Button(
        update_window,
        text="Update",
        command=update_data,
        bg="green",
        fg="white",
        width=18
    ).pack(pady=20)

def delete_record():

    delete_window = tk.Toplevel(root)
    delete_window.title("Delete Attendance")
    delete_window.geometry("350x180")
    delete_window.resizable(False, False)

    tk.Label(
        delete_window,
        text="Roll Number",
        font=("Arial", 11)
    ).pack(pady=10)

    roll_entry_delete = tk.Entry(delete_window, width=30)
    roll_entry_delete.pack()

    def delete_data():

        roll = roll_entry_delete.get().strip()

        if roll == "":
            messagebox.showerror(
                "Error",
                "Enter Roll Number"
            )
            return

        success = delete_attendance(roll)

        if success:

            messagebox.showinfo(
                "Success",
                "Attendance Deleted Successfully"
            )

            delete_window.destroy()

        else:

            messagebox.showerror(
                "Error",
                "Record Not Found"
            )

    tk.Button(
        delete_window,
        text="Delete",
        command=delete_data,
        bg="red",
        fg="white",
        width=18
    ).pack(pady=20)
        
def show_total():

    total = total_attendance()

    messagebox.showinfo(
        "Total Attendance",
        f"Total Attendance Records : {total}"
    )

def delete_all_records():

    answer = messagebox.askyesno(
        "Confirmation",
        "Are you sure you want to delete all attendance records?"
    )

    if answer:

        delete_all_attendance()

        messagebox.showinfo(
            "Success",
            "All Attendance Deleted Successfully"
        )

def exit_program():

    answer = messagebox.askyesno(
        "Exit",
        "Do you really want to exit?"
    )

    if answer:
        root.destroy()

# ------------------ Button ------------------

mark_btn = tk.Button(
    root,
    text="Mark Attendance",
    command=save_attendance,
    bg="green",
    fg="white",
    font=("Arial", 12, "bold"),
    width=20
)

mark_btn.pack(pady=15)

view_btn = tk.Button(
    root,
    text="View Attendance",
    command=show_attendance,
    bg="blue",
    fg="white",
    font=("Arial", 12, "bold"),
    width=20
)

view_btn.pack(pady=8)

search_btn = tk.Button(
    root,
    text="Search Attendance",
    command=search_record,
    bg="orange",
    fg="white",
    font=("Arial",12,"bold"),
    width=20
)

search_btn.pack(pady=8)

update_btn = tk.Button(
    root,
    text="Update Attendance",
    command=update_record,
    bg="purple",
    fg="white",
    font=("Arial",12,"bold"),
    width=20
)

update_btn.pack(pady=8)

delete_btn = tk.Button(
    root,
    text="Delete Attendance",
    command=delete_record,
    bg="red",
    fg="white",
    font=("Arial", 12, "bold"),
    width=20
)

delete_btn.pack(pady=8)

total_btn = tk.Button(
    root,
    text="Total Attendance",
    command=show_total,
    bg="brown",
    fg="white",
    font=("Arial",12,"bold"),
    width=20
)

total_btn.pack(pady=8)

delete_all_btn = tk.Button(
    root,
    text="Delete All",
    command=delete_all_records,
    bg="darkred",
    fg="white",
    font=("Arial",12,"bold"),
    width=20
)

delete_all_btn.pack(pady=8)

exit_btn = tk.Button(
    root,
    text="Exit",
    command=exit_program,
    bg="black",
    fg="white",
    font=("Arial",12,"bold"),
    width=20
)

exit_btn.pack(pady=8)

root.mainloop()
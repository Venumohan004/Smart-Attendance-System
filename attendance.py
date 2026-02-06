#Smart Attendance System using python

from datetime import datetime
import os

if not os.path.exists("attendance.txt"):
    open("attendance.txt","w").close()

print("file and modules ready")

def mark_attendance():
    name = input("Enter Student name: ")
    roll = input("Enter roll number: ")

    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    print("\n Attendance Details")
    print("Name:", name)
    print("Roll:", roll)
    print("Date:", date)
    print("Time:", time)

    with open("attendance.txt","r") as file:
        records = file.readlines()
        for record in records:
            if roll in record and date in record:
                print("Attendance already marked today")
                return
            
    with open("attendance.txt","a") as file:
        file.write(f"{roll},{name},{date},{time}\n")
        print("Attendance marked successfully")

 

def view_attendance():
    try:
        with open("attendance.txt", "r") as file:
            print("\n ROLL | NAME | DATE | TIME")
            print("----------------------------")
            for line in file:
                roll,name,date,time = line.strip().split(",")
                print(f"{roll} | {name} | {time}")
    except FileNotFoundError:
        print("Attendance file not found")


while True:
    print("\n SMART ATTENDANCE SYSTEM")
    print("1. Mark Attendance")
    print("2. view Attendance")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        mark_attendance()
    elif choice == "2":
        view_attendance()
    elif choice == "3":
        print("Thank you! Exiting program.")
        break
    else:
        print("Invalid choice. try again.")

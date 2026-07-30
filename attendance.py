from datetime import datetime
import csv
import os

FILE_NAME = "attendance.csv"

# Create CSV file automatically
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Roll", "Name", "Date", "Time"])


# MARK ATTENDANCE
def mark_attendance(name, roll):

    if not name or not roll:
        return False
    
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if len(row) == 4 and row[0] == roll and row[2] == date:
                return False

    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([roll, name, date, time])

    return True


# VIEW ATTENDANCE
def view_attendance():

    records = []

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)

        next(reader)

        for row in reader:
            if len(row) == 4:
                records.append(row)

    return records

# SEARCH ATTENDANCE
def search_attendance(roll_no):
    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if len(row) == 4 and row[0] == roll_no:
                return row
    return None

# DELETE ATTENDANCE
def delete_attendance(roll_no):
    updated_records = []
    deleted = False

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)

        header = next(reader)
        updated_records.append(header)

        for row in reader:
            if len(row) == 4:
                if row[0] != roll_no:
                    updated_records.append(row)
                else:
                    deleted = True

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(updated_records)

    return deleted


# UPDATE ATTENDANCE
def update_attendance(roll_no, new_name):
    updated_records = []
    updated = False

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)

        header = next(reader)
        updated_records.append(header)

        for row in reader:
            if len(row) == 4:
                if row[0] == roll_no:
                    now = datetime.now()
                    new_date = now.strftime("%Y-%m-%d")
                    new_time = now.strftime("%H:%M:%S")

                    updated_records.append(
                        [roll_no, new_name, new_date, new_time]
                    )
                    updated = True
                else:
                    updated_records.append(row)

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(updated_records)

    return updated


# TOTAL ATTENDANCE
def total_attendance():
    count = 0

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if len(row) == 4:
                count += 1

    return count


# DELETE ALL ATTENDANCE
def delete_all_attendance():
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Roll", "Name", "Date", "Time"])

    return True


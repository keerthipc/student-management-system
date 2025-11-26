# STUDENT MANAGEMENT SYSTEM

import os

FILE = "students.txt"


def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    course = input("Enter Course: ")
    age = input("Enter Age: ")

    with open(FILE, "a") as f:
        f.write(f"{roll},{name},{course},{age}\n")

    print("Student added successfully!")


def display_students():
    print("\n--- All Student Records ---")
    if not os.path.exists(FILE):
        print("No student records found.")
        return

    with open(FILE, "r") as f:
        data = f.readlines()
        if not data:
            print("No records to display.")
            return

        for line in data:
            roll, name, course, age = line.strip().split(",")
            print(f"Roll: {roll} | Name: {name} | Course: {course} | Age: {age}")


def search_student():
    roll = input("Enter Roll Number to Search: ")
    found = False

    if not os.path.exists(FILE):
        print("No student records found.")
        return

    with open(FILE, "r") as f:
        for line in f:
            r, name, course, age = line.strip().split(",")
            if r == roll:
                print("\n--- Student Found ---")
                print(f"Roll: {r}, Name: {name}, Course: {course}, Age: {age}")
                found = True
                break

    if not found:
        print("Student not found!")


def update_student():
    roll = input("Enter Roll Number to Update: ")

    if not os.path.exists(FILE):
        print("No student records found.")
        return

    updated = False
    new_data = []

    with open(FILE, "r") as f:
        for line in f:
            r, name, course, age = line.strip().split(",")
            if r == roll:
                print("\nEnter new details:")
                new_name = input("New Name: ")
                new_course = input("New Course: ")
                new_age = input("New Age: ")
                new_data.append(f"{roll},{new_name},{new_course},{new_age}\n")
                updated = True
            else:
                new_data.append(line)

    if updated:
        with open(FILE, "w") as f:
            f.writelines(new_data)
        print("Student record updated!")
    else:
        print("Student not found!")


def delete_student():
    roll = input("Enter Roll Number to Delete: ")

    if not os.path.exists(FILE):
        print("No student records found.")
        return

    deleted = False
    new_data = []

    with open(FILE, "r") as f:
        for line in f:
            r, name, course, age = line.strip().split(",")
            if r == roll:
                deleted = True
                continue
            new_data.append(line)

    if deleted:
        with open(FILE, "w") as f:
            f.writelines(new_data)
        print("Student deleted successfully!")
    else:
        print("Student not found!")


def main_menu():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting system...")
            break
        else:
            print("Invalid choice, try again!")


# Run Program
main_menu()



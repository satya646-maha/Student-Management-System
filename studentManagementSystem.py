
students = []

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    marks = input("Enter Marks: ")

    student = {
        "Roll": roll,
        "Name": name,
        "Age": age,
        "Marks": marks
    }

    students.append(student)
    print("Student added successfully!")


def view_students():
    if not students:
        print("No student records found.")
    else:
        print("\n--- Student Details ---")
        for student in students:
            print("Roll Number:", student["Roll"])
            print("Name:", student["Name"])
            print("Age:", student["Age"])
            print("Marks:", student["Marks"])
            print("----------------------")


def search_student():
    roll = input("Enter Roll Number to Search: ")

    for student in students:
        if student["Roll"] == roll:
            print("Student Found!")
            print(student)
            return

    print("Student Not Found!")


def update_student():
    roll = input("Enter Roll Number to Update: ")

    for student in students:
        if student["Roll"] == roll:
            student["Name"] = input("Enter New Name: ")
            student["Age"] = input("Enter New Age: ")
            student["Marks"] = input("Enter New Marks: ")
            print("Student Updated Successfully!")
            return

    print("Student Not Found!")


def delete_student():
    roll = input("Enter Roll Number to Delete: ")

    for student in students:
        if student["Roll"] == roll:
            students.remove(student)
            print("Student Deleted Successfully!")
            return

    print("Student Not Found!")


while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Thank You!")
        break
    else:
        print("Invalid Choice! Try Again.")

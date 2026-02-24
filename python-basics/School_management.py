import students
import Lecturers

students.show_details("Jane Doe", 1.2, "Baseball")

Lecturers.show_details("Brian KIbet", 1.6, "Rugby")

# Student Registration and Course Management System

students = []   # list to store all student records


def register_student():
    print("\n--- Register New Student ---")
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    course = input("Enter Course: ")
    phone = input("Enter Phone Number: ")

    student = {
        "ID": student_id,
        "Name": name,
        "Course": course,
        "Phone": phone,
        "Grades": {}
    }

    students.append(student)
    print("Student registered successfully!\n")


def display_students():
    if not students:
        print("\nNo students registered yet.\n")
        return

    print("\n--- Registered Students ---")
    for student in students:
        print(f"\nID: {student['ID']}")
        print(f"Name: {student['Name']}")
        print(f"Course: {student['Course']}")
        print(f"Phone: {student['Phone']}")

        if student["Grades"]:
            print("Grades:")
            for subject, grade in student["Grades"].items():
                print(f"  {subject}: {grade}")
        else:
            print("Grades: Not assigned yet")
    print()


def assign_course_and_grade():
    if not students:
        print("\n⚠ No students registered yet.\n")
        return

    student_id = input("\nEnter Student ID to assign course & grade: ")

    for student in students:
        if student["ID"] == student_id:
            subject = input("Enter Subject/Course Name: ")
            grade = input("Enter Grade: ")

            student["Grades"][subject] = grade
            print("Course and grade assigned successfully!\n")
            return

    print("Student not found.\n")


while True:
    print("==== Student Management Menu ====")
    print("1. Register New Student")
    print("2. Display Registered Students")
    print("3. Assign New Course and Grade")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        register_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        assign_course_and_grade()
    elif choice == "4":
        print("\n Exiting program. Goodbye!")
        break
    else:
        print("\n Invalid choice. Try again.\n")
from students import Students, Marks


students = {
    1: Marks("Amina", 20, "Female", "Python", 1),
    2: Marks("Bravin", 19, "Male", "Mobile Development", 2),
    3: Marks("Cathy", 18, "Female", "AI and Digital Marketing", 3),
    4: Marks("Daniel", 19, "Male", "Social Mobile Management", 4),
    5: Marks("Ethan", 21, "Male", "Generative AI", 5)
}


def main():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Register Student")
        print("2. Verify Student ID")
        print("3. Display Student Record")
        print("4. Update Student Record")
        print("5. Enter Student Marks")
        print("6. Search Registration Number")
        print("7. Display All Registered Students")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                reg_no = int(input("Enter registration number: "))

                if reg_no in students:
                    print("Registration number already exists.")
                    continue

                name = input("Enter student name: ")
                age = int(input("Enter student age: "))
                gender = input("Enter student gender: ")
                course = input("Enter student course: ")

                student = Marks(name, age, gender, course, reg_no)
                students[reg_no] = student
                student.registration()

            except ValueError:
                print("Please enter valid student details.")

        elif choice == "2":
            try:
                reg_no = int(input("Enter student registration number: "))

                if reg_no in students:
                    print("Welcome student!")
                    students[reg_no].student_record()
                else:
                    print("This student number does not exist.")

            except ValueError:
                print("Enter a valid registration number.")

        elif choice == "3":
            try:
                reg_no = int(input("Enter registration number: "))

                if reg_no in students:
                    students[reg_no].student_record()
                else:
                    print("Student not found.")

            except ValueError:
                print("Enter a valid registration number.")

        elif choice == "4":
            try:
                reg_no = int(input("Enter registration number: "))

                if reg_no in students:
                    students[reg_no].update_student_record()
                else:
                    print("Student not found.")

            except ValueError:
                print("Enter a valid registration number.")

        elif choice == "5":
            try:
                reg_no = int(input("Enter registration number: "))

                if reg_no in students:
                    students[reg_no].student_marks()
                else:
                    print("Student not found.")

            except ValueError:
                print("Enter a valid registration number.")

        elif choice == "6":
            search_student = Marks("", 0, "", "", 0)
            search_student.search_register_id(students)

        elif choice == "7":
            if students:
                for student in students.values():
                    print("\n------------------------")
                    student.display_registered_students()
            else:
                print("No students registered.")

        elif choice == "8":
            print("Thank you for using the Student Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
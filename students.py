class Students:
    def __init__(self, name, age, gender, course, reg_no=0):
        self.name = name
        self.age = age
        self.gender = gender
        self.course = course
        self.reg_no = reg_no

    def registration(self):
        if self.reg_no > 0:
            print(f"{self.name} has successfully been registered.")
        else:
            print("Invalid registration number.")

    def student_id(self):
        number = int(input("Enter your student number: "))

        if number == self.reg_no:
            print("Welcome student!")
        else:
            print("This number does not exist.")

    def student_record(self):
        print("\n--- Student Record ---")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Course: {self.course}")
        print(f"Registration Number: {self.reg_no}")

    def update_student_record(self):
        while True:
            print("\n--- Update Student Record ---")
            print("1. Update Name")
            print("2. Update Age")
            print("3. Update Gender")
            print("4. Update Course")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.name = input("Enter new name: ")
                print("Name updated successfully.")

            elif choice == "2":
                try:
                    age = int(input("Enter new age: "))
                    if age > 0:
                        self.age = age
                        print("Age updated successfully.")
                    else:
                        print("Age must be greater than zero.")
                except ValueError:
                    print("Please enter a valid age.")

            elif choice == "3":
                self.gender = input("Enter new gender: ")
                print("Gender updated successfully.")

            elif choice == "4":
                self.course = input("Enter new course: ")
                print("Course updated successfully.")

            elif choice == "5":
                print("Exiting student record.")
                break

            else:
                print("Invalid choice. Please try again.")


class Marks(Students):
    def __init__(self, name, age, gender, course, reg_no, marks=0):
        super().__init__(name, age, gender, course, reg_no)
        self.marks = marks

    def student_marks(self):
        try:
            marks = float(input("Enter your score: "))

            if 0 <= marks <= 100:
                self.marks = marks
                print(f"Your score is {self.marks}")
                print(f"Your grade is {self.average_grade()}")
            else:
                print("Marks must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")

    def average_grade(self):
        if self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 50:
            return "D"
        else:
            return "E"

    def search_register_id(self, students):
        try:
            number = int(input("Enter your registration number: "))

            if number in students:
                print("Student verified successfully.")
                students[number].student_record()
            else:
                print("Error, student not found!")

        except ValueError:
            print("Enter a valid registration number.")

    def display_registered_students(self):
        self.student_record()
        print(f"Marks: {self.marks}")
    
        print(f"Grade: {self.average_grade()}")
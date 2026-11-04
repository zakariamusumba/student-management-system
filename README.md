# student-management-system
# Student Management System

## 1. Project Description

The Student Management System is a Python-based application designed to manage student information, registration details, academic records, and student marks.

The system allows users to register students, verify student registration numbers, view student records, update student information, enter marks, and calculate grades.

## 2. Project Objectives

- To simplify student registration and record management.
- To store and manage student personal information.
- To allow students to be verified using registration numbers.
- To update student records when necessary.
- To record student marks and calculate grades.
- To display all registered students.

## 3. Features

1. **Student Registration** – Registers new students with unique registration numbers.
2. **Student ID Verification** – Checks whether a student registration number exists.
3. **Student Records** – Displays student names, ages, gender, courses, and registration numbers.
4. **Update Student Records** – Allows users to update student information.
5. **Marks Management** – Records student examination marks.
6. **Grade Calculation** – Automatically calculates grades based on student marks.
7. **Student Search** – Searches for students using registration numbers.
8. **Display Registered Students** – Displays all registered students and their academic information.

## 4. Project Structure

```text
Student-Management-System/
│
├── students.py
│
├── main.py
│
└── README.md
```

## 5. Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- Python Classes and Objects
- Inheritance
- Constructors (`__init__`)
- Methods
- Dictionaries
- Conditional Statements
- Loops
- Exception Handling

## 6. Installation and Setup

### Requirements

- Python 3 installed on your computer.
- A code editor such as Visual Studio Code or PyCharm.

### Steps

1. Download or clone the project repository.
2. Open the project folder in your code editor.
3. Ensure that `students.py` and `main.py` are in the same directory.
4. Open the terminal.
5. Run the application using:

```bash
python main.py
```

## 7. How to Use the Application

After running `main.py`, the system displays a menu with the following options:

| Option | Function |
|---|---|
| 1 | Register Student |
| 2 | Verify Student ID |
| 3 | Display Student Record |
| 4 | Update Student Record |
| 5 | Enter Student Marks |
| 6 | Search Registration Number |
| 7 | Display All Registered Students |
| 8 | Exit |

Select an option by entering its corresponding number.

## 8. Grading System

The application uses the following grading criteria:

| Marks | Grade |
|---|---|
| 80–100 | A |
| 70–79 | B |
| 60–69 | C |
| 50–59 | D |
| 0–49 | E |

## 9. Error Handling and Validation

The application handles several possible errors:

- Prevents duplicate registration numbers.
- Checks whether a student registration number exists.
- Prevents invalid age entries.
- Ensures marks are between 0 and 100.
- Handles invalid numerical inputs using `try` and `except`.
- Displays error messages when a student cannot be found.

## 10. Sample Student Records

The application initially contains five students:

| Name | Age | Gender | Course | Reg No. |
|---|---:|---|---|---:|
| Amina | 20 | Female | Python | 1 |
| Bravin | 19 | Male | Mobile Development | 2 |
| Cathy | 18 | Female | AI and Digital Marketing | 3 |
| Daniel | 19 | Male | Social Mobile Management | 4 |
| Ethan | 21 | Male | Generative AI | 5 |

## 11. Limitations

- Student records are stored in memory and disappear when the program closes.
- The application does not use a database.
- It does not support multiple user accounts.
- It does not generate printable student reports.

## 12. Future Improvements

- Integrate a database such as SQLite or MySQL.
- Add student login and authentication.
- Generate student report cards.
- Add attendance management.
- Develop a graphical user interface (GUI).
- Add data backup and recovery.

## 13. Conclusion

The Student Management System provides a simple way to manage student registration, personal information, and academic performance using Python.

The project demonstrates practical application of Object-Oriented Programming concepts, including classes, objects, inheritance, methods, dictionaries, loops, and exception handling.

## 14. Author

**Project:** Student Management System  
**Language:** Python  
**Project Type:** Student Management Application

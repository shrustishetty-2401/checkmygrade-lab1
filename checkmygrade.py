print("PROGRAM STARTED")

import csv
import time
import base64
from statistics import median


class Student:

    def add_student(self, email, first_name, last_name, course_id, grade, marks):

        with open("students.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([email, first_name, last_name, course_id, grade, marks])

        print("Student added successfully")


    def display_students(self):

        with open("students.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                print(row)


    def search_student(self, email):

        start = time.time()

        with open("students.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if row[0] == email:
                    print("Student Found:", row)

        end = time.time()
        print("Search time:", end - start)


    def update_student_marks(self, email, new_marks):

        rows = []

        with open("students.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if row[0] == email:
                    row[5] = new_marks

                rows.append(row)

        with open("students.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        print("Marks updated")


    def delete_student(self, email):

        rows = []

        with open("students.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if row[0] != email:
                    rows.append(row)

        with open("students.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        print("Student deleted")


    def sort_students_by_marks(self):

        students = []

        with open("students.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                students.append(row)

        if len(students) <= 1:
            print("No student data to sort")
            return

        header = students[0]
        data = students[1:]

        data.sort(key=lambda x: int(x[5]), reverse=True)

        print(header)
        print("Students sorted by marks:")

        for s in data:
            print(s)


    def average_marks(self):

        marks = []

        with open("students.csv", "r") as file:
            reader = csv.reader(file)

            next(reader)

            for row in reader:
                try:
                    marks.append(int(row[5]))
                except:
                    pass

        if len(marks) > 0:
            avg = sum(marks) / len(marks)
            print("Average marks:", avg)


    def median_marks(self):

        marks = []

        with open("students.csv", "r") as file:
            reader = csv.reader(file)

            next(reader)

            for row in reader:
                try:
                    marks.append(int(row[5]))
                except:
                    pass

        if len(marks) > 0:
            print("Median marks:", median(marks))


class Course:

    def add_course(self, cid, name, desc):

        with open("courses.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([cid, name, desc])

        print("Course added")


    def display_courses(self):

        with open("courses.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                print(row)


class Professor:

    def add_professor(self, pid, name, rank, course):

        with open("professors.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([pid, name, rank, course])

        print("Professor added")


    def display_professors(self):

        with open("professors.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                print(row)


class LoginUser:

    def encrypt_password(self, password):

        encoded = base64.b64encode(password.encode())
        return encoded.decode()


    def decrypt_password(self, password):

        decoded = base64.b64decode(password.encode())
        return decoded.decode()


    def register(self, email, password, role):

        encrypted = self.encrypt_password(password)

        with open("login.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([email, encrypted, role])

        print("User registered")


    def login(self, email, password):

        with open("login.csv", "r") as file:
            reader = csv.reader(file)

            next(reader)

            for row in reader:
                stored_password = self.decrypt_password(row[1])

                if row[0] == email and stored_password == password:
                    print("Login successful")
                    return

        print("Login failed")

if __name__ == "__main__":

    auth = LoginUser()

    print("===== Welcome to CheckMyGrade =====")
    print("1. Register")
    print("2. Login")

    option = input("Choose option: ")

    if option == "1":

        email = input("Email: ")
        password = input("Password: ")
        role = input("Role (student/professor/admin): ")

        auth.register(email, password, role)

    elif option == "2":

        email = input("Email: ")
        password = input("Password: ")

        auth.login(email, password)

    else:
        print("Invalid option")

    student = Student()

    while True:

        print("\n===== CheckMyGrade Menu =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Sort Students by Marks")
        print("7. Average Marks")
        print("8. Median Marks")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            email = input("Email: ")
            first = input("First Name: ")
            last = input("Last Name: ")
            course = input("Course ID: ")
            grade = input("Grade: ")
            marks = input("Marks: ")

            student.add_student(email, first, last, course, grade, marks)

        elif choice == "2":

            student.display_students()

        elif choice == "3":

            email = input("Enter email to search: ")
            student.search_student(email)

        elif choice == "4":

            email = input("Enter email: ")
            marks = int(input("Marks: "))
            student.update_student_marks(email, marks)

        elif choice == "5":

            email = input("Enter email to delete: ")
            student.delete_student(email)

        elif choice == "6":

            student.sort_students_by_marks()

        elif choice == "7":

            student.average_marks()

        elif choice == "8":

            student.median_marks()

        elif choice == "9":

            print("Exiting program")
            break

        else:

            print("Invalid choice")

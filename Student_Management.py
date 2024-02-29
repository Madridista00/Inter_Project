import json
import os

class Student:
    def __init__(self, name, roll_number, grade):
        self.name = str(name)
        self.roll_number = int(roll_number)
        self.grade = float(grade)

    def __str__(self):
        return f"Name: {self.name}, Roll Number: {self.roll_number}, Grade: {self.grade}"

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, name, roll_number, grade):
        if self.is_roll_number_unique(roll_number):
            student = Student(name, roll_number, grade)
            self.students.append(student)
            print("Student added successfully.")
        else:
            print("Roll number already exists. Please choose a different roll number.")

    def is_roll_number_unique(self, roll_number):
        return all(student.roll_number != roll_number for student in self.students)

    def view_all_students(self):
        if self.students:
            for student in self.students:
                print(student)
        else:
            print("No students found.")

    def search_student_by_roll_number(self, roll_number):
        found = False
        for student in self.students:
            if student.roll_number == roll_number:
                print(student)
                found = True
                break
        if not found:
            print("Student not found.")

    def update_student_grade(self, roll_number, new_grade):
        for student in self.students:
            if student.roll_number == roll_number:
                student.grade = new_grade
                print("Student grade is updated.")
                return
        print("Student not found.")

    def delete_student_by_roll_number(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                self.students.remove(student)
                print("Student deleted.")
                return
        print("Student not found.")

    def save_to_json(self, filename):
        with open(filename, "w", encoding='utf-8') as file:
            json.dump([student.__dict__ for student in self.students], file, indent=4)
        print("Data saved to JSON file.")

def display_menu():
    print("\nMenu:")
    print("1. Add a new student")
    print("2. View all students")
    print("3. Search student by roll number")
    print("4. Update student grade")
    print("5. Delete student by roll number")
    print("6. Exit\n\n")

def main():
    filename = "student.json"
    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8") as file:
            json.dump([], file)  # Create an empty JSON array
        print("Created empty student data file.")

    student_system = StudentManagementSystem()

    with open(filename, "r", encoding='utf-8') as file:
        data = json.load(file)
        for student_data in data:
            student_system.add_student(student_data["name"], student_data["roll_number"], student_data["grade"])

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student's name: ")
            while True:
                try:
                    roll_number = int(input("Enter student's roll number: "))
                    if not student_system.is_roll_number_unique(roll_number):
                        print("Roll number already exists. Please choose a different roll number.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Roll number must be a number.")

            while True:
                try:
                    grade = float(input("Enter student's grade: "))
                    break
                except ValueError:
                    print("Invalid input. Grade must be a number.")

            student_system.add_student(name, roll_number, grade)
            student_system.save_to_json(filename)

        elif choice == "2":
            student_system.view_all_students()
        elif choice == "3":
            while True:
                try:
                    roll_number = int(input("Enter student's roll number to search: "))
                    break
                except ValueError:
                    print("Invalid input. Roll number must be a number.")
            student_system.search_student_by_roll_number(roll_number)

        elif choice == "4":
            while True:
                try:
                    roll_number = int(input("Enter student's roll number to update grade: "))
                    break
                except ValueError:
                    print("Invalid input. Roll number must be a number.")
            while True:
                try:
                    new_grade = float(input("Enter student's new grade: "))
                    break
                except ValueError:
                    print("Invalid input. Grade must be a number.")
            student_system.update_student_grade(roll_number, new_grade)
            student_system.save_to_json(filename)

        elif choice == "5":
            while True:
                try:
                    roll_number = int(input("Enter student's roll number to delete: "))
                    break
                except ValueError:
                    print("Invalid input. Roll number must be a number.")
            student_system.delete_student_by_roll_number(roll_number)
            student_system.save_to_json(filename)

        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()

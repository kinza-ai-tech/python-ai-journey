import json

class StudentManager:
    def __init__(self):
        self.student = []
        self.next_id = 1

    def get_grade(self, marks):
        if marks >= 80:
            return "A"
        elif marks >= 60:
            return "B"
        elif marks >= 40:
            return "C"
        else:
            return "Fail"

    def add_student(self, name, marks):
        student = {
            "id": self.next_id,
            "name": name,
            "marks": marks,
            "grade": self.get_grade(marks)
        }
        self.student.append(student)
        self.next_id += 1
        print(f"Student '{name}' added with ID {student['id']}")

    def highest_marks(self):
        if len(self.student) == 0:
            print("No students yet.")
            return
        highest = self.student[0]
        for s in self.student:
            if s['marks'] > highest['marks']:
                highest = s
        print(f"\nHighest marks student:")
        print(f"Name: {highest['name']} | Marks: {highest['marks']} | Grade: {highest['grade']}")

    def failed_students(self):
        found = False
        for s in self.student:
            if s['marks'] < 50:
                found = True
                print(f"ID: {s['id']} | Name: {s['name']} | Marks: {s['marks']} | Grade: {s['grade']}")
        if not found:
            print("No failed students.")

    def view_students(self):
        if len(self.student) == 0:
            print("No students yet.")
        else:
            print("\n--- All Students ---")
            for s in self.student:
                print(f"ID: {s['id']} | Name: {s['name']} | Marks: {s['marks']} | Grade: {s['grade']}")

    def save_data(self):
        with open("students.json", "w") as f:
            json.dump(self.student, f)
        print("Data saved!")

    def load_data(self):
        try:
            with open("students.json", "r") as f:
                self.student = json.load(f)
            if len(self.student) > 0:
                self.next_id = self.student[-1]["id"] + 1
        except FileNotFoundError:
            self.student = []


manager = StudentManager()
manager.load_data()

while True:
    print("\n===== Student Grade Manager =====")
    print("1. Add student")
    print("2. View all students")
    print("3. Find highest marks")
    print("4. Find failed students")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        manager.add_student(name, marks)
    elif choice == "2":
        manager.view_students()
    elif choice == "3":
        manager.highest_marks()
    elif choice == "4":
        manager.failed_students()
    elif choice == "5":
        manager.save_data()
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1-5.")
"""
Student Class — Week 4 OOP Practice
Demonstrates: classes, __init__, methods, self keyword
"""

class Student:
    def __init__(self, name, age, city, marks):
        self.name = name
        self.age = age
        self.city = city
        self.marks = marks

    def get_grade(self):
        """Calculate and return grade based on marks."""
        if self.marks >= 80:
            return "A"
        elif self.marks >= 60:
            return "B"
        elif self.marks >= 40:
            return "C"
        else:
            return "Fail"

    def introduce(self):
        """Print full student information."""
        grade = self.get_grade()
        print(f"Name:   {self.name}")
        print(f"Age:    {self.age}")
        print(f"City:   {self.city}")
        print(f"Marks:  {self.marks}")
        print(f"Grade:  {grade}")
        print("-" * 30)


# --- Test ---
if __name__ == "__main__":
    student1 = Student("Ali", 17, "Lahore", 85)
    student2 = Student("Ahmad", 16, "Karachi", 75)
    student3 = Student("Sara", 18, "Islamabad", 90)
    student4 = Student("Kinza", 21, "Lahore", 95)

    student1.introduce()
    student2.introduce()
    student3.introduce()
    student4.introduce()
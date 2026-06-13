"""
Function Practice Exercises
Covers: functions with no parameters, parameters, return values,
        connecting multiple functions together
"""

# ---------- Exercise 1: Function with no parameters ----------
def show_welcome():
    print("Welcome to my program")
    print("Please follow the instructions")
    print("Enjoy!")


# ---------- Exercise 2: Function with parameters ----------
def introduce_student(name, city):
    print(f"Hi I am {name} from {city}")


# ---------- Exercise 3: Function with return value ----------
def find_bigger(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "Both are equal"


# ---------- Exercise 4: Two functions connected ----------
def get_total(numbers):
    """Adds up all numbers in a list and returns the total."""
    total = 0
    for number in numbers:
        total = total + number
    return total


def show_result(name, total):
    print(f"{name} spent Rs.{total} this month")


# ---------- Exercise 5: Three functions connected ----------
def ask_marks():
    """Asks the user for marks and returns it as a number."""
    marks = int(input("Enter your marks: "))
    return marks


def get_grade(marks):
    """Returns a letter grade based on marks."""
    if marks >= 80:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "Fail"


def show_grade_result(marks, grade):
    print(f"You scored {marks}")
    print(f"Your grade is {grade}")


# ---------- Run Everything ----------
if __name__ == "__main__":
    print("=== Exercise 1 ===")
    show_welcome()

    print("\n=== Exercise 2 ===")
    introduce_student("Ahmad", "Lahore")
    introduce_student("Ali", "Multan")
    introduce_student("Sara", "Karachi")

    print("\n=== Exercise 3 ===")
    print("Bigger of 50, 30:", find_bigger(50, 30))
    print("Bigger of 10, 20:", find_bigger(10, 20))
    print("Bigger of 10, 10:", find_bigger(10, 10))

    print("\n=== Exercise 4 ===")
    expenses = [100, 200, 300, 400, 450]
    total_spent = get_total(expenses)
    show_result("Ali", total_spent)

    print("\n=== Exercise 5 ===")
    marks = ask_marks()
    grade = get_grade(marks)
    show_grade_result(marks, grade)
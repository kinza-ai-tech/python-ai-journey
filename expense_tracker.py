# Expense Tracker
# I built this to practice classes, JSON and datetime module.
# Each expense is saved automatically after adding.
# I learned how json.dump saves data and json.load brings it back.

import json
from datetime import date


class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.next_id = 1

    def add_expense(self, category, amount, description):
        # create a new expense dictionary with auto date
        expense = {
            "id": self.next_id,
            "category": category,
            "amount": amount,
            "description": description,
            "date": str(date.today())
        }
        self.expenses.append(expense)
        self.next_id += 1
        self.save_data()   # save automatically after each add
        print(f"Expense added! Category: {category} | Amount: Rs.{amount}")

    def view_expenses(self):
        # show all expenses
        if len(self.expenses) == 0:
            print("No expenses yet.")
        else:
            print("\n--- All Expenses ---")
            for e in self.expenses:
                print(f"ID: {e['id']} | Category: {e['category']} | Amount: Rs.{e['amount']} | Description: {e['description']} | Date: {e['date']}")

    def view_total(self):
        # add up all amounts and show total
        if len(self.expenses) == 0:
            print("No expenses yet.")
            return
        total = sum([e['amount'] for e in self.expenses])
        print(f"\nTotal spending: Rs.{total}")

    def view_by_category(self):
        # show only expenses from one category
        category = input("Enter category (food/transport/rent/other): ")
        total = 0
        found = False
        for e in self.expenses:
            if e['category'] == category:
                found = True
                total += e['amount']
                print(f"ID: {e['id']} | Amount: Rs.{e['amount']} | Description: {e['description']} | Date: {e['date']}")
        if not found:
            print(f"No expenses found for '{category}'")
        else:
            print(f"Total spent on {category}: Rs.{total}")

    def save_data(self):
        # save all expenses to JSON file permanently
        with open("expenses.json", "w") as f:
            json.dump(self.expenses, f, indent=4)

    def load_data(self):
        # load expenses from file when program starts
        try:
            with open("expenses.json", "r") as f:
                self.expenses = json.load(f)
            if len(self.expenses) > 0:
                self.next_id = self.expenses[-1]["id"] + 1
        except FileNotFoundError:
            # if no file exists yet, start with empty list
            self.expenses = []


# --- Main Program ---
tracker = ExpenseTracker()
tracker.load_data()

while True:
    print("\n====Expense Tracker====")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. View total spending")
    print("4. View spending by category")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        category = input("Category (food/transport/rent/other): ")
        amount = int(input("Amount (Rs): "))
        description = input("Description: ")
        tracker.add_expense(category, amount, description)
    elif choice == "2":
        tracker.view_expenses()
    elif choice == "3":
        tracker.view_total()
    elif choice == "4":
        tracker.view_by_category()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Enter 1-5.")
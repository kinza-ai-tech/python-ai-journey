"""
BankAccount Class — Week 4 OOP Practice
Demonstrates: classes, data changing over time,
              conditional logic inside methods
"""

class BankAccount:
    def __init__(self, owner_name, balance):
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        """Add money to account."""
        self.balance += amount
        print(f" Deposited Rs.{amount}")
        print(f"   New balance: Rs.{self.balance}")
        print("-" * 30)

    def withdraw(self, amount):
        """Remove money from account if sufficient funds exist."""
        if amount > self.balance:
            print(f"   Insufficient funds!")
            print(f"   Requested: Rs.{amount}")
            print(f"   Available: Rs.{self.balance}")
        else:
            self.balance -= amount
            print(f" Withdrawn Rs.{amount}")
            print(f"   New balance: Rs.{self.balance}")
        print("-" * 30)

    def show_balance(self):
        """Display account summary."""
        print(f" Account Owner: {self.owner_name}")
        print(f" Current Balance: Rs.{self.balance}")
        print("-" * 30)


# --- Test ---
if __name__ == "__main__":
    account1 = BankAccount("Kinza", 5000)
    account1.show_balance()
    account1.deposit(2000)
    account1.withdraw(1000)
    account1.withdraw(10000)
    account1.show_balance()
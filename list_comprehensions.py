# List Comprehensions Practice
# I learned how to write shorter, cleaner loops using list comprehensions.
# Formula: [expression for item in list if condition]

# --- Exercise 1: Basic ---
# Get square of each number
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = [n * n for n in numbers]
print("Squares:", squares)

# --- Exercise 2: With Function ---
# Get length of each word
words = ["apple", "banana", "mango", "cherry"]
lengths = [len(word) for word in words]
print("Lengths:", lengths)

# --- Exercise 3: With Condition ---
# Get only even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [n for n in numbers if n % 2 == 0]
print("Even numbers:", evens)

# --- Exercise 4: Function + Condition ---
# Get only fruits with more than 5 letters
fruits = ["apple", "banana", "mango", "cherry", "fig"]
long_fruits = [fruit for fruit in fruits if len(fruit) > 5]
print("Long fruits:", long_fruits)

# --- Exercise 5: Real Use Case ---
# Working with dictionaries (like expense tracker)
expenses = [
    {"category": "food", "amount": 500},
    {"category": "transport", "amount": 200},
    {"category": "food", "amount": 300},
    {"category": "rent", "amount": 8000}
]

# Get all amounts
amounts = [e['amount'] for e in expenses]
print("All amounts:", amounts)

# Get only food amounts
food_only = [e['amount'] for e in expenses if e['category'] == 'food']
print("Food amounts:", food_only)

# Bonus: total using list comprehension
total = sum([e['amount'] for e in expenses])
print("Total spending: Rs.", total)
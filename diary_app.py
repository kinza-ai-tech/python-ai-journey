"""
Diary App
A simple command-line app to write and read diary entries.
Demonstrates: while loops, file handling (append/read), error handling
"""

while True:
    print("\n1. Write a new entry")
    print("2. Read all entries")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        entry = input("Write your entry: ")
        with open("entry.txt", "a") as f:
            f.write(entry + "\n")
        print("Entry saved!")

    elif choice == "2":
        try:
            with open("entry.txt", "r") as f:
                content = f.read()
            print("\nYour diary entries:")
            print(content)
        except FileNotFoundError:
            print("No entries yet. Write one first!")

    elif choice == "3":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice, please enter 1, 2, or 3.")
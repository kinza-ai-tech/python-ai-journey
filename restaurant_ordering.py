"""
Restaurant Ordering System
A command-line app that lets customers view a menu, place orders,
get a random dish suggestion, and receive a bill saved to a file.

Concepts used: dictionaries, functions, lists, while loops,
file handling, datetime, random module
"""

import random
from datetime import datetime

# --- Data ---
menu = {
    "food": {"chicken karahi": 500, "fried rice": 400, "biryani": 500, "beef karahi": 800},
    "drinks": {"pepsi": 100, "coke": 100, "water": 50}
}

order_list = []


# --- Functions ---
def show_menu():
    print("\n📋 MENU")
    print("---- Food ----")
    for item, price in menu["food"].items():
        print(f"{item} = {price} Rs")
    print("---- Drinks ----")
    for item, price in menu["drinks"].items():
        print(f"{item} = {price} Rs")


def take_order():
    show_menu()
    while True:
        choice = input("\nWhat would you like to order? (type 'done' when finished): ").lower()
        if choice == "done":
            break
        if choice in menu["food"]:
            order_list.append((choice, menu["food"][choice]))
            print(f"✅ Added {choice} - {menu['food'][choice]} Rs")
        elif choice in menu["drinks"]:
            order_list.append((choice, menu["drinks"][choice]))
            print(f"✅ Added {choice} - {menu['drinks'][choice]} Rs")
        else:
            print("❌ Sorry, item not available. Please try again.")


def show_bill():
    total = 0
    for item, price in order_list:
        total += price

    print("\n🧾 BILL")
    for item, price in order_list:
        print(f"- {item} = {price} Rs")
    print(f"Total = {total} Rs")
    print(f"Date/Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    with open("orders.txt", "a") as file:
        file.write(f"Order at {datetime.now()}:\n")
        for item, price in order_list:
            file.write(f"- {item}: {price} Rs\n")
        file.write(f"Total: {total} Rs\n\n")


def suggest_random_food():
    suggestion = random.choice(list(menu["food"].keys()))
    print(f"🤔 Can't decide? How about trying: {suggestion}!")


# --- Main Program ---
if __name__ == "__main__":
    print("Assalam o Alaikum! Welcome to our Restaurant 🥰")

    while True:
        print("\nOptions: 'menu' | 'order' | 'suggest' | 'exit'")
        choice = input("Enter your choice: ").lower()

        if choice == "menu":
            show_menu()
        elif choice == "order":
            take_order()
            show_bill()
            order_list.clear()
        elif choice == "suggest":
            suggest_random_food()
        elif choice == "exit":
            print("🙏 Thank you for visiting! Have a nice day.")
            break
        else:
            print("❌ Invalid choice, please try again.")
"""lundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlundlund"""
import json
import os
from datetime import datetime

DATA_FILE = "expenses.json"


def load_expenses():
    #Load expenses from the JSON file. If file doesn't exist, return empty list.
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return []
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_expenses(expenses):
    #Save the list of expenses to the JSON file.
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)


def add_expense(expenses):
    #Add a new expense entry.
    print("\n--- Add New Expense ---")

    # Date input
    date_str = input("Enter date (YYYY-MM-DD) or leave blank for today: ").strip()
    if date_str == "":
        date_str = datetime.today().strftime("%Y-%m-%d")
    else:
        # Basic validation
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format! Using today's date instead.")
            date_str = datetime.today().strftime("%Y-%m-%d")

    # Category input
    category = input("Enter category (food, travel, shopping, etc.): ").strip()
    if category == "":
        category = "other"

    # Amount input
    while True:
        amount_str = input("Enter amount (INR): ").strip()
        try:
            amount = float(amount_str)
            if amount <= 0:
                print("Amount must be positive!")
                continue
            break
        except ValueError:
            print("Invalid amount! Please enter a number.")

    description = input("Enter description (optional): ").strip()

    # Create expense record
    expense = {
        "date": date_str,
        "category": category,
        "amount": amount,
        "description": description
    }

    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")


def view_expenses(expenses):
    #Display all expenses
    print("\n--- All Expenses ---")
    if not expenses:
        print("No expenses recorded yet.")
        return

    total = 0
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['date']} | {exp['category']} | ₹{exp['amount']:.2f} | {exp['description']}")
        total += exp["amount"]

    print("-" * 40)
    print(f"Total expenses: ₹{total:.2f}")


def view_summary_by_category(expenses):
    #Show total spent per category
    print("\n--- Summary by Category ---")
    if not expenses:
        print("No expenses recorded yet.")
        return

    summary = {}
    for exp in expenses:
        cat = exp["category"]
        summary[cat] = summary.get(cat, 0) + exp["amount"]

    for cat, amt in summary.items():
        print(f"{cat}: ₹{amt:.2f}")


def view_summary_by_date(expenses):
    #Show total spent per date
    print("\n--- Summary by Date ---")
    if not expenses:
        print("No expenses recorded yet.")
        return

    summary = {}
    for exp in expenses:
        d = exp["date"]
        summary[d] = summary.get(d, 0) + exp["amount"]

    for d, amt in summary.items():
        print(f"{d}: ₹{amt:.2f}")


def main_menu():
    #Main menu loop
    expenses = load_expenses()

    while True:
        print("\n==============================")
        print("      EXPENSE TRACKER")
        print("==============================")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Summary by Category")
        print("4. View Summary by Date")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_summary_by_category(expenses)
        elif choice == "4":
            view_summary_by_date(expenses)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main_menu()

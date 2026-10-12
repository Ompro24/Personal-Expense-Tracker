

import json
from datetime import datetime

FILE_NAME = "expenses.json"


def load_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            expenses = json.load(file)
            if not isinstance(expenses, list): #checks whether the loaded files data is in list or not 
                print("Invalid file data. Starting with an empty list.")
                return []
            return expenses
    except FileNotFoundError:
        return []
    except (json.JSONDecodeError, OSError):
        print("Unable to read the file. Starting with an empty list.")
        return []



def save_expenses(expenses):#to save expenses to JSON file
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(expenses, file, indent=4)
    except OSError:
        print("Error: Unable to save expenses.") 



def add_expense(expenses):# Add a new expense
    expense_id = input("Enter expense ID: ").strip()#strip removes the space before and after the input data

    if not expense_id:
        print("Expense ID cannot be empty.")
        return

    for expense in expenses:
        if expense["id"] == expense_id:
            print("Duplicate expense ID. Try another ID.")
            return #to stop the function so the duplicate expense is not added

    category = input("Enter category: ").strip()

    if not category:
        print("Category cannot be empty.")
        return

    try:
        amount = float(input("Enter amount: "))

        if amount < 0:
            print("Amount cannot be negative.")
            return

        date = input("Enter date (YYYY-MM-DD): ")
        datetime.strptime(date, "%Y-%m-%d")

        description = input("Enter description: ")

        expense = {
            "id": expense_id,
            "category": category,
            "amount": amount,
            "date": date,
            "description": description
        }

        expenses.append(expense)
        save_expenses(expenses)
        print("Expense added successfully!")

    except ValueError:
        print("Invalid amount or date. Please try again.")



def view_expenses(expenses): #to display all expenses
    if len(expenses) == 0:
        print("No expenses recorded.")
        return

    for expense in expenses:
        print("\nExpense ID:", expense["id"])
        print("Category:", expense["category"])
        print("Amount: Rs.", expense["amount"])
        print("Date:", expense["date"])
        print("Description:", expense["description"])


# Search expenses by category
def search_expenses(expenses):
    category = input("Enter category to search: ").strip().lower()
    found = False

    for expense in expenses:
        if expense["category"].lower() == category:
            print(expense)
            found = True

    if not found:
        print("No expenses found in this category.")


# Calculate total spending
def calculate_total(expenses):
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("Total amount spent: Rs.", round(total, 2))


# Calculate spending by category
def category_analysis(expenses):
    if len(expenses) == 0:
        print("No expenses available.")
        return

    totals = {}

    for expense in expenses:
        category = expense["category"]

        if category in totals:
            totals[category] = totals[category] + expense["amount"]
        else:
            totals[category] = expense["amount"]

    print("\nCategory-wise Spending:")

    for category in totals:
        print(category, ": Rs.", round(totals[category], 2))


# Find the highest expense
def highest_expense(expenses):
    if len(expenses) == 0:
        print("No expenses available.")
        return

    highest = expenses[0]

    for expense in expenses:
        if expense["amount"] > highest["amount"]:
            highest = expense

    print("\nHighest Expense:")
    print("Category:", highest["category"])
    print("Amount: Rs.", highest["amount"])
    print("Date:", highest["date"])
    print("Description:", highest["description"])


# Main menu
def main():
    expenses = load_expenses()

    while True:
        print("\n===== PERSONAL EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expenses by Category")
        print("4. Calculate Total Spending")
        print("5. Category-wise Analysis")
        print("6. Highest Expense")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            search_expenses(expenses)

        elif choice == "4":
            calculate_total(expenses)

        elif choice == "5":
            category_analysis(expenses)

        elif choice == "6":
            highest_expense(expenses)

        elif choice == "7":
            save_expenses(expenses)
            print("Thank you for using the Expense Tracker!")
            break

        else:
            print("Invalid choice. Please enter 1 to 7.")


main()
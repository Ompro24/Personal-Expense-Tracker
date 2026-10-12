import json
from datetime import datetime

expenses = []


try: #to load the file
    with open("expenses.json", "r") as file:
        expenses = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    expenses = []



def add_expense(): 
    expense_id = input("Enter expense ID: ")

    for e in expenses:
        if e["id"] == expense_id:
            print("ID already exists!")
            return

    category = input("Enter category: ")
    amount = float(input("Enter amount: "))

    if amount < 0:
        print("Amount cannot be negative!")
        return

    date = input("Enter date (YYYY-MM-DD): ")

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date!")
        return

    description = input("Enter description: ")

    expense = {
        "id": expense_id,
        "category": category,
        "amount": amount,
        "date": date,
        "description": description
    }

    expenses.append(expense)

    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

    print("Expense added!")



def view_expenses():
    for e in expenses:
        print(e)



def search_expenses():
    category = input("Enter category: ").lower()

    for e in expenses:
        if e["category"].lower() == category:
            print(e)



def calculate_total():
    total = 0

    for e in expenses:
        total = total + e["amount"]

    print("Total spending:", total)



def category_analysis(): 
    totals = {}

    for e in expenses:
        category = e["category"]

        if category in totals:
            totals[category] = totals[category] + e["amount"]
        else:
            totals[category] = e["amount"]

    print(totals)



def highest_expense():
    if len(expenses) == 0:
        print("No expenses available!")
        return

    highest = expenses[0]

    for e in expenses:
        if e["amount"] > highest["amount"]:
            highest = e

    print("Highest expense:", highest)


while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Calculate Total")
    print("5. Category Analysis")
    print("6. Highest Expense")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        try:
            add_expense()
        except ValueError:
            print("Please enter a valid amount!")

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        search_expenses()

    elif choice == "4":
        calculate_total()

    elif choice == "5":
        category_analysis()

    elif choice == "6":
        highest_expense()

    elif choice == "7":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")


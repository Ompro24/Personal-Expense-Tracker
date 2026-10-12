# Personal Expense Tracker

## Project Description

The Personal Expense Tracker is a menu-driven Python application that helps users record and manage personal expenses. Each record contains an expense ID, category, amount, date, and description. The application can display expenses, search by category, calculate total spending, analyse category-wise spending, and identify the highest expense.

## Features

- Add a new expense
- View all recorded expenses
- Search expenses by category
- Calculate total spending
- Display category-wise spending
- Find the highest expense
- Save expense records to a JSON file
- Load saved records when the program starts
- Validate expense IDs, amounts, and dates
- Handle a missing JSON file and certain file or JSON errors

## Technologies Used

- Python 3
- Built-in `json` module
- Built-in `datetime` module

No database or third-party libraries are required.

## Project Files

```text
PersonalExpenseTracker/
├── Expense.py
├── expenses.json
├── README.md
└── screenshots/
    ├── add_expense.png
    ├── view_expenses.png
    ├── category_analysis.png
    └── highest_expense.png
```

The screenshot filenames above are examples. Save your own screenshots of the program in the `screenshots` folder.

## How to Run

1. Install Python 3 if it is not already installed.
2. Keep `Expense.py` and `expenses.json` in the same folder.
3. Open the folder in VS Code.
4. Open the integrated terminal.
5. Run:

   ```bash
   python3 Expense.py
   ```

   If you use a specific Python environment, run the script with that environment's Python interpreter.

6. Select an option from the menu and follow the prompts.

## Sample Expense Records Used

The following records were entered during the demonstrated run:

| Expense ID | Category | Amount | Date | Description |
|---|---|---:|---|---|
| 101 | Food | ₹2,000 | 2026-10-12 | Expense for Lunch Food at College |
| 102 | Food | ₹4,000 | 2026-03-20 | Expense for General Party |
| 103 | Gym | ₹10,000 | 2026-09-20 | Annual Gym Fee |
| 104 | Transport | ₹200 | 2026-10-09 | Travelling expense Nominal |
| 105 | Shopping | ₹5,000 | 2026-10-04 | Clothes |

**Total spending for these records: ₹21,200**

**Highest expense: Annual Gym Fee — ₹10,000**

Food category spending is ₹6,000. Transport spending is ₹200, Gym spending is ₹10,000, and Shopping spending is ₹5,000.

Note: The terminal transcript shows these five records being added successfully across two program runs. Confirm that `expenses.json` contains all five records before taking screenshots or submitting the sample data file.

## Assignment Questions and Answers

### 1. Why did you use a dictionary for each expense?

I used a dictionary because each expense contains related details, such as the expense ID, category, amount, date, and description. A dictionary stores these details as key-value pairs, making each record easy to organise and access.

### 2. Why is JSON useful for storing records?

JSON stores data in a readable text format. Python can write the expense list to a JSON file and load it again when the program starts. This allows expense records to remain available after the program closes.

### 3. What happens if the JSON file is missing?

The `load_expenses()` function handles `FileNotFoundError` and returns an empty list. The program can therefore start without an existing expense file. The file is created when the program saves expenses.

### 4. How did you prevent duplicate expense IDs?

Before adding an expense, the `add_expense()` function loops through the existing expense records and compares their IDs with the new ID. If a match is found, it displays a duplicate ID message and returns without adding the new record.

### 5. How would you modify the application to support multiple users?

I would add a user ID for each user and associate every expense with that user. The program could then show only the expenses belonging to the logged-in user. A login system could be added to identify users.

## Testing

Run the following tests and record the actual result before marking each one as passed.

| Test | Input or action | Expected result | Status |
|---|---|---|---|
| 1 | Add expense ID `101` with valid details | Expense is added successfully | Passed in the demonstrated run |
| 2 | Add an expense using an existing ID | Duplicate ID is rejected | Not tested in the transcript |
| 3 | Enter a negative amount | Negative amount is rejected | Not tested in the transcript |
| 4 | Enter an invalid date such as `2026-15-40` | Invalid date message is displayed | Not tested in the transcript |
| 5 | Enter letters instead of an amount, such as `abc` | The input error is handled | Not tested in the transcript |
| 6 | Start without an `expenses.json` file | Program starts with an empty list | Not tested in the transcript |
| 7 | Add the five records listed above and calculate the total | Total is ₹21,200 | Total option not shown in the transcript |

The program handles malformed JSON syntax, but its current type check does not validate every field in every loaded expense record.

## Screenshots

Include at least four screenshots showing your own program running. Recommended screenshots are:

1. Adding an expense successfully.
2. Viewing all recorded expenses.
3. Searching by category or displaying category-wise analysis.
4. Displaying the highest expense.

You may also include a screenshot of the total spending and the JSON file.

## Conclusion

The Personal Expense Tracker demonstrates the use of Python functions, lists, dictionaries, loops, conditional statements, exception handling, and JSON file handling to manage personal expense records.

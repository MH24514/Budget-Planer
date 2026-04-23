# Budget Planner

My project is a small budget planner that runs in the terminal. You can add your income and expenses, put them in categories and then check how much money you actually have left at the end.


# What it can do

- Add new entries (income or expense) with a category and short description
- Show all entries in a table
- Delete an entry if you made a mistake
- Show a summary: total income, total expenses, and the balance
- Group expenses by category so you can see where your money goes
- Save everything to a CSV file so the data is still there next time you open the program

# Files in this project

- `main.py` - starts the program and shows the menu
- `entries.py` - handles adding, showing and deleting entries
- `analysis.py` - does the calculations (summary, by category)
- `storage.py` - saves and loads the CSV file
- `data.csv` - this one is created automatically once you add entries

# How to run it

You just need Python 3 installed (I used Python 3.11 but anything from 3.8 should work). No extra libraries, everything is standard Python.

1. Download the files or clone the repo
2. Open a terminal in the project folder
3. Run:

```
python main.py
```

4. Then just follow the menu, type a number from 1 to 6 and press Enter.

Important: to save your data you have to exit with option 6. If you just close the window your new entries won't be saved.

# Example

When you start the program it looks like this:

```
--- Personal Budget Planner ---
1. Add new entry
2. Show all entries
3. Delete an entry
4. Show summary (income, expenses, balance)
5. Show expenses by category
6. Save and quit
-------------------------------
Please choose an option (1-6):
```

If you pick 1 it asks you for the type (income or expense), the amount, a category and a short description. The date is added automatically (today's date).

# About the CSV file

All entries end up in `data.csv` in the same folder. You can open it with Excel if you want. The columns are: date, type, category, description, amount.

# Notes

- The program checks if you type something invalid (like letters instead of a number for the amount) and just asks again instead of crashing.
- Could be extended later with things like a monthly budget limit or charts with matplotlib, but for now I focused on getting the basics working.

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

You just need Python 3 installed. No extra libraries, everything is standard Python.

1. Download the files or clone the repository
2. Open a terminal in the project folder
3. Run: python main.py
4. Then just follow the menu, type a number from 1 to 6 and press Enter.

To save data you have to exit with option 6. If you just close the window your new entries won't be saved.

# How the code works

I split the program into four files so each one has a clear job. This made it easier to work on one part at a time without breaking the rest.

**main.py** is the starting point. It shows the menu in a loop and calls the right function depending on what the user chooses. It also loads the data when the program starts and saves it at the end. I kept this file short on purpose, it's basically just the "controller" that connects everything.

**entries.py** is where the actual entries are managed. The `add_entry` function asks the user for type, amount, category and description, checks that the input makes sense (e.g. the amount has to be a real number) and then adds a new entry to the list. I used a dictionary for each entry because it's easy to read and you can just access things like `entry["amount"]`. The `show_entries` function prints everything in a table using Python's f-string formatting with fixed column widths. The `delete_entry` function shows all entries, asks which one to remove and handles invalid input.

**analysis.py** does the math. The `calculate_totals` function loops through all entries and sums up income and expenses separately, then returns income, expenses and balance. I split this out into its own function so `show_summary` stays clean. The `show_by_category` function was a bit trickier. I built a dictionary where the key is the category name and the value is the total spent in that category, then sorted it from highest to lowest with `sorted()` and a lambda.

**storage.py** handles reading and writing the CSV file. I used Python's built-in `csv` module with `DictReader` and `DictWriter` because the entries are already dictionaries, so this fits naturally. The `load_data` function checks first if the file exists (with `os.path.exists`), otherwise it would crash on the first run when there is no file yet. Amounts get saved as strings in CSV so I convert them back to float when loading.

# Example

When you start the program it looks like this:

Personal Budget Planner
1. Add new entry
2. Show all entries
3. Delete an entry
4. Show summary (income, expenses, balance)
5. Show expenses by category
6. Save and quit
Please choose an option (1-6):

If you pick 1 it asks you for the type (income or expense), the amount, a category and a short description. The date is added automatically (today's date).

# About the CSV file

All entries end up in `data.csv` in the same folder. You can open it with Excel if you want. The columns are: date, type, category, description, amount.

# Notes

- The program checks if you type something invalid (like letters instead of a number for the amount) and just asks again instead of crashing.

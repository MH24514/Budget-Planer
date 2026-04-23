# entries.py
# This file contains everything that has to do with single entries:
# adding a new one, showing all of them, and deleting one.
# Each entry is stored as a dictionary with date, type, category, description and amount.

from datetime import datetime


def add_entry(entries):
    """Ask the user for details and add a new entry to the list."""
    print("\n--- Add New Entry ---")

# First question: is it income or expense?
# We convert to lowercase so "Income", "INCOME" and "income" all work.
    entry_type = input("Type (income/expense): ").strip().lower()
    if entry_type not in ("income", "expense"):
        print("Invalid type. Entry was not added.")
        return entries

# Now ask for the amount. This is tricky because the user could type letters instead of a number, so we use try/except to catch that.
    amount_input = input("Amount: ").strip()
    try:
        amount = float(amount_input)
    except ValueError:
# If float() fails, it means the input wasn't a valid number.
        print("Invalid amount. Entry was not added.")
        return entries

# A negative or zero amount doesn't make sense for a budget entry.
    if amount <= 0:
        print("Amount must be greater than zero. Entry was not added.")
        return entries

# Category and description are just strings.
# If the user leaves the category empty, it gives it a default name.
    category = input("Category (e.g. Food, Rent, Salary): ").strip()
    if category == "":
        category = "Uncategorized"

    description = input("Short description: ").strip()

# Use today's date automatically. The user doesn't have to type it.
# strftime formats the date as "2026-04-15" (year-month-day).
    date = datetime.now().strftime("%Y-%m-%d")

# Build the entry as a dictionary. I used a dict instead of a tuple or list because it's much more readable: entry["amount"] is clearer than entry[4].
    new_entry = {
        "date": date,
        "type": entry_type,
        "category": category,
        "description": description,
        "amount": amount,
    }

# Add the new entry to the end of the list and return the updated list.
    entries.append(new_entry)
    print("Entry added successfully.")
    return entries


def show_entries(entries):
    """Display all entries in a readable table."""
# If there is nothing to show, say so and stop.  
    if len(entries) == 0:
        print("\nNo entries to display.")
        return

# Print the table header.
# The :<4 means "left-align in a column that is 4 characters wide".
# This way all the columns line up nicely under each other.
    print("\n--- All Entries ---")
    print(f"{'No.':<4}{'Date':<12}{'Type':<10}{'Category':<15}{'Amount':<10}{'Description'}")
    print("-" * 70)

# enumerate gives us both the index (starting at 1) and the entry, so we can number the rows for the user.
    for i, entry in enumerate(entries, start=1):
        print(f"{i:<4}{entry['date']:<12}{entry['type']:<10}"
              f"{entry['category']:<15}{entry['amount']:<10.2f}{entry['description']}")


def delete_entry(entries):
    """Let the user delete an entry by its number."""
# Can't delete from an empty list, so it checks it first.
    if len(entries) == 0:
        print("\nThere are no entries to delete.")
        return entries

# First show the list so the user can see the numbers.
    show_entries(entries)
    choice = input("Enter the number of the entry to delete (or 'c' to cancel): ").strip()

# Give the user an easy way out if they change their mind.
    if choice.lower() == "c":
        print("Deletion cancelled.")
        return entries

# Convert the input to an integer. If that fails, the user typed nonsense.
    try:
        index = int(choice) - 1
    except ValueError:
        print("Invalid input. No entry was deleted.")
        return entries

# Check that the number is actually in range.
    if index < 0 or index >= len(entries):
        print("Number out of range. No entry was deleted.")
        return entries

# pop() removes the entry at the given position and returns it, which is handy because we can show the user what was deleted.
    removed = entries.pop(index)
    print(f"Removed entry: {removed['description']} ({removed['amount']:.2f})")
    return entries

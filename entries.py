# entries.py
# Functions to add, display and delete budget entries.

from datetime import datetime


def add_entry(entries):
    """Ask the user for details and add a new entry to the list."""
    print("\n--- Add New Entry ---")

    # Ask whether it is income or expense
    entry_type = input("Type (income/expense): ").strip().lower()
    if entry_type not in ("income", "expense"):
        print("Invalid type. Entry was not added.")
        return entries

    # Ask for the amount and check that it is a number
    amount_input = input("Amount: ").strip()
    try:
        amount = float(amount_input)
    except ValueError:
        print("Invalid amount. Entry was not added.")
        return entries

    if amount <= 0:
        print("Amount must be greater than zero. Entry was not added.")
        return entries

    category = input("Category (e.g. Food, Rent, Salary): ").strip()
    if category == "":
        category = "Uncategorized"

    description = input("Short description: ").strip()

    # Use today's date automatically
    date = datetime.now().strftime("%Y-%m-%d")

    new_entry = {
        "date": date,
        "type": entry_type,
        "category": category,
        "description": description,
        "amount": amount,
    }

    entries.append(new_entry)
    print("Entry added successfully.")
    return entries


def show_entries(entries):
    """Display all entries in a readable table."""
    if len(entries) == 0:
        print("\nNo entries to display.")
        return

    print("\n--- All Entries ---")
    print(f"{'No.':<4}{'Date':<12}{'Type':<10}{'Category':<15}{'Amount':<10}{'Description'}")
    print("-" * 70)

    for i, entry in enumerate(entries, start=1):
        print(f"{i:<4}{entry['date']:<12}{entry['type']:<10}"
              f"{entry['category']:<15}{entry['amount']:<10.2f}{entry['description']}")


def delete_entry(entries):
    """Let the user delete an entry by its number."""
    if len(entries) == 0:
        print("\nThere are no entries to delete.")
        return entries

    show_entries(entries)
    choice = input("Enter the number of the entry to delete (or 'c' to cancel): ").strip()

    if choice.lower() == "c":
        print("Deletion cancelled.")
        return entries

    try:
        index = int(choice) - 1
    except ValueError:
        print("Invalid input. No entry was deleted.")
        return entries

    if index < 0 or index >= len(entries):
        print("Number out of range. No entry was deleted.")
        return entries

    removed = entries.pop(index)
    print(f"Removed entry: {removed['description']} ({removed['amount']:.2f})")
    return entries

# main.py
# This is the starting point of the program.
# It loads the saved data, shows the menu, and calls the right function depending on what the user chooses.

from entries import add_entry, show_entries, delete_entry
from analysis import show_summary, show_by_category
from storage import load_data, save_data

# Name of the file where all entries are saved.
# I put it as a constant at the top so it's easy to change later.
DATA_FILE = "data.csv"


def print_menu():
    """Display the main menu options to the user."""
    print("\n--- Personal Budget Planner ---")
    print("1. Add new entry")
    print("2. Show all entries")
    print("3. Delete an entry")
    print("4. Show summary (income, expenses, balance)")
    print("5. Show expenses by category")
    print("6. Save and quit")
    print("-------------------------------")


def main():
    """Main loop of the program."""
# First thing we do: try to load existing entries from the CSV file.
# If the file doesn't exist yet (first time running), we just get an empty list.
    entries = load_data(DATA_FILE)
    print(f"Loaded {len(entries)} entries from {DATA_FILE}.")
 
# This loop keeps running until the user quits.
# Each time, we show the menu and wait for their choice.
    while True:
        print_menu()
        choice = input("Please choose an option (1-6): ").strip()

# Depending on the choice, call the right function.
# We pass the entries list around and get it back updated,
# so we never use global variables (guidelines said no globals).
        if choice == "1":
            entries = add_entry(entries)
        elif choice == "2":
            show_entries(entries)
        elif choice == "3":
            entries = delete_entry(entries)
        elif choice == "4":
            show_summary(entries)
        elif choice == "5":
            show_by_category(entries)
        elif choice == "6":
# Before quitting, save everything to the file
            save_data(DATA_FILE, entries)
            print("Data saved. Goodbye!")
            break
        else:
# If the user types something else, we just tell them and ask again.
            print("Invalid option. Please enter a number between 1 and 6.")

# This makes sure main() only runs when we actually execute main.py
# (and not when main.py gets imported from somewhere else).
if __name__ == "__main__":
    main()

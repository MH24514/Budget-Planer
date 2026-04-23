# main.py
# Personal Budget Planner - Main Program
# This file runs the main menu and handles user input.

from entries import add_entry, show_entries, delete_entry
from analysis import show_summary, show_by_category
from storage import load_data, save_data

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
    # Load existing entries from the file (if any exist)
    entries = load_data(DATA_FILE)
    print(f"Loaded {len(entries)} entries from {DATA_FILE}.")

    while True:
        print_menu()
        choice = input("Please choose an option (1-6): ").strip()

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
            save_data(DATA_FILE, entries)
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()

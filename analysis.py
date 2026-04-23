# analysis.py
# Functions for summarizing and analyzing budget entries.


def calculate_totals(entries):
    """Calculate total income, total expenses and balance."""
    total_income = 0.0
    total_expenses = 0.0

    for entry in entries:
        if entry["type"] == "income":
            total_income += entry["amount"]
        elif entry["type"] == "expense":
            total_expenses += entry["amount"]

    balance = total_income - total_expenses
    return total_income, total_expenses, balance


def show_summary(entries):
    """Display total income, total expenses and the current balance."""
    if len(entries) == 0:
        print("\nNo entries yet. Add some entries first.")
        return

    total_income, total_expenses, balance = calculate_totals(entries)

    print("\n--- Summary ---")
    print(f"Total income:   {total_income:>10.2f}")
    print(f"Total expenses: {total_expenses:>10.2f}")
    print(f"Balance:        {balance:>10.2f}")

    if balance < 0:
        print("Warning: you are spending more than you earn!")
    elif balance == 0:
        print("You are breaking even.")
    else:
        print("You have money left over. Good job!")


def show_by_category(entries):
    """Display total expenses grouped by category."""
    if len(entries) == 0:
        print("\nNo entries yet. Add some entries first.")
        return

    # Build a dictionary: category -> total amount spent
    category_totals = {}
    for entry in entries:
        if entry["type"] == "expense":
            cat = entry["category"]
            category_totals[cat] = category_totals.get(cat, 0.0) + entry["amount"]

    if len(category_totals) == 0:
        print("\nNo expenses recorded yet.")
        return

    # Sort categories by amount, highest first
    sorted_categories = sorted(category_totals.items(), key=lambda x: x[1], reverse=True)

    print("\n--- Expenses by Category ---")
    print(f"{'Category':<20}{'Amount':<10}")
    print("-" * 30)
    for category, amount in sorted_categories:
        print(f"{category:<20}{amount:<10.2f}")

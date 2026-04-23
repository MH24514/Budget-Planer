# analysis.py
# This file is all about calculations and summaries.
# It doesn't change the data, it only reads it and shows results.


def calculate_totals(entries):
    """Calculate total income, total expenses and balance."""
    total_income = 0.0
    total_expenses = 0.0

# Loop through every entry and add its amount to the right total depending on whether it's income or expense.
    for entry in entries:
        if entry["type"] == "income":
            total_income += entry["amount"]
        elif entry["type"] == "expense":
            total_expenses += entry["amount"]

# Balance = what's left after expenses.
    balance = total_income - total_expenses
    return total_income, total_expenses, balance


def show_summary(entries):
    """Display total income, total expenses and the current balance."""
    if len(entries) == 0:
        print("\nNo entries yet. Add some entries first.")
        return

# I put the calculation in a separate function (calculate_totals) so this function only has to deal with printing.
    total_income, total_expenses, balance = calculate_totals(entries)
# The :>10.2f means "right-align in 10 chars wide, 2 decimal places".
# That way all the numbers line up on the right, which looks cleaner.
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

# Build a dictionary that maps each category to the total amount spent in it.
# .get(cat, 0.0) returns the current value if the category already exists, or 0.0 if it's the first time we see this category.
# This trick avoids having to write "if cat in category_totals" every time.
    category_totals = {}
    for entry in entries:
        if entry["type"] == "expense":
            cat = entry["category"]
            category_totals[cat] = category_totals.get(cat, 0.0) + entry["amount"]

# Could be that there are only income entries and no expenses yet.
    if len(category_totals) == 0:
        print("\nNo expenses recorded yet.")
        return

# Sort the categories by amount. sorted() returns a list of (key, value) tuples.
# key=lambda x: x[1] means "sort by the second element" (the amount).
# reverse=True means "biggest first".
    sorted_categories = sorted(category_totals.items(), key=lambda x: x[1], reverse=True)

    print("\n--- Expenses by Category ---")
    print(f"{'Category':<20}{'Amount':<10}")
    print("-" * 30)
    for category, amount in sorted_categories:
        print(f"{category:<20}{amount:<10.2f}")

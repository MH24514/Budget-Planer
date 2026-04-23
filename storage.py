# storage.py
# Functions to load data from a CSV file and save data back to it.

import csv
import os


def load_data(filename):
    """Load entries from a CSV file. Return an empty list if the file does not exist."""
    entries = []

    if not os.path.exists(filename):
        # File does not exist yet, that's fine on first start
        return entries

    try:
        with open(filename, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert the amount back to a float
                try:
                    row["amount"] = float(row["amount"])
                except ValueError:
                    continue  # skip broken rows
                entries.append(row)
    except OSError as error:
        print(f"Could not read file: {error}")

    return entries


def save_data(filename, entries):
    """Save the list of entries to a CSV file."""
    fieldnames = ["date", "type", "category", "description", "amount"]

    try:
        with open(filename, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for entry in entries:
                writer.writerow(entry)
    except OSError as error:
        print(f"Could not save file: {error}")

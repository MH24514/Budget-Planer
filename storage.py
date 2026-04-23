# storage.py
# This file takes care of saving the entries to a CSV file and loading them back when the program starts.

import csv
import os


def load_data(filename):
    """Load entries from a CSV file. Return an empty list if the file does not exist."""
    entries = []

# Check first if the file exists. If not, there's nothing to load and we just return an empty list. This avoids a crash on the first run.
    if not os.path.exists(filename):
        # File does not exist yet, that's fine on first start
        return entries

    try:
# newline="" is recommended in the csv docs to avoid problems on Windows.
# encoding="utf-8" makes sure special characters (like ä, é) work.
        with open(filename, "r", encoding="utf-8", newline="") as f:
# DictReader automatically uses the first row as column names and returns each row as a dictionary.
            reader = csv.DictReader(f)
            for row in reader:
# In CSV files everything is a string. We need to convert the amount back to a float so we can do math with it.
                try:
                    row["amount"] = float(row["amount"])
                except ValueError:
# Skip rows where the amount is broken.
                    continue  
                entries.append(row)
    except OSError as error:
# OSError covers "permission denied", "disk full" etc.
        print(f"Could not read file: {error}")

    return entries


def save_data(filename, entries):
    """Save the list of entries to a CSV file."""
# The fieldnames define the column order in the file.
# Has to match the keys we used in the entry dictionaries.
    fieldnames = ["date", "type", "category", "description", "amount"]

    try:
# "w" means write mode, which overwrites the file if it exists.
# That's fine because we always have all the entries in memory anyway.
        with open(filename, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
# writeheader writes the first row with the column names.
            writer.writeheader()
# Then we just loop through all entries and write each one.
            for entry in entries:
                writer.writerow(entry)
    except OSError as error:
        print(f"Could not save file: {error}")

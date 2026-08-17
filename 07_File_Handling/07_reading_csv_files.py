# Lesson 07: Reading and Parsing CSV Records
import csv
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, "data", "output.csv")

try:
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        print("Parsing CSV Rows into Dictionaries:")
        for row in reader:
            print(f"  [{row['ID']}] {row['Name']} - {row['Department']} (${row['Salary']})")
except FileNotFoundError:
    print(f"File not found. Run 04_writing_csv_files.py first to generate {csv_path}")

# Lesson 04: Writing Tabular Data to CSV (csv.writer and csv.DictWriter)
import csv
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, "data", "output.csv")

employees = [
    ["ID", "Name", "Department", "Salary"],
    [101, "Dexter Morgan", "Forensics", 95000],
    [102, "Debra Morgan", "Homicide", 88000],
    [103, "Angel Batista", "Sergeant", 92000],
    [104, "James Doakes", "Sergeant", 91000]
]

with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(employees)

print(f"CSV data written successfully to: {csv_path}")

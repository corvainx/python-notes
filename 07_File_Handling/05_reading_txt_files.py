# Lesson 05: Reading Text Files Line-by-Line
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
sample_path = os.path.join(base_dir, "data", "sample.txt")

try:
    with open(sample_path, "r", encoding="utf-8") as f:
        print("--- Reading File Content ---")
        for line_num, line in enumerate(f, start=1):
            print(f"Line {line_num}: {line.strip()}")
except FileNotFoundError:
    print(f"Error: '{sample_path}' does not exist.")

# Lesson 02: Writing Text Files (Modes: 'w', 'a', 'x')
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(base_dir, "data", "output.txt")

# 1. Write Mode ('w') - Creates new or completely overwrites
with open(output_path, "w", encoding="utf-8") as f:
    f.write("Line 1: Python Journal Entry.\n")
    f.write("Line 2: Demonstrating file writing.\n")
print(f"Successfully wrote to: {output_path}")

# 2. Append Mode ('a') - Appends to end of existing file
with open(output_path, "a", encoding="utf-8") as f:
    f.write("Line 3: Appended content at end.\n")
print("Appended new line.")

# 3. Writing lists of strings with writelines()
team = ["Alice\n", "Bob\n", "Charlie\n", "Dexter\n"]
with open(output_path, "a", encoding="utf-8") as f:
    f.writelines(team)
print("Wrote team member list.")

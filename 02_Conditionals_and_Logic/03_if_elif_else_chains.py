# Lesson 03: If-Elif-Else Decision Trees

name = input("Enter your name: ")

# Checking for empty string input
if name == "":
    print("Error: You did not enter a name.")
elif len(name) < 2:
    print("Warning: Name is too short.")
else:
    print(f"Hello, {name}!")

# Score Grading System
score = int(input("Enter your exam score (0-100): "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your final grade is: {grade}")

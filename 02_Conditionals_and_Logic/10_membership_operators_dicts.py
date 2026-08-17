# Lesson 10: Membership Operators with Dictionaries

grade_book = {
    "Alice": "A",
    "Bob": "B+",
    "Charlie": "A-",
    "Dexter": "A+"
}

student = input("Enter student name to look up grade: ")

# 'in' on a dictionary checks against KEYS by default
if student in grade_book:
    print(f"{student}'s grade is: {grade_book[student]}")
else:
    print(f"Error: {student} does not exist in the grade book.")

# Checking values explicitly using .values()
if "A+" in grade_book.values():
    print("Notice: At least one student achieved an A+ distinction!")

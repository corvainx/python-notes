# Lesson 09: Membership Operators with Collections (Sets, Lists, Tuples)

registered_students = {"Alice", "Bob", "Charlie", "Dexter"}

query = input("Enter student name to check enrollment: ")

if query in registered_students:
    print(f"Verified: {query} is an enrolled student.")
else:
    print(f"Not Found: {query} is not in the enrollment registry.")

# Sets provide O(1) average time complexity for membership testing!

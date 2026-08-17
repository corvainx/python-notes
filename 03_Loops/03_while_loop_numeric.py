# Lesson 03: Range Bounds Validation with While Loops

num = int(input("Enter a number between 1 and 10: "))

while num < 1 or num > 10:
    print(f"Error: {num} is outside the allowed range [1, 10].")
    num = int(input("Please enter a number between 1 and 10: "))

print(f"Accepted value: {num}")

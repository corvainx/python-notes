# Lesson 02: Input Validation with While Loops

age = int(input("Enter your age: "))

# Ensure age is not negative
while age < 0:
    print("Validation Error: Age cannot be negative.")
    age = int(input("Please enter a valid age: "))

print(f"Recorded Age: You are {age} years old.")

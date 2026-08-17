# Lesson 01: Basic If-Else Statements

age = int(input("Enter your age: "))

if age >= 18:
    print("Status: You are an adult.")
elif age < 0:
    print("Invalid age: Age cannot be negative.")
else:
    print("Status: You are a minor.")

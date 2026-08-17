# Lesson 01: While Loop Basics
# A while loop repeats execution as long as a condition evaluates to True.

name = input("Enter your name: ")

# Continues prompting until non-empty input is received
while name == "":
    print("Error: You did not enter your name.")
    name = input("Enter your name: ")

print(f"Hello, {name}!")

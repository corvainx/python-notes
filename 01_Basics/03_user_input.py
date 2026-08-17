# Lesson 03: User Input
# input() prompts the user to enter data and always returns it as a string (str).

name = input("What's your name?: ")
age_input = input("What's your age?: ")

# Convert the string input to an integer for mathematical operations
age = int(age_input)
age_next_year = age + 1

print(f"\nHello, {name}!")
print(f"Happy Birthday in advance! Next year you will be {age_next_year} years old.")

# Example: Calculating the area of a rectangle from user input
print("\n--- Rectangle Area Calculator ---")
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
print(f"The area of the rectangle is: {area} sq units")

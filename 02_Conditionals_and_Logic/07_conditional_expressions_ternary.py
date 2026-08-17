# Lesson 07: Conditional Expressions (Ternary Operator)
# Syntax: X if condition else Y

num = 5
a = 15
b = 20
age = 22
temp = 32
user_role = "admin"

# Examples of concise inline conditionals:
parity = "EVEN" if num % 2 == 0 else "ODD"
max_val = a if a > b else b
min_val = a if a < b else b
status = "Adult" if age >= 18 else "Minor"
weather = "Hot" if temp > 25 else "Pleasant"
access_level = "Access Granted" if user_role == "admin" else "Access Denied"

print(f"Number parity: {num} is {parity}")
print(f"Max of {a} and {b}: {max_val}")
print(f"User Status: {status}")
print(f"Current Weather: {weather}")
print(f"System Access: {access_level}")

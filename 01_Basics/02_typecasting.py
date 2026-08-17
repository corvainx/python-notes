# Lesson 02: Typecasting
# Typecasting is the process of converting a variable from one data type to another.
# Common functions: str(), int(), float(), bool()

name = "Dexter Morgan"
age = 24
gpa = 3.8
is_student = True

# Inspect original types
print("--- Before Conversion ---")
print(f"age: {age} -> type: {type(age)}")
print(f"gpa: {gpa} -> type: {type(gpa)}")

# Explicit Type Conversion
gpa_as_int = int(gpa)      # Truncates decimal portion (3.8 -> 3)
age_as_float = float(age)  # Converts to decimal (24 -> 24.0)
age_as_str = str(age)      # Converts to string ("24")

print("\n--- After Conversion ---")
print(f"gpa as int: {gpa_as_int} -> type: {type(gpa_as_int)}")
print(f"age as float: {age_as_float} -> type: {type(age_as_float)}")
print(f"age as string: '{age_as_str}' -> type: {type(age_as_str)}")

# Boolean Conversion (Truthiness)
print("\n--- Boolean Conversion ---")
print(f"bool(''): {bool('')}")           # Empty string -> False
print(f"bool('Hello'): {bool('Hello')}") # Non-empty string -> True
print(f"bool(0): {bool(0)}")             # 0 -> False
print(f"bool(10): {bool(10)}")           # Non-zero number -> True

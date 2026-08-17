# Lesson 07: Essential String Methods

name = "Dexter Morgan"
phone_number = "123-456-7890"

# Length
print(f"len('{name}'): {len(name)}")

# Searching
print(f"find('o'): {name.find('o')}")      # First occurrence index (from left)
print(f"rfind('o'): {name.rfind('o')}")    # Last occurrence index (from right)
print(f"find('z'): {name.find('z')}")      # Returns -1 if not found

# Casing
print(f"capitalize(): {name.capitalize()}")
print(f"upper(): {name.upper()}")
print(f"lower(): {name.lower()}")
print(f"title(): {'the python journal'.title()}")

# Validation checks
print(f"'12345'.isdigit(): {'12345'.isdigit()}")
print(f"'Dexter'.isalpha(): {'Dexter'.isalpha()}")
print(f"'Dexter123'.isalnum(): {'Dexter123'.isalnum()}")

# Replacement and counting
print(f"phone_number.count('-'): {phone_number.count('-')}")
clean_phone = phone_number.replace("-", "")
print(f"Cleaned phone: {clean_phone}")

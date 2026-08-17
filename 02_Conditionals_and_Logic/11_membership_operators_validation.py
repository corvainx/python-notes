# Lesson 11: Practical Input Validation with Membership Operators

email = input("Enter your email address: ").strip()

# Simple syntax check for required email symbols
if "@" in email and "." in email:
    # Ensure '@' is not first or last character, and '.' comes after '@'
    at_index = email.find("@")
    dot_index = email.rfind(".")
    if 0 < at_index < dot_index < len(email) - 1:
        print(f"Success: '{email}' appears to be a valid email structure.")
    else:
        print(f"Invalid format: Placement of '@' and '.' is incorrect in '{email}'.")
else:
    print(f"Rejected: Missing essential '@' or '.' characters in '{email}'.")

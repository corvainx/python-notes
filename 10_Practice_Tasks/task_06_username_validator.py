# Practice Task 06: User Registration String Validator
# Validation Rules:
# 1. Length must not exceed 12 characters.
# 2. Must not contain spaces.
# 3. Must contain alphabetical characters only.

username = input("Enter desired username: ")

if len(username) > 12:
    print("Registration Failed: Username cannot exceed 12 characters.")
elif " " in username:
    print("Registration Failed: Username cannot contain whitespace.")
elif not username.isalpha():
    print("Registration Failed: Username must only contain alphabetical letters (A-Z).")
else:
    print(f"Registration Successful! Welcome, @{username}.")

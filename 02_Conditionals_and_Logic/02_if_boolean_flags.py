# Lesson 02: Evaluating Boolean Flags

is_logged_in = True
has_permission = False

if is_logged_in:
    print("Welcome back, User!")
else:
    print("Please log in to continue.")

if is_logged_in and has_permission:
    print("Access Granted to admin dashboard.")
else:
    print("Access Denied: Insufficient permissions.")

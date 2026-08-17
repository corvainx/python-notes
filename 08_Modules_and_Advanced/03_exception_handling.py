# Lesson 03: Comprehensive Exception Handling (try / except / else / finally)

try:
    user_input = input("Enter a positive divisor: ")
    number = int(user_input)
    result = 100 / number
except ZeroDivisionError as e:
    print(f"ZeroDivisionError Caught: Cannot divide by zero ({e}).")
except ValueError as e:
    print(f"ValueError Caught: Please enter valid numerical integers ({e}).")
except Exception as e:
    print(f"Unexpected General Exception: {type(e).__name__} -> {e}")
else:
    # Runs only if NO exceptions were raised in the try block
    print(f"Computation Successful: 100 / {number} = {result:.2f}")
finally:
    # Always runs regardless of success or failure (cleanup / resource release)
    print("Execution complete. Cleanup routines executed.")

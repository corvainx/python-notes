# Lesson 02: The `__name__ == '__main__'` Idiom
# When executed directly, __name__ is set to "__main__".
# When imported as a module into another script, __name__ is set to the module filename.

def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

print(f"[02_if_name_main_entry.py] Current __name__ is: {__name__}")

if __name__ == "__main__":
    print("\n--- Running in Standalone Direct Mode ---")
    num1 = 15
    num2 = 5
    print(f"Sum of {num1} and {num2}: {add(num1, num2)}")
    print(f"Difference of {num1} and {num2}: {subtract(num1, num2)}")

# Project 02: Console Arithmetic Calculator
# Practice: Conditionals, Arithmetic Operators, ZeroDivision Defense

def run_calculator():
    print("================================")
    print("       PYTHON CALCULATOR        ")
    print("================================")

    operator = input("Choose an operator (+, -, *, /): ").strip()
    if operator not in ("+", "-", "*", "/"):
        print(f"Error: '{operator}' is not a valid operator.")
        return

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Error: Input must be numeric.")
        return

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Error: Division by zero is undefined.")
            return
        result = num1 / num2

    print(f"\nResult: {num1} {operator} {num2} = {result:.4f}")

if __name__ == "__main__":
    run_calculator()

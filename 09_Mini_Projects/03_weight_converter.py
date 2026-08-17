# Project 03: Unit Weight Converter (Kilograms <-> Pounds)

def run_weight_converter():
    print("================================")
    print("        WEIGHT CONVERTER        ")
    print("================================")

    try:
        weight = float(input("Enter weight magnitude: "))
    except ValueError:
        print("Error: Weight must be a valid number.")
        return

    unit = input("Unit of input? (K for Kilograms, L for Pounds): ").strip().upper()

    if unit == "K":
        converted = weight * 2.20462
        print(f"Result: {weight:.2f} kg = {converted:.2f} lbs")
    elif unit == "L":
        converted = weight / 2.20462
        print(f"Result: {weight:.2f} lbs = {converted:.2f} kg")
    else:
        print(f"Error: '{unit}' is an invalid unit. Use 'K' or 'L'.")

if __name__ == "__main__":
    run_weight_converter()

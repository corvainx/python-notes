# Project 04: Temperature Converter (Celsius <-> Fahrenheit)

def convert_temperature():
    print("================================")
    print("     TEMPERATURE CONVERTER      ")
    print("================================")

    scale = input("Is the initial temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    try:
        temp = float(input("Enter temperature value: "))
    except ValueError:
        print("Error: Temperature must be a valid number.")
        return

    if scale == "C":
        converted = (temp * 9 / 5) + 32
        print(f"Result: {temp:.1f}°C = {converted:.1f}°F")
    elif scale == "F":
        converted = (temp - 32) * 5 / 9
        print(f"Result: {temp:.1f}°F = {converted:.1f}°C")
    else:
        print(f"Error: '{scale}' is not a recognized scale. Enter 'C' or 'F'.")

if __name__ == "__main__":
    convert_temperature()

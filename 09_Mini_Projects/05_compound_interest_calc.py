# Project 05: Compound Interest Investment Calculator
# Formula: Total = Principle * (1 + Rate / 100) ** Time

def calculate_compound_interest():
    print("================================")
    print("   COMPOUND INTEREST CALCULATOR ")
    print("================================")

    # Validating principle
    while True:
        try:
            principle = float(input("Enter principal investment ($): "))
            if principle <= 0:
                print("Principal must be greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter numbers only.")

    # Validating annual interest rate
    while True:
        try:
            rate = float(input("Enter annual interest rate (%): "))
            if rate < 0:
                print("Interest rate cannot be negative.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter numbers only.")

    # Validating time in years
    while True:
        try:
            time_years = int(input("Enter duration (years): "))
            if time_years <= 0:
                print("Duration must be at least 1 year.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter integers only.")

    total_balance = principle * pow((1 + (rate / 100)), time_years)
    total_interest = total_balance - principle

    print("\n--- INVESTMENT SUMMARY ---")
    print(f"Initial Principal : ${principle:,.2f}")
    print(f"Annual Rate       : {rate:.2f}%")
    print(f"Investment Period : {time_years} year(s)")
    print(f"Total Interest    : ${total_interest:,.2f}")
    print(f"Final Balance     : ${total_balance:,.2f}")

if __name__ == "__main__":
    calculate_compound_interest()

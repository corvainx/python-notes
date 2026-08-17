# Lesson 04: Date & Time Manipulation with the 'datetime' Module
import datetime

# 1. Current Timestamps
today = datetime.date.today()
now = datetime.datetime.now()

print(f"Current Date: {today}")
print(f"ISO Timestamp: {now.isoformat()}")

# 2. String Formatting (strftime)
formatted_now = now.strftime("%A, %B %d, %Y | %I:%M:%S %p")
print(f"Formatted: {formatted_now}")

# 3. Date Arithmetic & Comparison
target_future_date = datetime.datetime(2030, 1, 1, 0, 0, 0)
time_remaining = target_future_date - now

print(f"\nDays until {target_future_date.year}: {time_remaining.days} days")
if target_future_date > now:
    print("Status: The target milestone is in the future.")
else:
    print("Status: The target date has already elapsed.")

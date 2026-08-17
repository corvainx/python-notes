# Lesson 09: String Format Specifiers
# Format specifiers = {value:flags} inside f-strings format values cleanly.

price1 = 3.14159
price2 = -987.65
price3 = 12000.34
score = 42

# Decimal places
print(f"price1 (2 decimal places) : ${price1:.2f}")

# Field width and alignment
print(f"Right-aligned (width 10)  : ${price1:>10.2f}")
print(f"Left-aligned (width 10)   : ${price1:<10.2f}")
print(f"Center-aligned (width 10) : ${price1:^10.2f}")

# Zero-padding
print(f"Zero-padded (width 5)     : {score:05d}")

# Signs and Comma separators
print(f"Always show sign (+/-)    : {price1:+.2f}")
print(f"Comma separator           : ${price3:,.2f}")
print(f"Combined flags            : ${price3:+12,.2f}")

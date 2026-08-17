# Lesson 08: String Indexing and Slicing
# Syntax: sequence[start : stop : step]
# - start: starting index (inclusive)
# - stop: ending index (exclusive)
# - step: stride / step interval (default 1)

credit_card = "1234-5678-9012-3456"

# 1. Single character indexing
print(f"First character: {credit_card[0]}")
print(f"Last character: {credit_card[-1]}")

# 2. Slicing ranges
print(f"First 4 digits: {credit_card[0:4]}")
print(f"Second block: {credit_card[5:9]}")
print(f"From index 5 to end: {credit_card[5:]}")
print(f"Up to index 9: {credit_card[:9]}")

# 3. Negative slicing
last_4_digits = credit_card[-4:]
print(f"Masked Card: XXXX-XXXX-XXXX-{last_4_digits}")

# 4. Stepping and Reversal
print(f"Every second character: {credit_card[::2]}")
reversed_str = credit_card[::-1]
print(f"Reversed string: {reversed_str}")

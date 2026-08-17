# Lesson 07: Iterating Over Strings

credit_card = "1234-5678-9012-3456"

print("Iterating character by character:")
for char in credit_card:
    if char != "-":
        print(char, end="")
print("\nCard processed.")

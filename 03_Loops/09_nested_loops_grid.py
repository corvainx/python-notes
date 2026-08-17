# Lesson 09: Nested Loops & Grid Printing

print("Generating 3 rows of numbers from 1 to 9:")
for row in range(3):
    for col in range(1, 10):
        print(col, end=" ")
    print()  # Newline after each row

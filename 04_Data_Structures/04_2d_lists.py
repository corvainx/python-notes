# Lesson 04: Multidimensional / 2D Lists

fruits = ["apple", "orange", "banana"]
vegetables = ["celery", "carrots", "potatoes"]
proteins = ["chicken", "fish", "eggs"]

# Matrix representation of groceries
groceries = [fruits, vegetables, proteins]

print("--- 2D Groceries List ---")
for category in groceries:
    print(category)

print(f"\nSpecific Item [Row 1, Col 2]: {groceries[1][2]}")  # 'potatoes'

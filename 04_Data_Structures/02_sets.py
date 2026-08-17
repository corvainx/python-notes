# Lesson 02: Sets (Unordered, Mutable, Unique Elements Only)

# Sets automatically deduplicate input elements
fruits = {"apple", "orange", "banana", "coconut", "apple"}
print(f"Set contents (duplicates eliminated): {fruits}")

# 1. Membership Testing (O(1) average time complexity)
print(f"Is 'banana' in set?: {'banana' in fruits}")

# 2. Adding & Removing
fruits.add("pineapple")
fruits.discard("coconut")   # Safe removal (no KeyError if missing)
print(f"After add and discard: {fruits}")

# 3. Set Algebraic Operations
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"Union (A | B): {set_a | set_b}")
print(f"Intersection (A & B): {set_a & set_b}")
print(f"Difference (A - B): {set_a - set_b}")
print(f"Symmetric Diff (A ^ B): {set_a ^ set_b}")

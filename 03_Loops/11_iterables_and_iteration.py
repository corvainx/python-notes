# Lesson 11: Iterables and Iteration Protocol
# An iterable is any Python object capable of returning its members one at a time.

# 1. Iterating over Lists
nums_list = [10, 20, 30, 40]
print("List Iteration (Reversed):")
for item in reversed(nums_list):
    print(item, end=" ")
print()

# 2. Iterating over Tuples
coords = (4, 5, 6)
print("\nTuple Iteration:")
for val in coords:
    print(val, end=" ")
print()

# 3. Iterating over Sets (Unordered)
unique_fruits = {"apple", "banana", "cherry"}
print("\nSet Iteration:")
for fruit in unique_fruits:
    print(fruit, end=" ")
print()

# 4. Iterating over Dictionaries
profile = {"user": "dexter", "role": "admin", "status": "active"}
print("\nDictionary (key, value) pairs:")
for key, value in profile.items():
    print(f"  {key}: {value}")

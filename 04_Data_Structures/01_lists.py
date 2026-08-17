# Lesson 01: Lists (Ordered, Mutable, Allows Duplicates)

fruits = ["apple", "orange", "banana", "coconut"]
print(f"Initial List: {fruits}")

# 1. Accessing & Slicing
print(f"First element: {fruits[0]}")
print(f"Last element: {fruits[-1]}")
print(f"Slice [1:3]: {fruits[1:3]}")

# 2. Mutability
fruits[0] = "pineapple"
print(f"After modifying index 0: {fruits}")

# 3. List Operations & Methods
fruits.append("strawberry")     # Add to end
fruits.insert(1, "mango")       # Insert at index 1
fruits.remove("banana")         # Remove by value
popped_item = fruits.pop()      # Remove and return last element
print(f"Popped item: {popped_item}")
print(f"Current list: {fruits}")

# 4. Sorting & Reversing
fruits.sort()
print(f"Alphabetically sorted: {fruits}")
fruits.reverse()
print(f"Reversed order: {fruits}")

# 5. Queries
print(f"Count of 'mango': {fruits.count('mango')}")
print(f"Index of 'orange': {fruits.index('orange')}")
print(f"Is 'mango' in list?: {'mango' in fruits}")

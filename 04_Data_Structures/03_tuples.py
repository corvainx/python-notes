# Lesson 03: Tuples (Ordered, Immutable, Memory Efficient)

# Tuples cannot be modified after instantiation
fruits = ("apple", "orange", "banana", "coconut")
print(f"Tuple elements: {fruits}")

# 1. Indexing and Slicing
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print(f"Slice [1:3]: {fruits[1:3]}")

# 2. Query methods
print(f"Index of 'banana': {fruits.index('banana')}")
print(f"Count of 'apple': {fruits.count('apple')}")

# 3. Tuple Unpacking
coordinates = (10, 20, 30)
x, y, z = coordinates
print(f"Unpacked Coordinates: x={x}, y={y}, z={z}")

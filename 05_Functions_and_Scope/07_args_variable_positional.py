# Lesson 07: Variable Positional Arguments (*args)
# *args allows a function to accept any number of positional arguments as a tuple.

def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(f"Sum of 1, 2, 3: {sum_all(1, 2, 3)}")
print(f"Sum of 10, 20, 30, 40, 50: {sum_all(10, 20, 30, 40, 50)}")
print(f"Sum with 0 arguments: {sum_all()}")

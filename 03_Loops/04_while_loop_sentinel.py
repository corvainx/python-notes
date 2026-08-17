# Lesson 04: Sentinel Value Termination
# A sentinel value (e.g. 'q') signals the termination of a loop.

food = input("Enter a food you like (press 'q' to quit): ")

while food.lower() != "q":
    print(f"Added '{food}' to your favorites list.")
    food = input("Enter another food (press 'q' to quit): ")

print("Exited successfully. Goodbye!")

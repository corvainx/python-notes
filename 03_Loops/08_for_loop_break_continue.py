# Lesson 08: Loop Control Statements ('break', 'continue', 'pass')

print("--- Demonstrating 'continue' (Skip 13) ---")
for x in range(1, 16):
    if x == 13:
        continue  # Skips remaining body for current iteration
    print(x, end=" ")
print()

print("\n--- Demonstrating 'break' (Stop when finding target) ---")
target = 7
for x in range(1, 20):
    if x == target:
        print(f"Target {target} located! Terminating loop.")
        break
    print(f"Checking {x}...")

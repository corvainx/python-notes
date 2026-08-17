# Lesson 05: Immutable 2D Grid / Keypad Tuples

keypad = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    ("*", 0, "#")
)

print("Rendering Phone Keypad Matrix:")
for row in keypad:
    for key in row:
        print(f"[{key}]", end=" ")
    print()

# Lesson 10: Dynamic Pattern & Matrix Printing

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
symbol = input("Enter symbol to render (e.g. *, #, @): ")

print(f"\nRendering {rows}x{columns} grid:")
for r in range(rows):
    for c in range(columns):
        print(symbol, end=" ")
    print()

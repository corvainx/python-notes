# Practice Task 01: Rectangle Dimensions and Area Calculation

length = float(input("Enter rectangle length (cm): "))
breadth = float(input("Enter rectangle breadth (cm): "))

area = length * breadth
perimeter = 2 * (length + breadth)

print(f"\nResults:")
print(f"  Perimeter : {perimeter:.2f} cm")
print(f"  Area      : {area:.2f} cm²")

# Practice Task 02: Item Quantity and Total Cost Calculator

item_name = input("What item would you like to buy?: ").strip()
unit_price = float(input("Unit price ($): "))
quantity = int(input("Quantity desired: "))

total_cost = unit_price * quantity

print(f"\nOrder Confirmation:")
print(f"  Item Purchased : {quantity}x {item_name}")
print(f"  Total Cost     : ${total_cost:.2f}")

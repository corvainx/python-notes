# Lesson 04: Default Arguments
# Default values allow parameters to be optional when invoking functions.

def calculate_net_price(list_price, discount=0.0, tax=0.05):
    """Calculates final price after discount and sales tax."""
    discounted_price = list_price * (1 - discount)
    final_price = discounted_price * (1 + tax)
    return round(final_price, 2)

print(f"Standard Item ($100, default 0% discount, 5% tax): ${calculate_net_price(100)}")
print(f"Sale Item ($100, 10% discount): ${calculate_net_price(100, discount=0.10)}")
print(f"Special Tax Item ($100, 10% discount, 8% tax): ${calculate_net_price(100, 0.10, 0.08)}")

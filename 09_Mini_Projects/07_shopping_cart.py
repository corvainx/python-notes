# Project 07: Dynamic Shopping Cart System

def run_shopping_cart():
    items = []
    prices = []

    print("================================")
    print("      ONLINE SHOPPING CART      ")
    print("================================")

    while True:
        item = input("Enter item to buy (or 'q' to checkout): ").strip()
        if item.lower() == "q":
            break

        while True:
            try:
                price = float(input(f"Enter price for '{item}': $"))
                if price < 0:
                    print("Price cannot be negative.")
                    continue
                items.append(item)
                prices.append(price)
                break
            except ValueError:
                print("Invalid price format. Please enter a number.")

    print("\n" + "=" * 32)
    print("           RECEIPT              ")
    print("=" * 32)

    total = sum(prices)
    for idx, (itm, prc) in enumerate(zip(items, prices), start=1):
        print(f"{idx:02d}. {itm:<18} ${prc:>8.2f}")

    print("-" * 32)
    print(f"TOTAL DUE:             ${total:>8.2f}")
    print("=" * 32)
    print("Thank you for shopping with us!\n")

if __name__ == "__main__":
    run_shopping_cart()

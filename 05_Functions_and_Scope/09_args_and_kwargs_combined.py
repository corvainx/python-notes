# Lesson 09: Combining *args and **kwargs

def generate_shipping_label(*names, **address):
    """Generates a complete parcel shipping label."""
    recipient = " ".join(names)
    print(f"SHIP TO: {recipient.upper()}")

    street = address.get("street", "N/A")
    apt = address.get("apt")
    city = address.get("city", "N/A")
    state = address.get("state", "N/A")
    zip_code = address.get("zip", "N/A")

    if apt:
        print(f"{street}, Apt {apt}")
    else:
        print(street)
    print(f"{city}, {state} {zip_code}")

generate_shipping_label(
    "Dexter", "Morgan",
    street="Bay Harbor Club",
    apt="10B",
    city="Miami",
    state="FL",
    zip="33101"
)

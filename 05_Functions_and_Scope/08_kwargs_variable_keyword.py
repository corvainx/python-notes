# Lesson 08: Variable Keyword Arguments (**kwargs)
# **kwargs packs arbitrary keyword arguments into a dictionary.

def print_address(**kwargs):
    print("--- Mailing Address ---")
    for field, value in kwargs.items():
        print(f"  {field.capitalize()}: {value}")

print_address(
    street="123 Ocean Drive",
    apt="Suite 4B",
    city="Miami",
    state="FL",
    zipcode="33101"
)

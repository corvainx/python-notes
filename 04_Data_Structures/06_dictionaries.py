# Lesson 06: Dictionaries (Key-Value Mappings, Ordered, Mutable)

capitals = {
    "USA": "Washington D.C.",
    "India": "New Delhi",
    "China": "Beijing",
    "Japan": "Tokyo"
}

# 1. Safe Access with .get()
print(f"Capital of USA: {capitals.get('USA')}")
print(f"Capital of Germany (default fallback): {capitals.get('Germany', 'Not Found')}")

# 2. Mutating Entries
capitals.update({"Germany": "Berlin", "USA": "Washington"})
print(f"Updated Capitals: {capitals}")

# 3. Removing Entries
removed_val = capitals.pop("China")
print(f"Removed Capital: {removed_val}")

# 4. Iteration views
print("\n--- Iterating Key-Value Pairs ---")
for country, capital in capitals.items():
    print(f"{country} -> {capital}")

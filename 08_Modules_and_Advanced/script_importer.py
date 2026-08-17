# Companion Script: Demonstrates importing a file with `__name__ == '__main__'`
import importlib

# Dynamically import 02_if_name_main_entry
entry_module = importlib.import_module("02_if_name_main_entry")

print("\n--- Imported Mode in script_importer.py ---")
result = entry_module.add(100, 50)
print(f"Calling add() through imported module: {result}")

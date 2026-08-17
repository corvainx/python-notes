# Lesson 12: Variable Scope — Global Scope and 'global' Keyword
# Global variables are defined at top-level and visible across the module.

global_counter = 100

def read_counter():
    print(f"Reading global_counter: {global_counter}")

def increment_counter():
    global global_counter
    global_counter += 1
    print(f"Incremented global_counter to: {global_counter}")

read_counter()
increment_counter()
read_counter()

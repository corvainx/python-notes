# Lesson 11: Variable Scope — Enclosing Scope (Closures)
# Inner nested functions can access variables in their outer enclosing scope.

def outer_function():
    enclosing_msg = "Hello from Outer"

    def inner_function():
        # Accessible via enclosing scope
        print(f"Inside inner_function: {enclosing_msg}")

    inner_function()

outer_function()

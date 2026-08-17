# Lesson 10: Variable Scope — Local Scope
# Local variables are defined inside a function and are only accessible within it.

def function_a():
    local_x = 10
    print(f"Inside function_a: local_x = {local_x}")

def function_b():
    local_x = 20  # Separate variable from function_a's local_x
    print(f"Inside function_b: local_x = {local_x}")

function_a()
function_b()

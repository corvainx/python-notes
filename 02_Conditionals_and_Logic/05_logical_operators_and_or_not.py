# Lesson 05: Logical Operators (and, or, not)
# - and : True only if ALL sub-conditions evaluate to True
# - or  : True if AT LEAST ONE sub-condition evaluates to True
# - not : Inverts the boolean result (not True -> False, not False -> True)

temp = -5
is_raining = False

# Using 'or' operator: event cancelled if too hot, freezing, or raining
if temp > 35 or temp < 0 or is_raining:
    print("Notice: The outdoor event has been cancelled.")
else:
    print("Notice: The outdoor event is still scheduled as planned.")

# Using 'not' operator
is_sunny = False
if not is_sunny:
    print("Warning: Carry an umbrella or warm clothing.")

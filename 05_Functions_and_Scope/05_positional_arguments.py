# Lesson 05: Positional Arguments
# Arguments matched strictly by their parameter order.

def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

# Correct order:
describe_pet("hamster", "Harry")

# Swapping positions alters the semantic meaning:
describe_pet("Harry", "hamster")  # "I have a Harry named hamster."

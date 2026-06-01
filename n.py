import random

secret_number = random.randint(1, 50)
print("I'm thinking of a number between 1 and 50.")

while True:
    guess = int(input("Enter your guess: "))
    if guess < secret_number:
        print("Too low! Try a higher number.")
    elif guess > secret_number:
        print("Too high! Try a lower number.")
    else:
        print("Congratulations, you won!")
        break
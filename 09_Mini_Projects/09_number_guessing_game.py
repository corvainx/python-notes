# Project 09: Number Guessing Game with Binary Search Hinting
import random

def play_guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("================================")
    print("      NUMBER GUESSING GAME      ")
    print("================================")
    print("I have selected a secret number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! ⬆️ Try a higher number.")
        elif guess > secret_number:
            print("Too high! ⬇️ Try a lower number.")
        else:
            print(f"\n🎉 Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
            break

if __name__ == "__main__":
    play_guessing_game()

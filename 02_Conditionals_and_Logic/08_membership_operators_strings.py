# Lesson 08: Membership Operators with Strings ('in' and 'not in')
# Used to test whether a substring or character exists within a string sequence.

secret_word = "PYTHON"
guess = input("Guess a letter in the secret word: ").upper()

if guess in secret_word:
    print(f"Correct! '{guess}' is in the secret word.")
else:
    print(f"Wrong! '{guess}' is not in the secret word.")

# Case-sensitivity reminder:
# 'p' in 'PYTHON' evaluates to False because strings are case-sensitive.

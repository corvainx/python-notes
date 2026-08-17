# Project 01: Interactive Mad Libs Story Generator
# Practice: User Input, String Formatting, Variable Interpolation

def play_madlibs():
    print("================================")
    print("      MAD LIBS STORY GAME       ")
    print("================================")

    adjective1 = input("Enter an adjective (e.g. spooky, giant): ")
    noun1 = input("Enter a noun (e.g. dinosaur, programmer): ")
    adjective2 = input("Enter a second adjective (e.g. glowing, hyper): ")
    verb1 = input("Enter a verb ending in 'ing' (e.g. coding, dancing): ")
    emotion = input("Enter an emotional adjective (e.g. ecstatic, shocked): ")

    print("\n--- YOUR GENERATED STORY ---")
    print(f"Today I ventured into a {adjective1} laboratory.")
    print(f"In the main testing chamber, I discovered a wild {noun1}.")
    print(f"The {noun1} was surprisingly {adjective2} and kept {verb1} around the room.")
    print(f"When I saw it, I was completely {emotion}!\n")

if __name__ == "__main__":
    play_madlibs()

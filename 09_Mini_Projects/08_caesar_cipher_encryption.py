# Project 08: Substitution Cipher Encryption & Decryption Tool
import random
import string

def build_cipher_keys():
    # Build complete character space
    chars = " " + string.punctuation + string.digits + string.ascii_letters
    char_list = list(chars)
    shuffled_key = char_list.copy()
    random.seed(42)  # Deterministic seed for repeatable testing
    random.shuffle(shuffled_key)
    return char_list, shuffled_key

def encrypt(message: str, chars: list, key: list) -> str:
    encrypted = []
    for letter in message:
        if letter in chars:
            idx = chars.index(letter)
            encrypted.append(key[idx])
        else:
            encrypted.append(letter)
    return "".join(encrypted)

def decrypt(cipher_text: str, chars: list, key: list) -> str:
    decrypted = []
    for letter in cipher_text:
        if letter in key:
            idx = key.index(letter)
            decrypted.append(chars[idx])
        else:
            decrypted.append(letter)
    return "".join(decrypted)

if __name__ == "__main__":
    chars, key = build_cipher_keys()
    original_msg = input("Enter a message to encrypt: ")
    encrypted_msg = encrypt(original_msg, chars, key)
    decrypted_msg = decrypt(encrypted_msg, chars, key)

    print(f"\nOriginal  : {original_msg}")
    print(f"Encrypted : {encrypted_msg}")
    print(f"Decrypted : {decrypted_msg}")

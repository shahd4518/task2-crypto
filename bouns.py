import string
from collections import Counter

english_frequency = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'U', 'C', 'M', 'F', 'Y', 'W', 'G', 'P', 'B', 'V', 'K', 'X', 'Q', 'J', 'Z']

def decrypt_monoalphabetic_cipher(encrypted_text):
    encrypted_text = encrypted_text.upper()
    encrypted_text = ''.join(filter(lambda x: x in string.ascii_uppercase, encrypted_text))
    letter_counts = Counter(encrypted_text)
    most_common_letters = [letter for letter, _ in letter_counts.most_common()]
    decryption_map = {}
    for i, letter in enumerate(most_common_letters):
        if i < len(english_frequency):
            decryption_map[letter] = english_frequency[i]
    decrypted_text = ''.join(decryption_map.get(letter, letter) for letter in encrypted_text)
    return decrypted_text, decryption_map

encrypted_text = input("Enter the encrypted text: ")
decrypted_text, decryption_map = decrypt_monoalphabetic_cipher(encrypted_text)

print("\nDecrypted text: ", decrypted_text)
print("\nDecryption Map: ")
for key, value in decryption_map.items():
    print(f"{key} -> {value}")

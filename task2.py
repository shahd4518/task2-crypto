import itertools
import string

def decrypt(ciphertext, key_mapping):
    return "".join(key_mapping.get(c, c) for c in ciphertext)

def brute_force_monoalphabetic(ciphertext):
    alphabet = string.ascii_lowercase
    possible_permutations = itertools.permutations(alphabet)
    
    results = []
    for perm in possible_permutations:
        key_mapping = dict(zip(alphabet, perm))
        decrypted_text = decrypt(ciphertext.lower(), key_mapping)
        results.append(decrypted_text)
        
        if len(results) >= 100:
            break
    
    return results

ciphertext = "wklv lv d whvw phvvdjh"  # Example encrypted text
possible_plaintexts = brute_force_monoalphabetic(ciphertext)

for i, text in enumerate(possible_plaintexts):
    print(f"Possible plaintext {i+1}: {text}")
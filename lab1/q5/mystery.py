def text_to_numbers(text):
    return [ord(c.upper()) - ord('A') for c in text]

def numbers_to_text(numbers):
    return ''.join(chr(n + ord('A')) for n in numbers)

def find_shift_key(plaintext, ciphertext):
    # Calculate shift key based on first character pair
    p = ord(plaintext[0].upper()) - ord('A')
    c = ord(ciphertext[0].upper()) - ord('A')
    # shift key k satisfies: (p + k) % 26 = c
    k = (c - p) % 26
    return k

def decrypt_shift(ciphertext, key):
    ciphertext_nums = text_to_numbers(ciphertext)
    plaintext_nums = [(c - key) % 26 for c in ciphertext_nums]
    return numbers_to_text(plaintext_nums)

if __name__ == "__main__":
    # Given known plaintext and ciphertext
    known_plaintext = "yes"
    known_ciphertext = "CIW"

    # Ciphertext to decrypt
    new_ciphertext = "XVIEWYWI"

    # Step 1: Find key from known plaintext attack
    key = find_shift_key(known_plaintext, known_ciphertext)
    print(f"Found shift key: {key}")

    # Step 2: Decrypt new ciphertext with the found key
    decrypted_text = decrypt_shift(new_ciphertext, key)
    print(f"Decrypted text for '{new_ciphertext}': {decrypted_text}")

    # Step 3: Identify attack type
    attack_type = "Known Plaintext Attack"
    print(f"Type of attack: {attack_type}")

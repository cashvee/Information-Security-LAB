def clean_text(text):
    return text.replace(" ", "").lower()

# Vigenere Cipher implementation
def vigenere_encrypt(plaintext, key):
    plaintext = clean_text(plaintext)
    key = key.lower()
    ciphertext = ""
    key_length = len(key)
    for i, char in enumerate(plaintext):
        # A-Z shift 0-25
        p = ord(char) - ord('a')
        k = ord(key[i % key_length]) - ord('a')
        c = (p + k) % 26
        ciphertext += chr(c + ord('a'))
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    key = key.lower()
    plaintext = ""
    key_length = len(key)
    for i, char in enumerate(ciphertext):
        c = ord(char) - ord('a')
        k = ord(key[i % key_length]) - ord('a')
        p = (c - k + 26) % 26
        plaintext += chr(p + ord('a'))
    return plaintext

# Autokey Cipher implementation (using numeric key for shift)
# Usually autokey cipher uses a key as a string; here key=7 means initial shift=7
# We'll implement a classic Autokey cipher where the key is a number shift
# The key is the initial shift; after that, the plaintext letters are used as key

def autokey_encrypt(plaintext, key):
    plaintext = clean_text(plaintext)
    ciphertext = ""
    key_stream = [key]  # start with the numeric key
    for i, char in enumerate(plaintext):
        p = ord(char) - ord('a')
        k = key_stream[i]
        c = (p + k) % 26
        ciphertext += chr(c + ord('a'))
        # for autokey: append plaintext letter to key stream for next rounds
        key_stream.append(p)
    return ciphertext

def autokey_decrypt(ciphertext, key):
    plaintext = ""
    key_stream = [key]
    for i, char in enumerate(ciphertext):
        c = ord(char) - ord('a')
        k = key_stream[i]
        p = (c - k + 26) % 26
        plaintext += chr(p + ord('a'))
        key_stream.append(p)
    return plaintext

# Input message
message = "the house is being sold tonight"

# Vigenere cipher
key_vigenere = "dollars"
ciphertext_vigenere = vigenere_encrypt(message, key_vigenere)
decrypted_vigenere = vigenere_decrypt(ciphertext_vigenere, key_vigenere)

print("Vigenere Cipher:")
print("Plaintext:", clean_text(message))
print("Encrypted:", ciphertext_vigenere)
print("Decrypted:", decrypted_vigenere)
print()

# Autokey cipher
key_autokey = 7
ciphertext_autokey = autokey_encrypt(message, key_autokey)
decrypted_autokey = autokey_decrypt(ciphertext_autokey, key_autokey)

print("Autokey Cipher:")
print("Plaintext:", clean_text(message))
print("Encrypted:", ciphertext_autokey)
print("Decrypted:", decrypted_autokey)

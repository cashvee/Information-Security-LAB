def char_to_int(c):
    return ord(c) - ord('a')

def int_to_char(i):
    return chr(i + ord('a'))

def mod_inverse(key, mod=26):
    for i in range(1, mod):
        if (key * i) % mod == 1:
            return i
    raise ValueError("No modular inverse found")

def encrypt_additive(plaintext, key):
    encrypted = ""
    for c in plaintext:
        if c.isalpha():
            encrypted += int_to_char((char_to_int(c) + key) % 26)
    return encrypted

def decrypt_additive(ciphertext, key):
    decrypted = ""
    for c in ciphertext:
        if c.isalpha():
            decrypted += int_to_char((char_to_int(c) - key) % 26)
    return decrypted

def encrypt_multiplicative(plaintext, key):
    encrypted = ""
    for c in plaintext:
        if c.isalpha():
            encrypted += int_to_char((char_to_int(c) * key) % 26)
    return encrypted

def decrypt_multiplicative(ciphertext, key):
    inverse_key = mod_inverse(key)
    decrypted = ""
    for c in ciphertext:
        if c.isalpha():
            decrypted += int_to_char((char_to_int(c) * inverse_key) % 26)
    return decrypted

def encrypt_affine(plaintext, a, b):
    encrypted = ""
    for c in plaintext:
        if c.isalpha():
            encrypted += int_to_char((a * char_to_int(c) + b) % 26)
    return encrypted

def decrypt_affine(ciphertext, a, b ):
    a_inv = mod_inverse(a)
    decrypted = ""
    for c in ciphertext:
        if c.isalpha():
            decrypted += int_to_char((a_inv * (char_to_int(c) - b)) % 26)
    return decrypted

# Main message
message = "Iamlearninginformationsecurity".lower()

# a) Additive cipher key=20
add_encrypted = encrypt_additive(message, 20)
add_decrypted = decrypt_additive(add_encrypted, 20)
print("Additive Cipher")
print("Encrypted:", add_encrypted)
print("Decrypted:", add_decrypted)

# b) Multiplicative cipher key=15
mul_encrypted = encrypt_multiplicative(message, 15)
mul_decrypted = decrypt_multiplicative(mul_encrypted, 15)
print("\nMultiplicative Cipher")
print("Encrypted:", mul_encrypted)
print("Decrypted:", mul_decrypted)

# c) Affine cipher key=(15, 20)
aff_encrypted = encrypt_affine(message, 15, 20)
aff_decrypted = decrypt_affine(aff_encrypted, 15, 20)
print("\nAffine Cipher")
print("Encrypted:", aff_encrypted)
print("Decrypted:", aff_decrypted)

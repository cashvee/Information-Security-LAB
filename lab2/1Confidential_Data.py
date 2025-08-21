from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# AES-192 key (24 bytes = 48 hex chars)
key_hex = "FEDCBA9876543210FEDCBA9876543210FEDCBA9876543210"
key = bytes.fromhex(key_hex)

# Message
message = b"Top Secret Data"

# Generate a random IV for CBC mode
iv = get_random_bytes(16)   

# Create AES cipher in CBC mode with AES-192 key
cipher = AES.new(key, AES.MODE_CBC, iv)

# Pad and encrypt
padded_message = pad(message, AES.block_size)
ciphertext = cipher.encrypt(padded_message)

print("IV (hex):", iv.hex())
print("Ciphertext (hex):", ciphertext.hex())

# Decrypt to verify
decipher = AES.new(key, AES.MODE_CBC, iv)
decrypted = unpad(decipher.decrypt(ciphertext), AES.block_size)

print("Decrypted message:", decrypted.decode())

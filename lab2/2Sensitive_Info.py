from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Key given as hex string (32 hex chars = 16 bytes)
key_hex = "0123456789ABCDEF0123456789ABCDEF"
key = bytes.fromhex(key_hex)  # convert hex string to bytes

# Message to encrypt
message = b"Sensitive Information"

# Generate a random 16-byte IV
iv = get_random_bytes(16)

# Create AES cipher in CBC mode
cipher = AES.new(key, AES.MODE_CBC, iv)

# Pad message to block size and encrypt
padded_message = pad(message, AES.block_size)
ciphertext = cipher.encrypt(padded_message)

print("IV (hex):", iv.hex())
print("Ciphertext (hex):", ciphertext.hex())

# To decrypt, create a new cipher with the same key and IV
decipher = AES.new(key, AES.MODE_CBC, iv)

# Decrypt and unpad
decrypted_padded = decipher.decrypt(ciphertext)
decrypted = unpad(decrypted_padded, AES.block_size)

print("Decrypted message:", decrypted.decode())

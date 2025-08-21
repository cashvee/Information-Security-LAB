from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Generate a valid Triple DES key
key = DES3.adjust_key_parity(get_random_bytes(24))

print("Valid 3DES key (hex):", key.hex())

message = b"Classified Text"
iv = get_random_bytes(8)

cipher = DES3.new(key, DES3.MODE_CBC, iv)
padded_message = pad(message, DES3.block_size)
ciphertext = cipher.encrypt(padded_message)

print("IV (hex):", iv.hex())
print("Ciphertext (hex):", ciphertext.hex())

decipher = DES3.new(key, DES3.MODE_CBC, iv)
decrypted = unpad(decipher.decrypt(ciphertext), DES3.block_size)
print("Decrypted message:", decrypted.decode())

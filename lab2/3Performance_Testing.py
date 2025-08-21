import time
from Crypto.Cipher import DES, AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

message = b"Performance Testing of Encryption Algorithms"

# DES Setup
des_key = b'8bytekey'  # exactly 8 bytes
des_cipher_enc = DES.new(des_key, DES.MODE_ECB)
des_cipher_dec = DES.new(des_key, DES.MODE_ECB)

# AES-256 Setup
aes_key = get_random_bytes(32)  # 32 bytes for AES-256
aes_iv = get_random_bytes(16)   # 16 bytes IV for AES
aes_cipher_enc = AES.new(aes_key, AES.MODE_CBC, aes_iv)
aes_cipher_dec = AES.new(aes_key, AES.MODE_CBC, aes_iv)

# --- DES encryption ---
start = time.time()
des_ciphertext = des_cipher_enc.encrypt(pad(message, DES.block_size))
des_enc_time = time.time() - start

# --- DES decryption ---
start = time.time()
des_plaintext = unpad(des_cipher_dec.decrypt(des_ciphertext), DES.block_size)
des_dec_time = time.time() - start

# --- AES encryption ---
start = time.time()
aes_ciphertext = aes_cipher_enc.encrypt(pad(message, AES.block_size))
aes_enc_time = time.time() - start

# --- AES decryption ---
start = time.time()
aes_plaintext = unpad(aes_cipher_dec.decrypt(aes_ciphertext), AES.block_size)
aes_dec_time = time.time() - start

# Results
print("DES Encryption Time: {:.6f} seconds".format(des_enc_time))
print("DES Decryption Time: {:.6f} seconds".format(des_dec_time))
print("AES-256 Encryption Time: {:.6f} seconds".format(aes_enc_time))
print("AES-256 Decryption Time: {:.6f} seconds".format(aes_dec_time))

# Verify correctness
assert des_plaintext == message, "DES decryption failed!"
assert aes_plaintext == message, "AES decryption failed!"

print("\nBoth DES and AES decrypted correctly.")

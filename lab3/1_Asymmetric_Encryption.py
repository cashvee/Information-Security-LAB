from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generate RSA keys
key = RSA.generate(2048)
public_key = key.publickey()
private_key = key

# Message
msg = b"Asymmetric Encryption"

# Encrypt with public key
cipher = PKCS1_OAEP.new(public_key)
ciphertext = cipher.encrypt(msg)

# Decrypt with private key
decipher = PKCS1_OAEP.new(private_key)
plaintext = decipher.decrypt(ciphertext)

print("Ciphertext:", ciphertext)
print("Decrypted:", plaintext.decode())

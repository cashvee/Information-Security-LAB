import random
from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes

# Key generation
p = getPrime(256)          # large prime
g = random.randint(2, p-2) # generator
x = random.randint(1, p-2) # private key
h = pow(g, x, p)           # public key component

public_key = (p, g, h)
private_key = x

# Message
msg = b"Confidential Data"
m = bytes_to_long(msg)     # convert message to integer

# --- Encryption ---
y = random.randint(1, p-2)        # random session key
c1 = pow(g, y, p)
s = pow(h, y, p)                  # shared secret
c2 = (m * s) % p                  # ciphertext

ciphertext = (c1, c2)
print("Ciphertext:", ciphertext)

# --- Decryption ---
s_dec = pow(c1, x, p)
s_inv = pow(s_dec, -1, p)         # modular inverse
m_dec = (c2 * s_inv) % p
plaintext = long_to_bytes(m_dec)

print("Decrypted:", plaintext.decode())

import random
import time
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# ---------- Diffie-Hellman Setup ----------
p = 23  # small prime (demo purpose; use 2048-bit in real life)
g = 5

def diffie_hellman():
    a = random.randint(2, p-2)
    b = random.randint(2, p-2)
    A = pow(g, a, p)
    B = pow(g, b, p)
    shared_A = pow(B, a, p)
    shared_B = pow(A, b, p)
    assert shared_A == shared_B
    return shared_A

# ---------- Subsystem Class ----------
class Subsystem:
    def __init__(self, name):
        self.name = name
        self.key_pair = RSA.generate(2048)
        self.public_key = self.key_pair.publickey()
        self.cipher = PKCS1_OAEP.new(self.key_pair)

    def encrypt_message(self, message, receiver_pubkey):
        cipher_rsa = PKCS1_OAEP.new(receiver_pubkey)
        return cipher_rsa.encrypt(message.encode())

    def decrypt_message(self, ciphertext):
        return self.cipher.decrypt(ciphertext).decode()

# ---------- Key Management ----------
class KeyManager:
    def __init__(self):
        self.keys = {}

    def register(self, subsystem):
        self.keys[subsystem.name] = subsystem.public_key

    def revoke(self, name):
        if name in self.keys:
            del self.keys[name]

# ---------- Demo ----------
if __name__ == "__main__":
    # Setup subsystems
    finance = Subsystem("Finance System")
    hr = Subsystem("HR System")
    scm = Subsystem("Supply Chain System")

    # Key Manager
    km = KeyManager()
    for sys in [finance, hr, scm]:
        km.register(sys)

    # Secure key exchange (Diffie-Hellman)
    start = time.time()
    shared_secret = diffie_hellman()
    print("Shared session key (DH):", shared_secret)
    print("Key exchange time:", time.time() - start, "s")

    # Secure communication (RSA)
    msg = "Confidential Financial Report"
    ciphertext = finance.encrypt_message(msg, km.keys["HR System"])
    print("\nEncrypted message:", ciphertext[:50], "...")

    decrypted = hr.decrypt_message(ciphertext)
    print("Decrypted message (at HR):", decrypted)

    # Key revocation example
    km.revoke("Supply Chain System")
    print("\nKeys after revocation:", list(km.keys.keys()))

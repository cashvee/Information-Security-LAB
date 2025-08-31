import secrets
import tinyec.ec as ec
import tinyec.registry as reg
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib

# Curve setup
curve = reg.get_curve("secp256r1")

# Generate private/public keys
privKey = secrets.randbelow(curve.field.n)
pubKey = privKey * curve.g

# Shared secret derivation
def ecc_point_to_key(point):
    return hashlib.sha256(int(point.x).to_bytes(32, "big")).digest()

# ECC Encryption (using ephemeral key)
def encrypt(pubKey, msg):
    ephKey = secrets.randbelow(curve.field.n)
    shared = ephKey * pubKey
    secret = ecc_point_to_key(shared)
    aes = AES.new(secret, AES.MODE_ECB)
    ct = aes.encrypt(pad(msg.encode(), 16))
    return (ephKey * curve.g, ct)

# ECC Decryption
def decrypt(privKey, ciphertext):
    ephPubKey, ct = ciphertext
    shared = privKey * ephPubKey
    secret = ecc_point_to_key(shared)
    aes = AES.new(secret, AES.MODE_ECB)
    pt = unpad(aes.decrypt(ct), 16)
    return pt.decode()

# --- Demo ---
msg = "Secure Transactions"
ciphertext = encrypt(pubKey, msg)
print("Ciphertext:", ciphertext[1])

plaintext = decrypt(privKey, ciphertext)
print("Decrypted:", plaintext)

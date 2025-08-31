import time, os, hashlib, secrets
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from tinyec import registry

def aes(k, d):
    c = AES.new(k, AES.MODE_GCM)
    ct, tg = c.encrypt_and_digest(d)
    AES.new(k, AES.MODE_GCM, nonce=c.nonce).decrypt_and_verify(ct, tg)
    return c.nonce, ct, tg

def t(fn, *a): 
    s=time.time(); r=fn(*a); return time.time()-s, r

d = os.urandom(1024*1024)         # 1 MB file

# RSA
kg, rsa = t(RSA.generate, 2048)
k = get_random_bytes(32)
ek = PKCS1_OAEP.new(rsa.publickey()).encrypt(k)
e, (n, ct, tg) = t(aes, k, d)
k2 = PKCS1_OAEP.new(rsa).decrypt(ek)
dec, _ = t(aes, k2, d)
print(f"RSA-2048: KeyGen={kg:.4f}s Enc={e:.4f}s Dec={dec:.4f}s")

# ECC
c = registry.get_curve("secp256r1")
kg, priv = t(lambda: secrets.randbelow(c.field.n))
pub = priv*c.g
eph = secrets.randbelow(c.field.n)
sh = eph*pub
k = hashlib.sha256(int(sh.x).to_bytes(32,"big")).digest()
e, (n, ct, tg) = t(aes, k, d)
sh2 = priv*(eph*c.g)
k2 = hashlib.sha256(int(sh2.x).to_bytes(32,"big")).digest()
dec, _ = t(aes, k2, d)
print(f"ECC-P256: KeyGen={kg:.4f}s Enc={e:.4f}s Dec={dec:.4f}s")

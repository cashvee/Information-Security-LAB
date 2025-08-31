import time, random

# Large safe prime (RFC 3526 Group 14 - 2048 bits)
p = int(
    "FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD1"
    "29024E088A67CC74020BBEA63B139B22514A08798E3404DD"
    "EF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245"
    "E485B576625E7EC6F44C42E9A63A36210000000000090563",
    16
)
g = 2

# Peer A
t0 = time.time()
a = random.randint(2, p - 2)           # private key
A = pow(g, a, p)                       # public key
keygen_A = time.time() - t0

# Peer B
t0 = time.time()
b = random.randint(2, p - 2)
B = pow(g, b, p)
keygen_B = time.time() - t0

# Exchange and compute shared secret
t0 = time.time()
shared_A = pow(B, a, p)
shared_B = pow(A, b, p)
exchange_time = time.time() - t0

print("Peer A public key:", A)
print("Peer B public key:", B)
print("Shared secret (A):", shared_A)
print("Shared secret (B):", shared_B)
print("KeyGen A Time: %.6fs" % keygen_A)
print("KeyGen B Time: %.6fs" % keygen_B)
print("Exchange Time: %.6fs" % exchange_time)

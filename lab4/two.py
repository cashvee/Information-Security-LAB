import random
import time
import logging
from math import gcd

# Setup logging for auditing
logging.basicConfig(filename="key_management.log", level=logging.INFO,
                    format="%(asctime)s - %(message)s")

# ---------- Rabin Cryptosystem ----------
def generate_rabin_keypair(bits=512):
    """Generate Rabin public and private key pair"""
    def get_prime(bits):
        while True:
            p = random.getrandbits(bits)
            if p % 4 == 3 and is_prime(p):
                return p

    p = get_prime(bits // 2)
    q = get_prime(bits // 2)
    n = p * q
    return (n,), (p, q)   # Public = (n,), Private = (p,q)

def is_prime(n, k=5):  # Miller-Rabin primality test
    if n < 2:
        return False
    for _ in range(k):
        a = random.randint(2, n - 2)
        if gcd(a, n) != 1 or pow(a, n - 1, n) != 1:
            return False
    return True

# ---------- Key Management Service ----------
class KeyManagementService:
    def __init__(self):
        self.keys = {}  # { hospital_name: {pub, priv, last_renew} }

    def generate_keys(self, name, bits=1024):
        pub, priv = generate_rabin_keypair(bits)
        self.keys[name] = {"public": pub, "private": priv, "last_renew": time.time()}
        logging.info(f"Generated keys for {name}")
        return pub, priv

    def distribute_keys(self, name):
        if name in self.keys:
            logging.info(f"Distributed keys to {name}")
            return self.keys[name]["public"], self.keys[name]["private"]
        return None

    def revoke_keys(self, name):
        if name in self.keys:
            del self.keys[name]
            logging.info(f"Revoked keys for {name}")

    def renew_keys(self, interval=10):  # short interval for demo
        now = time.time()
        for name in list(self.keys.keys()):
            if now - self.keys[name]["last_renew"] > interval:
                self.generate_keys(name)
                logging.info(f"Renewed keys for {name}")

    def audit_log(self):
        print("---- Audit Log ----")
        with open("key_management.log") as f:
            print(f.read())

# ---------- Demo ----------
if __name__ == "__main__":
    kms = KeyManagementService()

    # Hospitals request keys
    pub1, priv1 = kms.generate_keys("Hospital A")
    pub2, priv2 = kms.generate_keys("Clinic B")

    # Distribution
    print("Hospital A keys:", kms.distribute_keys("Hospital A"))

    # Simulate renewal
    time.sleep(2)
    kms.renew_keys(interval=1)  # Force renew quickly for demo

    # Revoke a key
    kms.revoke_keys("Clinic B")

    # Print audit log
    kms.audit_log()

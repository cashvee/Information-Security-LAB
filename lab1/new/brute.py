from math import gcd

m = 26  # Alphabet size

def mod_inverse(a, m):
    # Find modular inverse of a under mod m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_decrypt_char(c, a_inv, b):
    y = ord(c) - ord('A')
    x = (a_inv * (y - b)) % m
    return chr(x + ord('A'))

def affine_decrypt(text, a, b):
    a_inv = mod_inverse(a, m)
    if a_inv is None:
        return None
    result = ''
    for c in text:
        if c.isalpha():
            result += affine_decrypt_char(c.upper(), a_inv, b)
        else:
            result += c
    return result

def find_candidate_keys(pt_pair, ct_pair):
    # Given pt_pair and ct_pair (both length 2), find all possible (a,b) matching this pair
    candidates = []
    x1, x2 = [ord(c.lower()) - ord('a') for c in pt_pair]
    y1, y2 = [ord(c.upper()) - ord('A') for c in ct_pair]

    for a in range(1, m):
        if gcd(a, m) != 1:
            continue  # skip invalid a
        for b in range(m):
            # Check if affine encrypt matches pt->ct for both chars
            if (a * x1 + b) % m == y1 and (a * x2 + b) % m == y2:
                candidates.append((a, b))
    return candidates

if __name__ == "__main__":
    known_plaintext = "ab"
    known_ciphertext = "GL"
    ciphertext = "XPALASXYFGFUKPXUSOGEUTKCDGEXANMGNVS"

    keys = find_candidate_keys(known_plaintext, known_ciphertext)
    if not keys:
        print("No keys found that match the known pair.")
    else:
        print(f"Possible keys (a,b) that map '{known_plaintext}' -> '{known_ciphertext}': {keys}\n")

        for a, b in keys:
            decrypted = affine_decrypt(ciphertext, a, b)
            print(f"Decrypted with key (a={a}, b={b}):")
            print(decrypted)
            print("-" * 50)

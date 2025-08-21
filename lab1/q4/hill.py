def preprocess_text(text):
    # Remove spaces, make uppercase, keep only letters
    text = ''.join(filter(str.isalpha, text)).upper()
    if len(text) % 2 != 0:
        text += 'X'  # padding if odd length
    return text

def text_to_numbers(text):
    return [ord(char) - ord('A') for char in text]

def numbers_to_text(numbers):
    return ''.join(chr(num + ord('A')) for num in numbers)

def hill_encrypt(plaintext, key):
    plaintext = preprocess_text(plaintext)
    plaintext_numbers = text_to_numbers(plaintext)

    ciphertext_numbers = []

    # Key is a 2x2 matrix: list of lists [[a,b],[c,d]]
    a, b = key[0]
    c, d = key[1]

    for i in range(0, len(plaintext_numbers), 2):
        p1 = plaintext_numbers[i]
        p2 = plaintext_numbers[i+1]

        # Multiply and mod 26
        c1 = (a * p1 + b * p2) % 26
        c2 = (c * p1 + d * p2) % 26

        ciphertext_numbers.extend([c1, c2])

    return numbers_to_text(ciphertext_numbers)

if __name__ == "__main__":
    key_matrix = [[3, 3],
                  [2, 7]]

    message = "We live in an insecure world"
    cipher = hill_encrypt(message, key_matrix)
    print("Plaintext:", message)
    print("Ciphertext:", cipher)

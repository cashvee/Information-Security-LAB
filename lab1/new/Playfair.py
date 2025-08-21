def create_playfair_matrix_fixed(key):
    key = key.upper().replace('J', 'I')
    # Remove duplicates from key
    seen = []
    for char in key:
        if char not in seen and char.isalpha():
            seen.append(char)
    # Matrix starts with key letters, but fill first row + part of second row only
    # key letters count = 8
    matrix_letters = []

    # Fill first row: 5 letters
    matrix_letters += seen[:5]

    # Fill start of second row: next 3 letters
    matrix_letters += seen[5:8]

    # Now fill rest of alphabet except letters already in matrix and 'J'
    alphabet = [chr(c) for c in range(ord('A'), ord('Z')+1) if chr(c) != 'J']

    for letter in alphabet:
        if letter not in matrix_letters:
            matrix_letters.append(letter)

    # Reshape into 5x5 matrix
    matrix = [matrix_letters[i*5:(i+1)*5] for i in range(5)]
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(' '.join(row))


def find_position(matrix, char):
    for i, row in enumerate(matrix):
        for j, c in enumerate(row):
            if c == char:
                return i, j
    return None


def preprocess_text(text):
    text = text.upper().replace('J', 'I')
    text = ''.join(filter(str.isalpha, text))  # Remove spaces and non-alpha
    result = ""
    i = 0
    while i < len(text):
        a = text[i]
        b = ''
        if i + 1 < len(text):
            b = text[i + 1]

        if b == a:
            result += a + 'X'
            i += 1
        else:
            if b:
                result += a + b
                i += 2
            else:
                result += a + 'X'
                i += 1
    return result


def playfair_encrypt_pair(matrix, a, b):
    r1, c1 = find_position(matrix, a)
    r2, c2 = find_position(matrix, b)

    if r1 == r2:  # same row
        return matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]
    elif c1 == c2:  # same column
        return matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]
    else:  # rectangle swap columns
        return matrix[r1][c2] + matrix[r2][c1]


def playfair_encrypt(text, key):
    matrix = create_playfair_matrix_fixed(key)
    print("Playfair Key Matrix:")
    print_matrix(matrix)

    text = preprocess_text(text)
    print("\nProcessed plaintext (digraphs):", ' '.join(text[i:i+2] for i in range(0, len(text), 2)))

    ciphertext = ""
    for i in range(0, len(text), 2):
        ciphertext += playfair_encrypt_pair(matrix, text[i], text[i+1])
    return ciphertext


# Example usage
plaintext = "The key is hidden under the door pad"
key = "GUIDANCE"

ciphertext = playfair_encrypt(plaintext, key)
print("\nEncrypted ciphertext:", ciphertext)

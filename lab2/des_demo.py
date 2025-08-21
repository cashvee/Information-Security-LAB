from Crypto.Hash import SHA256

message = b"Hello, this is a message to hash!"

# Create a new SHA-256 hash object
hash_obj = SHA256.new(data=message)

# Get the hexadecimal digest
hash_hex = hash_obj.hexdigest()

print(f"SHA-256 hash: {hash_hex}")

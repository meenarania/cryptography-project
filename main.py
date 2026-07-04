import hashlib

password = input("Enter password: ")

hashed_password = hashlib.sha256(password.encode()).hexdigest()

print("Original Password:", password)
print("Hashed Password:", hashed_password)
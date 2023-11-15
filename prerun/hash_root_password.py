import maskpass
import hashlib


def hash_password(password: str):
    return hashlib.sha512(password.encode()).hexdigest()


root_password = maskpass.askpass("Enter your root password: ", mask="#")

print()

print(root_password)

print()

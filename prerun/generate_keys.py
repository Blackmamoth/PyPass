from Crypto.PublicKey import RSA
import os


def generate_keys(dir_path: str):
    try:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)
        private_key = RSA.generate(1024)
        public_key = private_key.public_key()
        os.chdir(dir_path)
        with open("public_key.pem", "w") as public_key_file:
            public_key_file.write(public_key.export_key().decode())
        with open("private_key.pem", "w") as private_key_file:
            private_key_file.write(private_key.export_key().decode())
        print(f"Private and public key successfully save at {dir_path} directory.")
    except Exception:
        print("An error occured while generating and saving keys.")


directory_path = input(
    "Enter the path to the directory where you want to store your keys: "
)

generate_keys(dir_path=directory_path)

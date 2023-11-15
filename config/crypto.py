from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from config.environment import Environment
from config.console import ConsoleLogger
import binascii
import hashlib


class Cryptography:
    def __init__(self) -> None:
        self.public_key, self.private_key = self._load_keys()

    def _load_keys(self) -> None:
        try:
            with open(Environment.PUBLIC_KEY_PATH) as public_file:
                public_key = public_file.read()
            with open(Environment.PRIVATE_KEY_PATH) as private_file:
                private_key = private_file.read()
            return [RSA.import_key(public_key), RSA.import_key(private_key)]
        except FileNotFoundError as e:
            ConsoleLogger.error(e.strerror)

    def encrypt_data(self, data: str) -> str:
        try:
            encryptor = PKCS1_OAEP.new(self.public_key)
            encrypted = encryptor.encrypt(data.encode("utf-8"))
            return binascii.hexlify(encrypted).decode("utf-8")
        except Exception as e:
            ConsoleLogger.error(e)

    def decrypt_data(self, encrypted_data: str) -> str:
        try:
            data = binascii.unhexlify(encrypted_data.encode("utf-8"))
            decryptor = PKCS1_OAEP.new(self.private_key)
            decrypted = decryptor.decrypt(data)
            return decrypted.decode("utf-8")
        except Exception as e:
            ConsoleLogger.error(e)

    def hash_data(self, data: str) -> str:
        return hashlib.sha512(data.encode()).hexdigest()

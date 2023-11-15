from dotenv import load_dotenv
from os import environ

load_dotenv()


class Environment:
    PRIVATE_KEY_PATH = environ.get("PRIVATE_KEY_PATH")
    PUBLIC_KEY_PATH = environ.get("PUBLIC_KEY_PATH")
    ROOT_PASSWORD = environ.get("ROOT_PASSWORD")

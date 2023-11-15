from dataclasses import dataclass


@dataclass
class PasswordType:
    id: str
    application: str
    password: str

from dataclasses import dataclass, asdict


@dataclass
class PasswordType:
    id: str
    application: str
    password: str

    def to_dict(self):
        return asdict(self)

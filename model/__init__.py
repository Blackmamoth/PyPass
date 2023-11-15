from sqlalchemy.orm import DeclarativeBase
from uuid import uuid4


class Base(DeclarativeBase):
    ...


def generate_uuid():
    return uuid4().hex

from model import Base, generate_uuid
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text
from config.db import engine


class Password(Base):
    __tablename__ = "passwords"

    id: Mapped[str] = mapped_column(
        primary_key=True, unique=True, default=generate_uuid, nullable=False
    )
    application: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(Text, nullable=False)

    def __repr__(self) -> str:
        return f"<Password for [{self.application}]>"


Base.metadata.create_all(bind=engine)

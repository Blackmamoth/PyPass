from config.crypto import Cryptography
from model.password import Password
from config.db import session
from config.console import ConsoleLogger
from exception.exceptions import DuplicateEntryError, ApplicationNotFoundError
from type.password import PasswordType
from config.environment import Environment

_cryptography = Cryptography()


class PasswordManager:
    def __init__(self, application: str, password: str) -> None:
        self.application = application
        self.password = _cryptography.encrypt_data(password)

    def save(self) -> None:
        try:
            does_password_exist = PasswordManager.find_password_by_application(
                application=self.application
            )
            if does_password_exist is not None:
                raise DuplicateEntryError(
                    f"A record for the application [{self.application}] already exists."
                )
            password = Password(application=self.application, password=self.password)
            session.add(password)
            session.commit()
            ConsoleLogger.info("Password successfully saved to the database.")
        except DuplicateEntryError as e:
            ConsoleLogger.error(e)
        except Exception as e:
            ConsoleLogger.error(
                "An error occured while saving password to the database."
            )

    @staticmethod
    def find_password_by_application(application: str) -> Password | None:
        password = session.query(Password).filter_by(application=application).first()
        return password

    @staticmethod
    def update_password(application: str, new_password: str) -> None:
        try:
            password = PasswordManager.find_password_by_application(
                application=application
            )
            if password is None:
                raise ApplicationNotFoundError(
                    f"Application [{application}] does not exist."
                )
            password.password = _cryptography.encrypt_data(new_password)
            session.commit()
            ConsoleLogger.info("Password updated successfully.")
        except ApplicationNotFoundError as e:
            ConsoleLogger.error(e)
        except Exception as e:
            ConsoleLogger.error("An error occured while updating password.")

    @staticmethod
    def delete_password(application: str) -> None:
        try:
            password = PasswordManager.find_password_by_application(
                application=application
            )
            if password is None:
                raise ApplicationNotFoundError(
                    f"Application [{application}] does not exist."
                )
            session.delete(password)
            session.commit()
            ConsoleLogger.info("Password deleted successfully.")
        except ApplicationNotFoundError as e:
            ConsoleLogger.error(e)
        except Exception as e:
            ConsoleLogger.error("An error occured while deleting password.")

    @staticmethod
    def get_all_passwords(unecnrypted: bool = False) -> list[PasswordType]:
        query = session.query(Password)
        passwords = session.scalars(query)
        if not unecnrypted:
            encrypted_passwords = [
                PasswordType(
                    id=password.id,
                    application=password.application,
                    password=password.passwprd,
                )
                for password in passwords
            ]
            return encrypted_passwords
        else:
            unencrypted_passwords = [
                PasswordType(
                    id=password.id,
                    application=password.application,
                    password=_cryptography.decrypt_data(password.password),
                )
                for password in passwords
            ]
            return unencrypted_passwords

    @staticmethod
    def verify_root_password(password: str) -> bool:
        try:
            hashed_password = _cryptography.hash_data(data=password)
            return Environment.ROOT_PASSWORD == hashed_password
        except Exception as e:
            return False

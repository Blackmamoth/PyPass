from config.crypto import Cryptography
from model.password import Password
from config.db import session
from config.console import ConsoleLogger
from exception.exceptions import DuplicateEntryError, ApplicationNotFoundError
from type.password import PasswordType
from config.environment import Environment
import json
import os

_cryptography = Cryptography()


class PasswordManager:
    def __init__(self, application: str, password: str) -> None:
        self.application = application
        self.password = _cryptography.encrypt_data(password)

    def save(self, show_success: bool = True) -> None:
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
            ConsoleLogger.info(
                "Password successfully saved to the database."
            ) if show_success else None
        except DuplicateEntryError as e:
            ConsoleLogger.error(e)
        except Exception:
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
        except Exception:
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
        except Exception:
            ConsoleLogger.error("An error occured while deleting password.")

    @staticmethod
    def get_all_passwords(
        unecnrypted: bool = False, as_dictionary: bool = False
    ) -> list[PasswordType]:
        query = session.query(Password)
        passwords = session.scalars(query)
        password_list = [
            (
                PasswordType(
                    id=password.id,
                    application=password.application,
                    password=_cryptography.decrypt_data(password.password)
                    if unecnrypted
                    else password.password,
                ).to_dict()
                if as_dictionary
                else PasswordType(
                    id=password.id,
                    application=password.application,
                    password=_cryptography.decrypt_data(password.password)
                    if unecnrypted
                    else password.password,
                )
            )
            for password in passwords
        ]
        return password_list

    @staticmethod
    def verify_root_password(password: str) -> bool:
        try:
            hashed_password = _cryptography.hash_data(data=password)
            return Environment.ROOT_PASSWORD == hashed_password
        except Exception:
            return False

    @staticmethod
    def import_passwords(file_path: str) -> None:
        try:
            with open(file_path) as password_file:
                passwords: list[dict] = json.loads(password_file.read())
            for item in passwords:
                application = item.get("application")
                password_value = item.get("password")
                if application and password_value:
                    password = PasswordManager(
                        application=application, password=password_value
                    )
                    password.save(show_success=False)
            ConsoleLogger.info("Passwords imported successfully.")
        except FileNotFoundError:
            ConsoleLogger.error(f"{file_path} does not exist.")
        except json.decoder.JSONDecodeError:
            ConsoleLogger.error("An error occured while decoding json in your file.")
        except Exception:
            ConsoleLogger.error("An error occured while importing passwords.")

    @staticmethod
    def export_passwords(file_path: str) -> None:
        try:
            does_file_path_exist = os.path.exists(file_path)
            if not does_file_path_exist:
                f_path = file_path.split("/")
                f_path.pop()
                dir_path = "/".join(f_path)
                os.makedirs(dir_path, exist_ok=True)
            with open(file_path, "w") as passwords_file:
                passwords = PasswordManager.get_all_passwords(
                    unecnrypted=True, as_dictionary=True
                )
                to_json = json.dumps(passwords)
                passwords_file.write(to_json)
            ConsoleLogger.info("Passwords exported successfully.")
        except Exception as e:
            ConsoleLogger.error("An error occured while exporting passwords.")

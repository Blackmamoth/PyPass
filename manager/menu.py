from inquirer import List, Path, prompt
from manager.manager import PasswordManager
from rich.table import Table
from rich.console import Console
from os import system, name
from config.console import ConsoleLogger
import maskpass

_choices = [
    "1. Add a new password.",
    "2. Show all passwords.",
    "3. Update a password.",
    "4. Delete a password.",
    "5. Import passwords.",
    "6. Export passwords.",
    "7. Exit.",
]


def _clear_screen() -> None:
    if name == "nt":
        system("cls")
    else:
        system("clear")


class PasswordManagerMenu:
    def show_menu(self):
        options = [
            List(
                "options",
                message="Choose an option between 1-5",
                choices=_choices,
            ),
        ]
        option = prompt(options)
        index = _choices.index(option.get("options"))
        _clear_screen()
        return index

    def verify_root_password(self) -> bool:
        password = maskpass.askpass("Enter your root password to proceed: ", mask="#")
        return PasswordManager.verify_root_password(password=password)

    def add_password(self):
        application = input("Enter the name of the application: ")
        password = maskpass.askpass("Enter the password for this application: ")
        pm = PasswordManager(application=application, password=password)
        pm.save()

    def show_passwords(self):
        if self.verify_root_password():
            passwords = PasswordManager.get_all_passwords(unecnrypted=True)
            table = Table(title="Password List")
            table.add_column("S. No.", style="cyan", no_wrap=True)
            table.add_column("Application", style="magenta")
            table.add_column("Password", justify="right", style="green")
            for index, password in enumerate(passwords):
                table.add_row(f"{index + 1}", password.application, password.password)
            console = Console()
            console.print(table)
        else:
            ConsoleLogger.error("Invalid root password, try again.")

    def update_password(self):
        if self.verify_root_password():
            application = input("Enter the name of the application: ")
            new_password = maskpass.askpass(
                "Enter the new password for this application: "
            )
            PasswordManager.update_password(
                application=application, new_password=new_password
            )
        else:
            ConsoleLogger.error("Invalid root password, try again.")

    def delete_password(self):
        if self.verify_root_password():
            application = input("Enter the name of the application: ")
            PasswordManager.delete_password(application=application)
        else:
            ConsoleLogger.error("Invalid root password, try again.")

    def import_passwords(self):
        json_file = [
            Path(
                "json_file",
                message="Enter the path to your passwords file, which is in json format",
                path_type=Path.FILE,
                exists=True,
            )
        ]
        file_path = prompt(json_file).get("json_file")
        PasswordManager.import_passwords(file_path=file_path)

    def export_passwords(self):
        if self.verify_root_password():
            json_file = [
                Path(
                    "json_file",
                    message="Please enter the path to which you want to save your passwords, use the extension '.json'.",
                    path_type=Path.FILE,
                )
            ]
            file_path = prompt(json_file).get("json_file")
            PasswordManager.export_passwords(file_path=file_path)
        else:
            ConsoleLogger.error("Invalid root password, try again.")

from manager.menu import PasswordManagerMenu


def main() -> None:
    menu = PasswordManagerMenu()
    while True:
        option = menu.show_menu()
        match option:
            case 0:
                menu.add_password()
            case 1:
                menu.show_passwords()
            case 2:
                menu.update_password()
            case 3:
                menu.delete_password()
            case 4:
                break


main()

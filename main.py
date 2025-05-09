from modules.menu import show_menu, menu_selection
from modules.os_det import clear_screen

from time import sleep

def main():
    menu_error = False
    clear_screen()
    while True:
        if menu_error == True:
            print(f"{menu_choice} is not an available option!")
            menu_error = False

        menu_choice = show_menu()
        menu_error = menu_selection(menu_choice)

if __name__ == "__main__":
    main()

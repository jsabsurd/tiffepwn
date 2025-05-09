from modules.menu import show_menu
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
        
        if menu_choice == "1":
            print("nmap loading...")
            sleep(2)
            break
        elif menu_choice == "x":
            break
        else:
            menu_error = True
        clear_screen()

if __name__ == "__main__":
    main()

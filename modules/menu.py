from modules.os_det import clear_screen
from time import sleep

def show_menu():
    print("select what to do:")
    print("1: nmap (simple nmap implementation)")
    print()
    print("x: exit")
    
    choice = input("> ")
    return choice

def menu_selection(menu_choice):
    menu_error = False
    if menu_choice == "1":
        print("nmap loading...")
        sleep(2)
    elif menu_choice == "x":
        print("goodby!")
        exit()
    else:
        menu_error=True
    clear_screen()
    return menu_error

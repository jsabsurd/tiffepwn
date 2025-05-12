from modules.os_det import clear_screen
from modules.nmap_func import nmap_simple
from modules.webbuster import bustit
from time import sleep
import asyncio
from termcolor import colored


def show_menu():

    print("████████╗██╗███████╗███████╗███████╗███████╗    ██████╗ ██╗    " +
          "  ██╗███╗   ██╗      ██╗  ██╗██╗████████╗")
    print("╚══██╔══╝██║██╔════╝██╔════╝██╔════╝██╔════╝    ██╔══██╗██║    " +
          " ║████╗  ██║      ██║ ██╔╝██║╚══██╔══╝")
    print("   ██║   ██║█████╗  █████╗  █████╗  ███████╗    ██████╔╝██║ █╗ " +
          " ║██╔██╗ ██║█████╗█████╔╝ ██║   ██║   ")
    print("   ██║   ██║██╔══╝  ██╔══╝  ██╔══╝  ╚════██║    ██╔═══╝ ██║███╗" +
          " ║██║╚██╗██║╚════╝██╔═██╗ ██║   ██║   ")
    print("   ██║   ██║██║     ██║     ███████╗███████║    ██║     ╚███╔██" +
          " ╔╝██║ ╚████║      ██║  ██╗██║   ██║   ")
    print("   ╚═╝   ╚═╝╚═╝     ╚═╝     ╚══════╝╚══════╝    ╚═╝      ╚══╝╚═" +
          "═╝ ╚═╝  ╚═══╝      ╚═╝  ╚═╝╚═╝   ╚═╝   ")
    print("                                                               \
            ")
    print("                     " +
          colored("\"Ein Tiffe Sport FM Schnellfilm.\"",
                  "yellow", "on_grey"))
    print("select what to do:")
    print("1: nmap (simple nmap implementation)")
    print("2: bruteforc website dirs/files")
    print()
    print("x: exit")

    choice = input("> ")
    return choice


def menu_selection(menu_choice):
    menu_error = False
    if menu_choice == "1":
        clear_screen()
        nmap_simple()
    elif menu_choice == "2":
        clear_screen()
        asyncio.run(bustit(["get-started", "backup", "login.php"]))
    elif menu_choice == "x":
        print(colored("Hier wird gehackt wie beim Amt - nur ohne Genehmigung!",
                      "yellow", "on_grey"))
        exit()
    else:
        menu_error = True
    clear_screen()
    return menu_error

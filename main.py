from modules.menu import show_menu

def main():
    while True:
        menu_choice = show_menu()
        
        if menu_choice == "1":
            print("nmap loading...")
        elif menu_choice == "x":
            break
        else:
            print(f"{menu_choice} is not an available option!")

if __name__ == "__main__":
    main()

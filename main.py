from modules.menu import show_menu

def main():
    while True:
        menu_choice = show_menu()
        
        if menu_choice == "x":
            break
        else:
            print(f"das hier: {menu_choice} ?")

if __name__ == "__main__":
    main()

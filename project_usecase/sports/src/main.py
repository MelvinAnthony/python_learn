import player_manager

def main_menu():
    while True:
        print("\n=== Cricket Player Management ===")
        print("1. Add Player")
        print("2. View Players")
        print("3. Update Player")
        print("4. Remove Player")
        print("6. View Player Stats")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            player_manager.add_player()
        elif choice == "2":
            player_manager.view_player()
        elif choice == "3":
            player_manager.update_player()
        elif choice == "4":
            player_manager.remove_player()
        elif choice == "5":
            player_manager.add_stats()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main_menu()
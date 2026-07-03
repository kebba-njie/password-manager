from manager import add_password, view_passwords

def main():
    while True:
        print("\n🔐 PASSWORD MANAGER")
        print("1. Add password")
        print("2. View passwords")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_password()

        elif choice == "2":
            view_passwords()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
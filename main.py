from manager import (
    add_password,
    view_passwords,
    analyze_password_strength,
    calculate_password_entropy,
    generate_password
)


def main():
    while True:
        print("\nPASSWORD MANAGER")
        print("========================")
        print("1. Add password")
        print("2. View passwords")
        print("3. Analyze password strength")
        print("4. Calculate password entropy")
        print("5. Generate secure password")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            analyze_password_strength()
        elif choice == "4":
            calculate_password_entropy()
        elif choice == "5":
            generate_password()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()
from manager import (
    add_password,
    view_passwords,
    analyze_password_strength,
    calculate_password_entropy,
    generate_password,
    detect_common_password,
    detect_password_reuse,
    search_password,
    delete_password,
    update_password,
    export_password_report
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
        print("6. Detect common passwords")
        print("7. Detect password reuse")
        print("8. Search passwords")
        print("9. Delete saved password")
        print("10. Update saved password")
        print("11. Export account report")
        print("12. Exit")

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
            detect_common_password()
        elif choice == "7":
            detect_password_reuse()
        elif choice == "8":
            search_password()
        elif choice == "9":
            delete_password()
        elif choice == "10":
            update_password()
        elif choice == "11":
         export_password_report()
        elif choice == "12":
         print("Goodbye!")
        break
        print("Invalid option, try again.")


if __name__ == "__main__":
    main()
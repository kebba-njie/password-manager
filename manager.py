from storage import load_data, save_data

def add_password():
    website = input("Website: ")
    username = input("Username: ")
    password = input("Password: ")

    data = load_data()

    data.append({
        "website": website,
        "username": username,
        "password": password
    })

    save_data(data)

    print("✅ Password saved successfully!")


def view_passwords():
    data = load_data()

    if not data:
        print("❌ No passwords saved yet.")
        return

    print("\n🔐 SAVED PASSWORDS:")
    for item in data:
        print("----------------------")
        print("Website:", item["website"])
        print("Username:", item["username"])
        print("Password:", item["password"])


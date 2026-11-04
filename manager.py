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
    print("Password saved successfully!")


def view_passwords():
    data = load_data()

    if not data:
        print("No passwords saved yet.")
        return

    print("\nSAVED PASSWORDS:")

    for item in data:
        print("----------------------")
        print("Website:", item["website"])
        print("Username:", item["username"])
        print("Password:", item["password"])


def analyze_password_strength():
    password = input("Enter a sample password to analyze: ")

    score = 0

    if len(password) >= 8:
        score += 1

    if len(password) >= 12:
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(not char.isalnum() for char in password):
        score += 1

    print("\nPASSWORD SECURITY ANALYSIS")
    print("--------------------------")

    if score <= 2:
        print("Strength: WEAK")
    elif score <= 4:
        print("Strength: MODERATE")
    else:
        print("Strength: STRONG")

    print("Security Score:", score, "/ 6")
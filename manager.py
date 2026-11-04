import math
import secrets
import string

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


def calculate_password_entropy():
    password = input("Enter a sample password: ")

    if not password:
        print("Password cannot be empty.")
        return

    pool_size = 0

    if any(char.islower() for char in password):
        pool_size += 26
    if any(char.isupper() for char in password):
        pool_size += 26
    if any(char.isdigit() for char in password):
        pool_size += 10
    if any(not char.isalnum() for char in password):
        pool_size += 32

    entropy = len(password) * math.log2(pool_size)

    print("\nPASSWORD ENTROPY ANALYSIS")
    print("--------------------------")
    print("Password Length:", len(password))
    print("Estimated Entropy:", round(entropy, 2), "bits")

    if entropy < 28:
        print("Security Level: VERY WEAK")
    elif entropy < 36:
        print("Security Level: WEAK")
    elif entropy < 60:
        print("Security Level: MODERATE")
    elif entropy < 80:
        print("Security Level: STRONG")
    else:
        print("Security Level: VERY STRONG")


def generate_password():
    try:
        length = int(input("Enter desired password length (8-64): "))

        if length < 8 or length > 64:
            print("Password length must be between 8 and 64.")
            return

        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        symbols = string.punctuation

        password = [
            secrets.choice(lowercase),
            secrets.choice(uppercase),
            secrets.choice(digits),
            secrets.choice(symbols)
        ]

        all_characters = lowercase + uppercase + digits + symbols

        for _ in range(length - 4):
            password.append(secrets.choice(all_characters))

        secrets.SystemRandom().shuffle(password)

        print("\nGENERATED PASSWORD")
        print("--------------------------")
        print("".join(password))

    except ValueError:
        print("Please enter a valid number.")


def detect_common_password():
    common_passwords = {
        "123456",
        "password",
        "123456789",
        "12345678",
        "qwerty",
        "abc123",
        "password123",
        "admin",
        "admin123",
        "letmein",
        "welcome",
        "iloveyou",
        "111111",
        "000000",
        "123123"
    }

    password = input("Enter a sample password to check: ")

    if not password:
        print("Password cannot be empty.")
        return

    print("\nCOMMON PASSWORD CHECK")
    print("--------------------------")

    if password.lower() in common_passwords:
        print("WARNING: This is a commonly used password!")
        print("Security Risk: HIGH")
    else:
        print("This password is not in our common password list.")
        print("Security Risk: Not identified by this check.")
def detect_password_reuse():
    data = load_data()

    if len(data) < 2:
        print("At least two saved accounts are needed.")
        return

    password_counts = {}

    for item in data:
        password = item["password"]
        password_counts[password] = password_counts.get(password, 0) + 1

    reused_passwords = {
        password: count
        for password, count in password_counts.items()
        if count > 1
    }

    print("\nPASSWORD REUSE CHECK")
    print("--------------------------")

    if reused_passwords:
        print("WARNING: Password reuse detected!")

        for password, count in reused_passwords.items():
            print("A password is used by", count, "accounts.")

        print("Security Risk: HIGH")
    else:
        print("No reused passwords detected.")
        print("Security Risk: No reuse found.") 
def search_password():
    data = load_data()

    if not data:
        print("No passwords saved yet.")
        return

    search_term = input("Enter website name to search: ").strip().lower()

    if not search_term:
        print("Search term cannot be empty.")
        return

    results = [
        item for item in data
        if search_term in item["website"].lower()
    ]

    print("\nPASSWORD SEARCH RESULTS")
    print("--------------------------")

    if results:
        for item in results:
            print("Website:", item["website"])
            print("Username:", item["username"])
            print("--------------------------")

        print("Matches found:", len(results))
    else:
        print("No matching website found.")   
def delete_password():
    data = load_data()

    if not data:
        print("No passwords saved yet.")
        return

    website = input("Enter website name: ").strip().lower()
    username = input("Enter username: ").strip().lower()

    matching_accounts = [
        item for item in data
        if item["website"].lower() == website
        and item["username"].lower() == username
    ]

    if not matching_accounts:
        print("No matching account found.")
        return

    if len(matching_accounts) > 1:
        print("Multiple matching accounts found.")
        print("Please make sure the website and username identify one account.")
        return

    confirmation = input("Are you sure you want to delete this account? (yes/no): ")

    if confirmation.lower() == "yes":
        data.remove(matching_accounts[0])
        save_data(data)
        print("Account deleted successfully!")
    else:
        print("Deletion cancelled.")                    
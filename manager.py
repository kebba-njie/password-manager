import csv
import math
import secrets
import string

from datetime import datetime

from storage import load_data, save_data


MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 64
PASSWORD_EXPIRATION_DAYS = 90


def get_required_input(prompt):
    """Request input and reject empty or whitespace-only values."""
    value = input(prompt).strip()

    if not value:
        print("Input cannot be empty.")
        return None

    return value


def save_changes(data):
    """Save changes and handle unexpected storage errors."""
    try:
        save_data(data)
        return True

    except (OSError, ValueError, TypeError, RuntimeError):
        print("Error: Unable to save changes.")
        return False


def valid_account(item):
    """Check whether an account contains the required fields."""
    if not isinstance(item, dict):
        return False

    required_fields = ["website", "username", "password"]

    return all(
        isinstance(item.get(field), str) and item[field].strip()
        for field in required_fields
    )


def add_password():
    website = get_required_input("Website: ")
    if website is None:
        return

    username = get_required_input("Username: ")
    if username is None:
        return

    password = input("Password: ")

    if not password.strip():
        print("Password cannot be empty.")
        return

    if len(password) < MIN_PASSWORD_LENGTH:
        print("Password must be at least 8 characters long.")
        return

    data = load_data()

    if any(
        valid_account(item)
        and item["website"].lower() == website.lower()
        and item["username"].lower() == username.lower()
        for item in data
    ):
        print("This account already exists.")
        return

    data.append({
        "website": website,
        "username": username,
        "password": password,
        "last_updated": datetime.now().isoformat()
    })

    if save_changes(data):
        print("Password saved successfully!")


def view_passwords():
    data = load_data()

    if not data:
        print("No passwords saved yet.")
        return

    print("\nSAVED PASSWORDS")
    print("----------------------")

    for item in data:
        if not valid_account(item):
            print("Warning: Invalid account record skipped.")
            continue

        print("Website:", item["website"])
        print("Username:", item["username"])
        print("Password: ********")
        print("----------------------")


def analyze_password_strength():
    password = input("Enter a sample password to analyze: ")

    if not password.strip():
        print("Password cannot be empty.")
        return

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

    if not password.strip():
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

        if not MIN_PASSWORD_LENGTH <= length <= MAX_PASSWORD_LENGTH:
            print("Password length must be between 8 and 64.")
            return

        characters = (
            string.ascii_lowercase
            + string.ascii_uppercase
            + string.digits
            + string.punctuation
        )

        password = [
            secrets.choice(string.ascii_lowercase),
            secrets.choice(string.ascii_uppercase),
            secrets.choice(string.digits),
            secrets.choice(string.punctuation)
        ]

        for _ in range(length - 4):
            password.append(secrets.choice(characters))

        secrets.SystemRandom().shuffle(password)

        print("\nGENERATED PASSWORD")
        print("--------------------------")
        print("".join(password))

    except ValueError:
        print("Please enter a valid number.")


def detect_common_password():
    common_passwords = {
        "123456", "password", "123456789",
        "12345678", "qwerty", "abc123",
        "password123", "admin", "admin123",
        "letmein", "welcome", "iloveyou",
        "111111", "000000", "123123"
    }

    password = input("Enter a sample password to check: ")

    if not password.strip():
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

    accounts = [item for item in data if valid_account(item)]

    if len(accounts) < 2:
        print("At least two valid saved accounts are needed.")
        return

    password_counts = {}

    for item in accounts:
        password = item["password"]
        password_counts[password] = password_counts.get(password, 0) + 1

    reused_passwords = [
        count for count in password_counts.values() if count > 1
    ]

    print("\nPASSWORD REUSE CHECK")
    print("--------------------------")

    if reused_passwords:
        print("WARNING: Password reuse detected!")

        for count in reused_passwords:
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

    search_term = get_required_input("Enter website name to search: ")

    if search_term is None:
        return

    search_term = search_term.lower()

    results = [
        item for item in data
        if valid_account(item)
        and search_term in item["website"].lower()
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

    website = get_required_input("Enter website name: ")
    if website is None:
        return

    username = get_required_input("Enter username: ")
    if username is None:
        return

    matching_accounts = [
        item for item in data
        if valid_account(item)
        and item["website"].lower() == website.lower()
        and item["username"].lower() == username.lower()
    ]

    if not matching_accounts:
        print("No matching account found.")
        return

    if len(matching_accounts) > 1:
        print("Multiple matching accounts found.")
        print("Please resolve the duplicate records first.")
        return

    confirmation = input(
        "Are you sure you want to delete this account? (yes/no): "
    ).strip().lower()

    if confirmation == "yes":
        data.remove(matching_accounts[0])

        if save_changes(data):
            print("Account deleted successfully!")

    elif confirmation == "no":
        print("Deletion cancelled.")

    else:
        print("Invalid confirmation. Deletion cancelled.")


def update_password():
    data = load_data()

    if not data:
        print("No passwords saved yet.")
        return

    website = get_required_input("Enter website name: ")
    if website is None:
        return

    username = get_required_input("Enter username: ")
    if username is None:
        return

    matching_accounts = [
        item for item in data
        if valid_account(item)
        and item["website"].lower() == website.lower()
        and item["username"].lower() == username.lower()
    ]

    if not matching_accounts:
        print("No matching account found.")
        return

    if len(matching_accounts) > 1:
        print("Multiple matching accounts found.")
        return

    new_password = input("Enter new password: ")

    if not new_password.strip():
        print("Password cannot be empty.")
        return

    if len(new_password) < MIN_PASSWORD_LENGTH:
        print("Password must be at least 8 characters long.")
        return

    matching_accounts[0]["password"] = new_password
    matching_accounts[0]["last_updated"] = datetime.now().isoformat()

    if save_changes(data):
        print("Password updated successfully!")


def export_password_report():
    data = load_data()

    if not data:
        print("No passwords available to export.")
        return

    try:
        with open(
            "password_report.csv",
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)
            writer.writerow(["Website", "Username"])

            for item in data:
                if valid_account(item):
                    writer.writerow([
                        item["website"],
                        item["username"]
                    ])

        print("Account report exported successfully!")
        print("File created: password_report.csv")
        print("Passwords were excluded from the report.")

    except (OSError, csv.Error, UnicodeError):
        print("Error: Could not export the account report.")

def check_password_expiration():
    data = load_data()

    if not data:
        print("No passwords saved yet.")
        return

    print("\nPASSWORD EXPIRATION CHECK")
    print("--------------------------")

    current_date = datetime.now()

    for item in data:
        if not valid_account(item):
            print("Invalid account record skipped.")
            continue

        website = item["website"]
        last_updated = item.get("last_updated")

        if not last_updated:
            print(website + ": Update date unavailable.")
            continue

        try:
            update_date = datetime.fromisoformat(last_updated)

            if update_date.tzinfo is not None:
                update_date = update_date.replace(tzinfo=None)

            if update_date > current_date:
                print(website + ": Invalid future update date.")
                continue

            age = current_date - update_date

            if age.days >= PASSWORD_EXPIRATION_DAYS:
                print(
                    website
                    + ": WARNING - Password is older than 90 days!"
                )
            else:
                remaining = PASSWORD_EXPIRATION_DAYS - age.days
                print(website + ": Password is up to date.")
                print("Days until expiration warning:", remaining)

        except (ValueError, TypeError):
            print(website + ": Invalid update date.")


def generate_security_audit():
    data = load_data()

    if not data:
        print("No passwords available for security auditing.")
        return

    common_passwords = {
        "123456", "password", "123456789",
        "12345678", "qwerty", "abc123",
        "password123", "admin", "admin123",
        "letmein", "welcome", "iloveyou",
        "111111", "000000", "123123"
    }

    total_accounts = 0
    weak_passwords = 0
    common_count = 0
    expired_count = 0

    password_counts = {}
    current_date = datetime.now()

    for item in data:
        if not valid_account(item):
            continue

        total_accounts += 1
        password = item["password"]

        # Check password strength.
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

        if score <= 2:
            weak_passwords += 1

        # Check common passwords.
        if password.lower() in common_passwords:
            common_count += 1

        # Count password usage.
        password_counts[password] = (
            password_counts.get(password, 0) + 1
        )

        # Check password age.
        last_updated = item.get("last_updated")

        if last_updated:
            try:
                update_date = datetime.fromisoformat(last_updated)

                if update_date.tzinfo is not None:
                    update_date = update_date.replace(tzinfo=None)

                if update_date <= current_date:
                    age = current_date - update_date

                    if age.days >= PASSWORD_EXPIRATION_DAYS:
                        expired_count += 1

            except (ValueError, TypeError):
                pass

    reused_count = sum(
        count for count in password_counts.values()
        if count > 1
    )

    print("\nPASSWORD SECURITY AUDIT REPORT")
    print("================================")
    print("Total accounts audited:", total_accounts)
    print("Weak passwords:", weak_passwords)
    print("Common passwords:", common_count)
    print("Accounts using reused passwords:", reused_count)
    print("Passwords older than 90 days:", expired_count)

    print("\nSECURITY ASSESSMENT")
    print("--------------------------")

    if total_accounts == 0:
        print("No valid accounts were available for auditing.")
        return

    issues = weak_passwords + common_count + expired_count

    if issues == 0 and reused_count == 0:
        print("GOOD: No issues were detected by this audit.")
    else:
        print("WARNING: Security issues were detected.")
        print("Review your passwords and update vulnerable accounts.")

    print("\nNote: This report does not display actual passwords.")
    print("================================")

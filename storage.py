import json
import os

from cryptography.fernet import InvalidToken
from security import encrypt_data, decrypt_data

FILE_NAME = "vault.json"
BACKUP_FILE = "vault_backup.json"


def validate_backup_data(data):
    if not isinstance(data, list):
        return False

    required_fields = ["website", "username", "password"]

    for item in data:
        if not isinstance(item, dict):
            return False

        for field in required_fields:
            if field not in item or not isinstance(item[field], str):
                return False

    return True


def read_data_file(filename):
    with open(filename, "rb") as file:
        raw_data = file.read()

    # Support existing plaintext vaults during migration.
    try:
        data = json.loads(raw_data.decode("utf-8"))
        return data, False
    except (UnicodeDecodeError, json.JSONDecodeError):
        pass

    # Otherwise, decrypt the encrypted file.
    decrypted_data = decrypt_data(raw_data)
    return json.loads(decrypted_data), True


def write_encrypted_data(filename, data):
    json_data = json.dumps(data, indent=4)
    encrypted_data = encrypt_data(json_data)

    with open(filename, "wb") as file:
        file.write(encrypted_data)


def load_data():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        data, encrypted = read_data_file(FILE_NAME)

        if not isinstance(data, list):
            print("Error: Vault data is invalid.")
            return []

        # Automatically encrypt an older plaintext vault.
        if not encrypted:
            write_encrypted_data(FILE_NAME, data)
            print("Existing vault successfully encrypted.")

        return data

    except (OSError, ValueError, json.JSONDecodeError, InvalidToken):
        print("Error: Unable to read the password vault.")
        return []


def save_data(data):
    if os.path.exists(FILE_NAME):
        try:
            existing_data, _ = read_data_file(FILE_NAME)

            if validate_backup_data(existing_data):
                write_encrypted_data(BACKUP_FILE, existing_data)
                print("Encrypted backup created successfully.")
            else:
                print("Warning: Existing data is invalid. Backup not updated.")

        except (OSError, ValueError, json.JSONDecodeError, InvalidToken):
            print("Warning: Existing vault could not be validated.")

    write_encrypted_data(FILE_NAME, data)
    print("Data encrypted and saved successfully.")


def restore_backup():
    if not os.path.exists(BACKUP_FILE):
        print("No backup file found.")
        return

    try:
        backup_data, _ = read_data_file(BACKUP_FILE)

        if not validate_backup_data(backup_data):
            print("Backup validation failed. Restoration cancelled.")
            return

        write_encrypted_data(FILE_NAME, backup_data)

        print("Backup validation successful.")
        print("Encrypted backup restored successfully!")

    except (OSError, ValueError, json.JSONDecodeError, InvalidToken):
        print("Unable to restore backup. The backup may be damaged.")
import json
import os
import shutil

FILE_NAME = "vault.json"
BACKUP_FILE = "vault_backup.json"


def load_data():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)


def validate_backup_data(data):
    if not isinstance(data, list):
        return False

    for item in data:
        if not isinstance(item, dict):
            return False

        required_fields = ["website", "username", "password"]

        for field in required_fields:
            if field not in item or not isinstance(item[field], str):
                return False

    return True


def save_data(data):
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                existing_data = json.load(file)

            if validate_backup_data(existing_data):
                shutil.copy2(FILE_NAME, BACKUP_FILE)
                print("Backup created successfully.")
            else:
                print("Warning: Existing data is invalid. Backup not updated.")

        except (json.JSONDecodeError, OSError):
            print("Warning: Could not validate existing data. Backup not updated.")

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

    print("Data saved successfully.")


def restore_backup():
    if not os.path.exists(BACKUP_FILE):
        print("No backup file found.")
        return

    try:
        with open(BACKUP_FILE, "r") as file:
            backup_data = json.load(file)

        if not validate_backup_data(backup_data):
            print("Backup validation failed. Restoration cancelled.")
            return

        shutil.copy2(BACKUP_FILE, FILE_NAME)

        print("Backup validation successful.")
        print("Password data restored successfully!")

    except (json.JSONDecodeError, OSError):
        print("Unable to restore backup. The backup file may be damaged.")
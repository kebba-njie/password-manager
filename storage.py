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


def save_data(data):
    if os.path.exists(FILE_NAME):
        shutil.copy2(FILE_NAME, BACKUP_FILE)

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

    print("Data saved successfully.")

    if os.path.exists(BACKUP_FILE):
        print("Backup created successfully.")


def restore_backup():
    if not os.path.exists(BACKUP_FILE):
        print("No backup file found.")
        return

    try:
        with open(BACKUP_FILE, "r") as file:
            backup_data = json.load(file)

        if not isinstance(backup_data, list):
            print("Backup file contains invalid data.")
            return

        shutil.copy2(BACKUP_FILE, FILE_NAME)

        print("Password data restored successfully!")

    except (json.JSONDecodeError, OSError):
        print("Unable to restore backup. The backup file may be damaged.")
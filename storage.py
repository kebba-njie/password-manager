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
    # Create a backup before overwriting existing data
    if os.path.exists(FILE_NAME):
        shutil.copy2(FILE_NAME, BACKUP_FILE)

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

    print("Data saved successfully.")
    if os.path.exists(BACKUP_FILE):
        print("Backup created successfully.")
import os
from cryptography.fernet import Fernet

KEY_FILE = "secret.key"


def load_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as file:
            return file.read()

    key = Fernet.generate_key()

    with open(KEY_FILE, "wb") as file:
        file.write(key)

    return key


def encrypt_data(data):
    key = load_key()
    cipher = Fernet(key)

    return cipher.encrypt(data.encode())


def decrypt_data(encrypted_data):
    key = load_key()
    cipher = Fernet(key)

    return cipher.decrypt(encrypted_data).decode()
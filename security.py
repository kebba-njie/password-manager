import os
import base64
import getpass

from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


SALT_FILE = "master.salt"
VERIFIER_FILE = "master.verifier"
LEGACY_KEY_FILE = "secret.key"

ITERATIONS = 600000

_cipher = None


def derive_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=ITERATIONS
    )

    key = kdf.derive(password.encode())
    return base64.urlsafe_b64encode(key)


def initialize_master_password():
    global _cipher

    if os.path.exists(SALT_FILE) and os.path.exists(VERIFIER_FILE):
        print("\nMASTER PASSWORD LOGIN")
        password = getpass.getpass("Enter master password: ")

        with open(SALT_FILE, "rb") as file:
            salt = file.read()

        key = derive_key(password, salt)
        cipher = Fernet(key)

        try:
            with open(VERIFIER_FILE, "rb") as file:
                verifier = file.read()

            if cipher.decrypt(verifier) != b"password-manager-verification":
                return False

            _cipher = cipher
            print("Master password accepted.")
            return True

        except InvalidToken:
            print("Incorrect master password.")
            return False

    print("\nCREATE MASTER PASSWORD")
    password = getpass.getpass("Create master password: ")

    if len(password) < 12:
        print("Master password must contain at least 12 characters.")
        return False

    confirmation = getpass.getpass("Confirm master password: ")

    if password != confirmation:
        print("Passwords do not match.")
        return False

    salt = os.urandom(16)
    key = derive_key(password, salt)
    cipher = Fernet(key)

    verifier = cipher.encrypt(b"password-manager-verification")

    with open(SALT_FILE, "wb") as file:
        file.write(salt)

    with open(VERIFIER_FILE, "wb") as file:
        file.write(verifier)

    _cipher = cipher

    print("Master password created successfully!")
    return True


def load_key():
    if not os.path.exists(LEGACY_KEY_FILE):
        raise FileNotFoundError("Legacy encryption key not found.")

    with open(LEGACY_KEY_FILE, "rb") as file:
        return file.read()


def encrypt_data(data):
    if _cipher is None:
        raise RuntimeError("Master password has not been initialized.")

    return _cipher.encrypt(data.encode())


def decrypt_data(encrypted_data):
    if _cipher is None:
        raise RuntimeError("Master password has not been initialized.")

    try:
        return _cipher.decrypt(encrypted_data).decode()

    except InvalidToken:
        # Support migration from the previous encryption system.
        legacy_cipher = Fernet(load_key())
        return legacy_cipher.decrypt(encrypted_data).decode()
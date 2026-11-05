# 🔐 Python Password Manager

A Python-based cybersecurity application designed to securely manage password credentials through encryption, master password authentication, password analysis, and automated security auditing.

## 📌 Project Overview

The Password Manager is a command-line application developed to demonstrate practical cybersecurity and secure programming concepts.

It allows users to store, retrieve, update, and manage their password credentials while incorporating security mechanisms designed to protect sensitive information.

The project also includes password strength analysis, encrypted storage, backup management, and security auditing.

## ✨ Features

### 🔑 Password Management

* Add and store password credentials.
* View saved accounts.
* Search for stored credentials.
* Update existing passwords.
* Delete saved credentials.
* Mask passwords when displaying account information.

### 🛡️ Security Features

* Master password authentication.
* Password-based encryption key derivation.
* Encrypted password storage.
* Secure password generation.
* Password strength analysis.
* Password entropy calculation.
* Common password detection.
* Password reuse detection.
* Password expiration monitoring.
* Input validation and error handling.

### 📊 Security Auditing

* Generate password security audit reports.
* Identify weak passwords.
* Detect commonly used passwords.
* Identify reused passwords.
* Check password expiration.

### 💾 Backup and Data Management

* Automatic password data backups.
* Backup restoration.
* Backup validation.
* CSV account report export.
* Password data import and export.
* Duplicate account detection during import.

## 🧰 Technologies Used

* **Python** — Application development.
* **Cryptography (Fernet)** — Encrypted password storage.
* **PBKDF2-HMAC-SHA256** — Master password-based key derivation.
* **CSV** — Data import and export.
* **JSON** — Password data management.
* **Unittest** — Automated testing.

## 📁 Project Structure

```text
password-manager/
│
├── main.py
├── manager.py
├── security.py
├── storage.py
├── test_manager.py
├── README.md
└── .gitignore
```

| File              | Description                                                   |
| ----------------- | ------------------------------------------------------------- |
| `main.py`         | Application entry point and main menu.                        |
| `manager.py`      | Password management and security features.                    |
| `security.py`     | Master password authentication and encryption key management. |
| `storage.py`      | Encrypted data storage, backups, and restoration.             |
| `test_manager.py` | Automated account validation tests.                           |
| `.gitignore`      | Excludes sensitive files and unnecessary project data.        |

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/kebba-njie/password-manager.git
```

### 2. Navigate into the project directory

```bash
cd password-manager
```

### 3. Install the required dependency

```bash
pip install cryptography
```

### 4. Run the application

```bash
python main.py
```

Follow the prompts to configure or enter your master password.

## 🧪 Running Automated Tests

Run the automated account validation tests using:

```bash
python -m unittest test_manager.py
```

The tests cover:

* Valid account acceptance.
* Missing website rejection.
* Empty password rejection.
* Invalid account type rejection.

## 🔒 Security Considerations

Security is a central focus of this project.

The application incorporates encrypted password storage, master password authentication, input validation, and protected local data files.

**Important security considerations:**

* Exported CSV files contain readable password information and must be kept private.
* Encryption keys, master password files, vault data, and backups should never be committed to GitHub.
* The application is an educational cybersecurity project and has not undergone an independent security audit.
* Users should maintain secure backups and protect their local system.

## 🎯 Project Objectives

This project demonstrates practical knowledge and implementation of:

* Secure software development.
* Password security principles.
* Cryptographic key management.
* Data encryption and protection.
* Input validation.
* Secure file handling.
* Automated software testing.
* Cybersecurity risk identification.

## 👨‍💻 Author

**Kebba Njie**

GitHub: [@kebba-njie](https://github.com/kebba-njie)

---

*Developed as a practical cybersecurity and secure programming portfolio project.*

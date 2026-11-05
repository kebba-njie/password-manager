import unittest

from manager import valid_account


class TestAccountValidation(unittest.TestCase):

    def test_valid_account(self):
        account = {
            "website": "google.com",
            "username": "testuser",
            "password": "StrongPass123!"
        }

        self.assertTrue(valid_account(account))

    def test_missing_website(self):
        account = {
            "username": "testuser",
            "password": "StrongPass123!"
        }

        self.assertFalse(valid_account(account))

    def test_empty_password(self):
        account = {
            "website": "google.com",
            "username": "testuser",
            "password": ""
        }

        self.assertFalse(valid_account(account))

    def test_invalid_account_type(self):
        account = "invalid account"

        self.assertFalse(valid_account(account))


if __name__ == "__main__":
    unittest.main()
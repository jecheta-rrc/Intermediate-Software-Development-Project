"""Unit tests for the Client class

   example usage:
            $ python -m unittest tests/test_client.py
"""

__Author__ = "Nkechi Echeta"
__Version__ = "1.0.0"

import unittest
from email_validator import EmailNotValidError
from client.client import Client

class TestClient(unittest.TestCase):
    """Unit tests for the Client class"""

    def setUp(self):

        # Set up runs before each test method runs
        # Create a valid instance of the Client class
        client_number = 1
        first_name = "John"
        last_name = "Doe"
        email_address = "johndoe@gmail.com"

        self.client = Client(client_number, first_name, last_name, email_address)

    def test_init_valid_instance(self):
        # Arrange
        client_number = 1
        first_name = "John"
        last_name = "Doe"
        email_address = "johndoe@gmail.com"

        # Act
        self.client = Client(client_number, first_name, last_name, email_address)

        # Assert
        self.assertEqual(1, self.client.client_number)
        self.assertEqual("John", self.client.first_name)
        self.assertEqual("Doe", self.client.last_name)
        self.assertEqual("johndoe@gmail.com", self.client.email_address)

    def test_init_invalid_client_number(self):
        # Arrange
        client_number = "1"
        first_name = "John"
        last_name = "Doe"
        email_address = "johndoe@gmail.com"

        # Assert
        with self.assertRaises(ValueError):
            Client(client_number, first_name, last_name, email_address)

    def test_init_invalid_first_name(self):
        # Arrange
        client_number = 1
        first_name = ""
        last_name = "Doe"
        email_address = "johndoe@gmail.com"

        # Assert
        with self.assertRaises(ValueError) as context:
            Client(client_number, first_name, last_name, email_address)
            
    def test_init_invalid_last_name(self):
        # Arrange
        client_number = 1
        first_name = "John"
        last_name = ""
        email_address = "johndoe@gmail.com"

        # Assert
        with self.assertRaises(ValueError) as context:
            Client(client_number, first_name, last_name, email_address)

    def test_init_invalid_email_address(self):
        # Arrange
        client_number = 1
        first_name = "John"
        last_name = "Doe"
        email_address = "johndoegmail.com"

        # Assert
        with self.assertRaises(EmailNotValidError):
            Client(client_number, first_name, last_name, email_address)

    def test_client_number_accessor_returns_correct_state(self):
        # Assert
        self.assertEqual(1, self.client.client_number)

    def test_first_name_accessor_returns_correct_state(self):
        # Assert
        self.assertEqual("John", self.client.first_name)

    def test_last_name_accessor_returns_correct_state(self):
        # Assert
        self.assertEqual("Doe", self.client.last_name)

    def test_email_address_accessor_returns_correct_state(self):
        # Assert
        self.assertEqual("johndoe@gmail.com", self.client.email_address)

    def test_str_returns_string_representation(self):
        # Act
        actual = str(self.client)

        # Assert
        expected = (f"{self.client.last_name}, {self.client.first_name}"
                    f"[{self.client.client_number}] - {self.client.email_address}")

        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()

"""Unit tests for the Client class.
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""

__author__ = "Nkechi Echeta"
__version__ = "1.0.0"

import unittest
from client.client import Client
from email_validator import EmailNotValidError

class TestClient(unittest.TestCase):
    """Test cases for the Client class."""

    def test_init_sets_attributes(self):
        # Arrange
        client_number = 1010
        first_name = "Susan"
        last_name = "Clark"
        email_address = "susanclark@pixell.com"

        # Act
        client = Client(client_number, first_name, last_name, email_address)

        # Assert
        self.assertEqual(client.client_number, client_number)
        self.assertEqual(client.first_name, first_name)
        self.assertEqual(client.last_name, last_name)
        self.assertEqual(client.email_address, email_address)

    def test_invalid_client_number_raises_exception(self):
        # Arrange
        client_number = "invalid"
        first_name = "Susan"
        last_name = "Clark"
        email_address = "susanclark@pixell.com"

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            Client(client_number, first_name, last_name, email_address)
        expected_message = "Client number must be an integer."
        self.assertEqual(str(context.exception), expected_message)

    def test_init_blank_first_name_raises_exception(self):
        # Arrange
        client_number = 1010
        first_name = " "
        last_name = "Clark"
        email_address = "susanclark@pixell.com"

        # Act
        with self.assertRaises(ValueError) as context:
            Client(client_number, first_name, last_name, email_address)

        # Assert
        expected_message = "First name cannot be blank."
        self.assertEqual(str(context.exception), expected_message)

    def test_init_blank_last_name_raises_exception(self):
        # Arrange
        client_number = 1010
        first_name = "Susan"
        last_name = " "
        email_address = "susanclark@pixell.com"

        # Act
        with self.assertRaises(ValueError) as context:
            Client(client_number, first_name, last_name, email_address)

        # Assert
        expected_message = "Last name cannot be blank."
        self.assertEqual(str(context.exception), expected_message)

    def test_init_invalid_email_sets_default_value(self):
        # Arrange
        client_number = 1010
        first_name = "Susan"
        last_name = "Clark"
        invalid_email_address = "invalid-email"

        # Act
        client = Client(client_number, first_name, last_name, invalid_email_address)

        # Assert
        expected = "email@pixell-river.com"
        actual = client.email_address
        self.assertEqual(expected, actual)

    def test_client_number_accessor(self):
        # Arrange
        client_number = 1010
        first_name = "Susan"
        last_name = "Clark"
        email_address = "susanclark@pixell.com"
        client = Client(client_number, first_name, last_name, email_address)

        # Act
        result = client.client_number

        # Assert
        self.assertEqual(result, client_number)

    def test_first_name_accessor(self):
        # Arrange
        client_number = 1010
        first_name = "Susan"
        last_name = "Clark"
        email_address = "susanclark@pixell.com"
        client = Client(client_number, first_name, last_name, email_address)

        # Act
        result = client.first_name

        # Assert
        self.assertEqual(result, first_name)

    def test_last_name_accessor(self):
        # Arrange
        client_number = 1010
        first_name = "Susan"
        last_name = "Clark"
        email_address = "susanclark@pixell.com"
        client = Client(client_number, first_name, last_name, email_address)

        # Act
        result = client.last_name

        # Assert
        self.assertEqual(result, last_name)

    def test_email_address_accessor(self):
        # Arrange
        client_number = 1010
        first_name = "Susan"
        last_name = "Clark"
        email_address = "susanclark@pixell.com"
        client = Client(client_number, first_name, last_name, email_address)

        # Act
        result = client.email_address

        # Assert
        self.assertEqual(result, email_address)

    def test_str_method_returns_correct_format(self):
        # Arrange
        client_number = 1010
        first_name = "Susan"
        last_name = "Clark"
        email_address = "susanclark@pixell.com"
        client = Client(client_number, first_name, last_name, email_address)

        # Act
        result = str(client)

        # Assert
        expected = "Clark, Susan [1010] - susanclark@pixell.com"
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()

"""Unit tests for the Client class.
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""

__author__ = "Nkechi Echeta"
__version__ = "1.0.0"

import unittest
from client.client import Client

class TestClient(unittest.TestCase):
    """Unit tests for the Client class."""

    def test_init_sets_attributes(self):
        """Test that the __init__ method correctly sets attributes."""
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
        first_name = "Tehila"
        last_name = "Akpabio"
        email_address = "tehila.akpabio@example.com"
    
        # Act
        with self.assertRaises(ValueError) as context:
            Client(client_number, first_name, last_name, email_address)
    
        # Assert
        expected_message = "Client number must be an integer."
        self.assertEqual(str(context.exception), expected_message)

    def test_init_blank_first_name_raises_exception(self):
        # Arrange
        client_number = 1010
        first_name = "   "  # Blank after stripping whitespace
        last_name = "Akpabio"
        email_address = "test@example.com"

        # Act
        with self.assertRaises(ValueError) as context:
            Client(client_number, first_name, last_name, email_address)
        
        #Assert
        expected_message = "First name cannot be blank."
        self.assertEqual(str(context.exception), expected_message)

if __name__ == "__main__":
    unittest.main()

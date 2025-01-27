"""
A client program written to verify correctness of the BankAccount and Client 
classes.
"""

__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Nkechi Echeta"

from bank_account.bank_account import BankAccount
from client.client import Client


def main():
    """Test the functionality of the methods encapsulated in the BankAccount and 
    Client classes.
    """
    try:
        client = Client(client_number=12345, first_name="Susan", last_name="Clark", 
        email_address="susanclark@pixell.com")
        print("Client created successfully.")
    except Exception as e:
        print(f"Error creating Client: {e}")

    bank_account = None

    try:
        bank_account = BankAccount(account_number=1, client_number=client.client_number, balance=1000.50)
        print("BankAccount created successfully.")
    except Exception as e:
        print(f"Error creating BankAccount: {e}")

    try:
        invalid_bank_account = BankAccount(account_number=2, client_number=client.client_number, balance="invalid_balance")
    except Exception as e:
        print(f"Error creating BankAccount with invalid balance: {e}")

    if client:
        print(f"Client: {client}")
    if bank_account:
        print(f"BankAccount: {bank_account}")

    try:
        bank_account.deposit("not_a_number")
    except Exception as e:
        print(f"Error during deposit: {e}")

    try:
        bank_account.deposit(-50)
    except Exception as e:
        print(f"Error during deposit: {e}")

    try:
        bank_account.withdraw(200.00)
        print(f"After withdrawal, balance is: {bank_account.balance}")
    except Exception as e:
        print(f"Error during withdrawal: {e}")

    try:
        bank_account.withdraw("not_a_number")
    except Exception as e:
        print(f"Error during withdrawal: {e}")

    try:
        bank_account.withdraw(-50)
    except Exception as e:
        print(f"Error during withdrawal: {e}")

    try:
        bank_account.withdraw(5000.00)
    except Exception as e:
        print(f"Error during withdrawal: {e}")

    if bank_account:
        print(f"Final BankAccount: {bank_account}")


if __name__ == "__main__":
    main()

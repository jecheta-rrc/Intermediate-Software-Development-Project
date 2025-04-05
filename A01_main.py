""""A client program written to verify correctness of the BankAccount and 
Client classes.
"""

__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Nkechi Echeta"

from bank_account.bank_account import BankAccount
from client.client import Client

def main():
    """Test the functionality of the methods encapsulated 
    in the BankAccount and Client classes.
    """

    try:
        # 1. Code a statement which creates a valid instance of the 
        # Client class.
        # Use your own unique valid values for the inputs to the class.
        client = Client(client_number=12345, first_name="John", last_name="Doe", 
                        email_address="john.doe@example.com")

        # 2. Declare a variable that could store a BankAccount instance.
        # Define the variable with an initial value of None.
        bank_account = None

        # 3. Using the variable declared in step 2, code a statement
        # to instantiate a BankAccount object.
        # Use any integer value for the BankAccount number.
        # Use the client number used to create the Client object in step 
        # 1 for the
        # BankAccount's client number.
        # Use a floating point value for the balance.
        bank_account = BankAccount(account_number=67890, client_number=client.client_number, 
                                   balance=1000.0)

        # 4. Code a statement which creates an instance of the BankAccount 
        # class.
        # Use any integer value for the BankAccount number.
        # Use the client_number used to create the Client object in step 
        # 1 for the
        # BankAccount's client_number.
        # Use an INVALID value (non-float) for the balance.
        try:
            invalid_bank_account = BankAccount(account_number=67891, 
                                               client_number=client.client_number, balance="invalid_balance")
        except ValueError as e:
            print(f"Exception caught: {e}")

        # 5. Code a statement which prints the Client instance created in 
        # step 1.
        # Code a statement which prints the BankAccount instance created 
        # in step 3.
        print(client)
        print(bank_account)

        # 6. Attempt to deposit a non-numeric value into the BankAccount 
        # created in step 3.
        try:
            bank_account.deposit("non_numeric_value")
        except ValueError as e:
            print(f"Exception caught: {e}")

        # 7. Attempt to deposit a negative value into the BankAccount 
        # created in step 3.
        try:
            bank_account.deposit(-100)
        except ValueError as e:
            print(f"Exception caught: {e}")

        # 8. Attempt to withdraw a valid amount of your choice from the 
        # BankAccount created in step 3.
        try:
            bank_account.withdraw(100)
        except ValueError as e:
            print(f"Exception caught: {e}")

        # 9. Attempt to withdraw a non-numeric value from the BankAccount 
        # created in step 3.
        try:
            bank_account.withdraw("non_numeric_value")
        except ValueError as e:
            print(f"Exception caught: {e}")

        # 10. Attempt to withdraw a negative value from the BankAccount 
        # created in step 3.
        try:
            bank_account.withdraw(-100)
        except ValueError as e:
            print(f"Exception caught: {e}")

        # 11. Attempt to withdraw a value from the BankAccount created 
        # in step 3 which
        # exceeds the current balance of the account.
        try:
            bank_account.withdraw(2000)
        except ValueError as e:
            print(f"Exception caught: {e}")

        # 12. Code a statement which prints the BankAccount instance 
        # created in step 3.
        print(bank_account)

    except Exception as e:
        print(f"Exception caught: {e}")

if __name__ == "__main__":
    main()

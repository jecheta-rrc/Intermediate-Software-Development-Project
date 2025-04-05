"""A client program written to verify implementation of the Observer Pattern.
"""

__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Nkechi Echeta"

# 1. Import all BankAccount types using the bank_account package
#    Import date
#    Import Client
import os
from datetime import date
from client.client import Client
from bank_account.chequing_account import ChequingAccount
from bank_account.savings_account import SavingsAccount

# Set up the output directory for storing observer emails
OUTPUT_DIR = "output"
EMAIL_FILE = os.path.join(OUTPUT_DIR, "observer_emails.txt")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# 2. Create Client objects
client1 = Client(101, "Alice", "Johnson", "alice@example.com")
client2 = Client(102, "Bob", "Smith", "bob@example.com")

# 3a. Create a ChequingAccount object with data of your choice, using the client_number of client1.
chequing_account = ChequingAccount(
    account_number=12345, 
    client_number=101, 
    balance=500, 
    date_created=date.today(), 
    overdraft_limit=200,  # ✅ Added overdraft_limit
    overdraft_rate=0.05  # ✅ Added overdraft_rate
)

# 3b. Create a SavingsAccount object with data of your choice, using the client_number of client1.
savings_account = SavingsAccount(
    account_number=67890, 
    client_number=101, 
    balance=1000, 
    date_created=date.today(), 
    minimum_balance=200  # ✅ Removed service_charge_strategy
)

# 5b. Create a second SavingsAccount object with data of your choice, using the client_number of client2.
savings_account_2 = SavingsAccount(
    account_number=34567, 
    client_number=102, 
    balance=800, 
    date_created=date.today(), 
    minimum_balance=150  # ✅ Removed service_charge_strategy
)

# 4. Attach clients to their accounts
chequing_account.attach(client1)
savings_account.attach(client1)
savings_account_2.attach(client2)

# 5. Perform transactions
for account in [chequing_account, savings_account, savings_account_2]:
    try:
        account.deposit(5000)
        account.withdraw(1000)
        account.deposit(12000)
    except ValueError as e:
        print(f"Error: {e}")

# Print observer emails for verification
with open(EMAIL_FILE, "r") as file:
    print("Observer Emails Log:")
    print(file.read())


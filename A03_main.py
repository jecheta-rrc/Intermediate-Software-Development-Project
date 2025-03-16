"""
Description: A client program written to verify implementation 
of the Observer Pattern.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

# 1.  Import all BankAccount types using the bank_account package
# Import date
# Import Client
from abc import ABC, abstractmethod
from datetime import datetime, date
from typing import TYPE_CHECKING
from patterns.observer.subject import Subject
from bank_account.bank_account import BankAccount
from datetime import date
from patterns.strategy.overdraft_strategy import OverdraftStrategy
from datetime import date, timedelta
from bank_account.bank_account import BankAccount
from patterns.strategy.management_fee_strategy import ManagementFeeStrategy
from bank_account.bank_account import BankAccount
from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy
from patterns.observer.observer import Observer
from datetime import datetime
from utility.file_utils import simulate_send_email

# 2. Create a Client object with data of your choice.
client1 = Client(290128, "Tehilah", "Akpabio", "tehilah.akpabio@gmail.com")

# 3a. Create a ChequingAccount object with data of your choice, using the client_number 
# of the client created in step 2.
# 3b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in step 2.
chequing_account = ChequingAccount(
    account_number=2001,
    client_number=290128,
    balance=500.00,
    date_created=date(2024, 3, 16),
    overdraft_limit=-200.00,
    overdraft_rate=0.05
)

savings_account = SavingsAccount(
    account_number=2002,
    client_number=290128,
    balance=1500.00,
    date_created=date(2024, 3, 16),
    minimum_balance=100.00
)

# 4 The ChequingAccount and SavingsAccount objects are 'Subject' objects.
# The Client object is an 'Observer' object.  
# 4a.  Attach the Client object (created in step 1) to the ChequingAccount object (created in step 2).
# 4a.  Attach the Client object (created in step 1) to the SavingsAccount object (created in step 2).
chequing_account.attach(client1)
savings_account.attach(client1)

# 5a. Create a second Client object with data of your choice.
# 5b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in this step.
client2 = Client(290129, "Kamsi", "Akpabio", "kamsi.akpabio@gmail.com")

savings_account2 = SavingsAccount(
    account_number=2003,
    client_number=290129,
    balance=700.00,
    date_created=date(2024, 3, 16),
    minimum_balance=200.00
)

savings_account2.attach(client2)

# 6. Use the ChequingAccount and SavingsAccount objects created 
# in steps 3 and 5 above to perform transactions (deposits and withdraws) 
# which would cause the Subject (BankAccount) to notify the Observer 
# (Client) as well as transactions that would not 
# cause the Subject to notify the Observer.  Ensure each 
# BankAccount object performs at least 3 transactions.
# REMINDER: the deposit() and withdraw() methods can raise exceptions
# ensure the methods are invoked using proper exception handling such 
# that any exception messages are printed to the console.
# Transaction 1: Deposit into ChequingAccount
try:
    chequing_account.deposit(1000.00)
except ValueError as e:
    print(f"Error: {e}")

# Transaction 2: Withdraw an amount that will trigger a low balance warning
try:
    chequing_account.withdraw(1700.00) 
except ValueError as e:
    print(f"Error: {e}")

# Transaction 3: Large Transaction triggering observer notifications
try:
    savings_account.deposit(12000.00)
except ValueError as e:
    print(f"Error: {e}")

"""A client program written to verify correctness of the BankAccount subclasses.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Nkechi Echeta"

from bank_account.chequing_account import ChequingAccount
from bank_account.savings_account import SavingsAccount
from bank_account.investment_account import InvestmentAccount 
from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy
from patterns.strategy.management_fee_strategy import ManagementFeeStrategy
from datetime import date
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from patterns.strategy.overdraft_strategy import OverdraftStrategy

# 2. Create an instance of a ChequingAccount with a balance below the overdraft limit
chequing_account = ChequingAccount(
    account_number=1001, 
    client_number=5001, 
    balance=-150.0, 
    date_created=date(2024, 2, 1), 
    overdraft_limit=-100.0, 
    overdraft_rate=0.05
)

# 3. Print the ChequingAccount and its service charges
print(chequing_account)
print("Service Charges:", chequing_account.get_service_charge())

# 4. Deposit enough money to avoid overdraft fees
chequing_account.deposit(100.0)
print(chequing_account)
print("Service Charges:", chequing_account.get_service_charge())

print("===================================================")

# 5. Create an instance of a SavingsAccount with a balance above the minimum balance
savings_account = SavingsAccount(
    account_number=1002, 
    client_number=5002, 
    balance=200.0, 
    date_created=date(2024, 1, 15), 
    minimum_balance=50.0
)

# 6. Print the SavingsAccount and its service charges
print(savings_account)
print("Service Charges:", savings_account.get_service_charge())

# 7. Withdraw enough money to drop below the minimum balance
savings_account.withdraw(160.0)
print(savings_account)
print("Service Charges:", savings_account.get_service_charge())

print("===================================================")

# 8. Create an instance of an InvestmentAccount with a date created within the last 10 years
investment_account_recent = InvestmentAccount(
    account_number=1003, 
    client_number=5003, 
    balance=5000.0, 
    date_created=date(2018, 6, 1), 
    management_fee=25.0
)

# 9. Print the recent InvestmentAccount and its service charges
print(investment_account_recent)
print("Service Charges:", investment_account_recent.get_service_charge())

# 10. Create an instance of an InvestmentAccount with a date created more than 10 years ago
investment_account_old = InvestmentAccount(
    account_number=1004, 
    client_number=5004, 
    balance=10000.0, 
    date_created=date(2010, 3, 20), 
    management_fee=30.0
)

# 11. Print the old InvestmentAccount and its service charges
print(investment_account_old)
print("Service Charges:", investment_account_old.get_service_charge())

print("===================================================")

# 12. Withdraw the service charges from each account
chequing_account.withdraw(chequing_account.get_service_charge())
savings_account.withdraw(savings_account.get_service_charge())
investment_account_recent.withdraw(investment_account_recent.get_service_charge())
investment_account_old.withdraw(investment_account_old.get_service_charge())

# 13. Print each account after withdrawing service charges
print(chequing_account)
print(savings_account)
print(investment_account_recent)
print(investment_account_old)

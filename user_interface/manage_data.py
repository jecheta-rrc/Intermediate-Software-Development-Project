"""Implement the load_data function to read and parse data from 
clients.csv and accounts.csv.
"""

__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Nkechi Echeta"

import os
import sys
import csv
from datetime import datetime
import logging

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from client.client import Client
from bank_account.chequing_account import ChequingAccount
from bank_account.investment_account import InvestmentAccount
from bank_account.savings_account import SavingsAccount
from bank_account.bank_account import BankAccount

# *******************************************************************************
# GIVEN LOGGING AND FILE ACCESS CODE
 
root_dir = os.path.dirname(os.path.dirname(__file__))
 
log_dir = os.path.join(root_dir, 'logs')
os.makedirs(log_dir, exist_ok = True)
log_file_path = os.path.join(log_dir, 'manage_data.log')
logging.basicConfig(filename=log_file_path, filemode='a',
                    format='%(name)s - %(levelname)s - %(message)s\n\n')
data_dir = os.path.join(root_dir, 'data')
clients_csv_path = os.path.join(data_dir, 'clients.csv')
accounts_csv_path = os.path.join(data_dir, 'accounts.csv')
 
# END GIVEN LOGGING AND FILE ACCESS CODE
# *******************************************************************************

def load_data()->tuple[dict,dict]:
    """Populates a client dictionary and an account dictionary with 
    corresponding data from files within the data directory.
    
    Returns:
        tuple containing client dictionary and account dictionary.
    """
    
    client_listing = {}
    accounts = {}

    # READ CLIENT DATA 
    with open(clients_csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for record in reader:
            try:
                client_number = int(record['client_number'])
                first_name = record['first_name'].strip()
                last_name = record['last_name'].strip()
                email = record['email_address'].strip()

                if not first_name:
                    raise ValueError("First Name cannot be blank.")

                client = Client(client_number, first_name, last_name, email)
                client_listing[client_number] = client
            
            except Exception as e:
                logging.error(f"Unable to create client: {e}")

    # READ ACCOUNT DATA
    with open(accounts_csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)  
        
        for record in reader:
            try:
                account_number = int(record['account_number'])
                client_number = int(record['client_number'])
                balance = float(record['balance'])
                date_created = datetime.strptime(
                    record['date_created'],
                    '%Y-%m-%d'
                ).date()
                account_type = record['account_type'].strip()

                if account_type == "ChequingAccount":
                    overdraft_limit = float(record['overdraft_limit'])
                    overdraft_rate = float(record['overdraft_rate'])
                    account = ChequingAccount(account_number, client_number, 
                                            balance, date_created, 
                                            overdraft_limit, overdraft_rate)

                elif account_type == "InvestmentAccount":
                    account = InvestmentAccount(account_number, client_number, 
                                                balance, date_created)

                elif account_type == "SavingsAccount":
                    minimum_balance = float(record['minimum_balance'])
                    account = SavingsAccount(account_number, client_number, 
                                            balance, date_created, 
                                            minimum_balance)

                else:
                    logging.error("Not a valid account type.")
                    continue

                if client_number in client_listing:
                    accounts[account_number] = account
                else:
                    logging.error(
                        f"Bank Account: {account_number} "
                        f"contains invalid Client Number: {client_number}"
                    )

            except Exception as e:
                logging.error(f"Unable to create bank account: {e}")

    # RETURN STATEMENT
    return client_listing, accounts

def update_data(updated_account: BankAccount) -> None:
    """A function to update the accounts.csv file with balance data provided in 
    the BankAccount argument.
    
    Args:
        updated_account (BankAccount): A bank account containing an updated 
        balance.
    """
    updated_rows = []

    with open(accounts_csv_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        fields = reader.fieldnames

        for row in reader:
            if int(row['account_number']) == updated_account.account_number:
                row['balance'] = updated_account.balance
            updated_rows.append(row)

    with open(accounts_csv_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(updated_rows)

# GIVEN TESTING SECTION:
if __name__ == "__main__":
    clients,accounts = load_data()

    print("=========================================")
    for client in clients.values():
        print(client)
        print(f"{client.client_number} Accounts\n=============")
        for account in accounts.values():
            if account.client_number == client.client_number:
                print(f"{account}\n")
        print("=========================================")
        
"""This defines the AccountDetailsWindow class."""

__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Nkechi Echeta"

from copy import copy
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal
from ui_superclasses.details_window import DetailsWindow
from bank_account.bank_account import BankAccount

class AccountDetailsWindow(DetailsWindow):
    """A class used to display account details and perform bank account 
    transactions.
    """
    
    balance_updated = Signal(BankAccount)

    def __init__(self, account: BankAccount) -> None:
        """
        Initializes a new instance of the ExtendedAccountDetails window.

        Args:
            account (BankaAccount): The bank account to be displayed and 
            modified.
        """

        super().__init__()

        if not isinstance(account, BankAccount):
            self.reject()
            return

        self.account = copy(account)

        self.account_number_label.setText(str(self.account.account_number))

        self.balance_label.setText(f"${self.account.balance:,.2f}")

        self.deposit_button.clicked.connect(self.__on_apply_transaction)

        self.withdraw_button.clicked.connect(self.__on_apply_transaction)

        self.exit_button.clicked.connect(self.__on_exit)

    def __on_apply_transaction(self):
        """Attempts to apply a transaction (deposit or withdrawal) and emit 
        update signal.
        """

        try:
            amount = float(self.transaction_amount_edit.text())
        except ValueError:
            QMessageBox.information(
                self, 
                "Invalid Data", 
                "Amount must be numeric."
            )
            self.transaction_amount_edit.setFocus()
            return

        try:
            sender = self.sender()
            transaction_type = ""

            if sender == self.deposit_button:
                transaction_type = "Deposit"
                self.account.deposit(amount)

            elif sender == self.withdraw_button:
                transaction_type = "Withdraw"
                self.account.withdraw(amount)
                
                if amount > self.account.balance:
                    raise ValueError("Insufficient funds for withdrawal.")

                self.account.withdraw(amount)

            else:
                QMessageBox.warning(
                    self, 
                    "Unknown Action", 
                    "Unknown transaction source."
                )
                return

            self.balance_label.setText(f"${self.account.balance:,.2f}")

            self.transaction_amount_edit.clear()
            self.transaction_amount_edit.setFocus()

            self.balance_updated.emit(self.account)

        except Exception as e:
            QMessageBox.information(self, f"{transaction_type} Failed", str(e))
            self.transaction_amount_edit.clear()
            self.transaction_amount_edit.setFocus()

    def __on_exit(self):
        """Closes the dialog window."""
        
        self.close()

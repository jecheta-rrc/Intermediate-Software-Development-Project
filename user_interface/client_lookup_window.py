"""This defines the ClientLookupWindow class."""

__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Nkechi Echeta"

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Slot
from ui_superclasses.lookup_window import LookupWindow
from user_interface.manage_data import load_data
from user_interface.account_details_window import AccountDetailsWindow


class ClientLookupWindow(LookupWindow):
    """Represents a window that allows for client lookup and account viewing."""

    def __init__(self):
        """Initializes the window, loads client/account data, and connects signals."""
        super().__init__()

        self.client_listing, self.accounts = load_data()

        self.lookup_button.clicked.connect(self.on_lookup_client)
        self.client_number_edit.textChanged.connect(self.on_text_changed)
        self.account_table.cellClicked.connect(self.on_select_account)
        self.filter_button.clicked.connect(self.on_filter_clicked)  # NEW

    def on_lookup_client(self):
        """Handles the logic when the lookup button is clicked."""
        raw_input = self.client_number_edit.text().strip()

        if not raw_input:
            QMessageBox.warning(self, "Missing Input", "Please enter a client number.")
            self.reset_display()
            return

        try:
            client_number = int(raw_input)
        except ValueError:
            QMessageBox.information(self, "Input Error",
                                     "The client number must be a numeric value.")
            self.reset_display()
            return

        if client_number not in self.client_listing:
            QMessageBox.information(self, "Not Found",
                                     f"Client number: {client_number} not found.")
            self.reset_display()
            return

        client = self.client_listing[client_number]
        self.client_info_label.setText(f"{client.first_name} {client.last_name}")
        self.account_table.setRowCount(0)

        for account in self.accounts.values():
            if account.client_number == client_number:
                row_position = self.account_table.rowCount()
                self.account_table.insertRow(row_position)

                account_number_item = QTableWidgetItem(str(account.account_number))
                balance_item = QTableWidgetItem(f"${account.balance:,.2f}")
                date_item = QTableWidgetItem(str(account.date_created))
                type_item = QTableWidgetItem(account.__class__.__name__)

                self.account_table.setItem(row_position, 0, account_number_item)
                self.account_table.setItem(row_position, 1, balance_item)
                self.account_table.setItem(row_position, 2, date_item)
                self.account_table.setItem(row_position, 3, type_item)

        self.account_table.resizeColumnsToContents()
        self.filter_button.setEnabled(True)  # ✅ Enable filter button
        self.toggle_filter(False)  # Reset filter state

    def on_text_changed(self):
        """Clears the account table when client number text is changed."""
        self.account_table.setRowCount(0)

    @Slot(int, int)
    def on_select_account(self, row: int, column: int):
        """Opens the account details dialog based on selected row."""
        account_item = self.account_table.item(row, 0)

        if account_item is None or not account_item.text():
            QMessageBox.information(self, "Invalid Selection", "Please select a valid record.")
            return

        account_number = int(account_item.text())
        if account_number not in self.accounts:
            QMessageBox.information(self, "No Bank Account", "Bank Account selected does not exist.")
            return

        account = self.accounts[account_number]
        details_window = AccountDetailsWindow(account)
        details_window.balance_updated.connect(self.update_data)
        details_window.exec()

    def update_data(self, account):
        """Updates the account information in the table and internal data."""
        for row in range(self.account_table.rowCount()):
            table_account_number = self.account_table.item(row, 0)
            if table_account_number and int(table_account_number.text()) == account.account_number:
                self.account_table.setItem(
                    row,
                    1,
                    QTableWidgetItem(f"${account.balance:,.2f}")
                )
                break

        self.accounts[account.account_number] = account

        from user_interface.manage_data import update_data
        update_data(account)

    def on_filter_clicked(self):
        """Filters the account_table based on user input."""
        if self.filter_button.text() == "Apply Filter":
            filter_column = self.filter_combo_box.currentIndex()
            filter_text = self.filter_edit.text().strip().lower()

            for row in range(self.account_table.rowCount()):
                item = self.account_table.item(row, filter_column)
                if item and filter_text in item.text().lower():
                    self.account_table.setRowHidden(row, False)
                else:
                    self.account_table.setRowHidden(row, True)

            self.toggle_filter(True)
        else:
            self.toggle_filter(False)

    def toggle_filter(self, filter_on: bool):
        """Toggles the filter UI elements and updates the filter label and button."""
        if filter_on:
            self.filter_button.setText("Reset")
            self.filter_combo_box.setEnabled(False)
            self.filter_edit.setEnabled(False)
            self.filter_label.setText("Data is Currently Filtered")
        else:
            self.filter_button.setText("Apply Filter")
            self.filter_combo_box.setEnabled(True)
            self.filter_edit.setEnabled(True)
            self.filter_edit.setText("")
            self.filter_combo_box.setCurrentIndex(0)

            for row in range(self.account_table.rowCount()):
                self.account_table.setRowHidden(row, False)

            self.filter_label.setText("Data is Not Currently Filtered")

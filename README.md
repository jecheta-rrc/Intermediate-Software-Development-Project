# Intermediate Software Development Automated Teller Project

This project will be developed over the course of several assignments. Each assignment will build on
the work done in the previous assignment(s). Ultimately, an entire system will be created to manage
bank transactions for clients who have one or more bank accounts.

## Author

Nkechi Echeta

## Assignment

Assignment 1: Bank Account Management and this assignment involves creating classes and testing for managing a bank account and its associated operations.

Assignment 2: This assignment will focus on inheritance, abstraction, and polymorphism. I created a hierarchy of classes that demonstrate these object-oriented principles, allowing for code reuse and flexibility in the overall system design.

Assignment 3: This assignment will focus on design patterns, specifically the Singleton and Observer patterns. I will implement these patterns in the context of the bank account system to improve the overall design and functionality of the system.

## Encapsulation

Encapsulation in the BankAccount and Transaction classes was achieved as follows:

- Key attributes like _account_number, _balance, and_client_number were made private using a single underscore prefix to restrict direct access.
- Getter methods (@property) were used to retrieve private attributes, while public methods like
deposit() and withdraw() controlled modifications.
- Validation logic in methods ensured data integrity by rejecting invalid inputs, such as negative deposits or withdrawals exceeding the balance.
- By encapsulating functionality within class methods, external code interacts with these classes
only through predefined interfaces, ensuring data security and consistency.
  
## Polymorphism

Polymorphism in object-oriented programming allows different classes to implement the same method in different ways. In the BankAccount class and its subclasses (ChequingAccount, SavingsAccount, InvestmentAccount), polymorphism is primarily achieved through method overriding.

## Strategy Pattern

The Strategy Pattern is used in this application to handle different types of service charges
dynamically based on the type of bank account.Instead of hardcoding the service charge calculations
inside each account class, we define separate strategy classes that handle these calculations. This
allows us to easily change or extend the logic without modifying the core account classes.

## Observer Pattern

The Observer Pattern in this application ensures that bank clients receive real-time notifications
about significant account activities. The BankAccount class acts as the Subject, maintaining a list
of observers (clients) and notifying them of important events. The Client class, as an Observer, implements the update() method to receive alerts when a large transaction occurs or when the account balance drops below a set threshold. This design allows for a flexible and decoupled notification
system, improving real-time communication between bank accounts and clients.

Assignment 4: Implementation of the Observer Pattern with Event-Driven GUI Components using PySide6.

## Event-Driven Programming Paradigm

This application follows the Event-Driven Programming Paradigm by responding to user interactions and internal signals through a series of event handlers and slots.

Key event-driven features include:

- PySide6 Signals and Slots: The application uses custom signals (e.g., 'balance_updated') to notify components when a transaction is completed, allowing the UI to refresh automatically without polling.
- GUI Interactions: Buttons like 'lookup_button' and input fields such as 'client_number_edit' trigger event-handling methods when users enter values or click buttons.
- Dynamic Updates: The 'AccountDetailsWindow' emits signals when transactions are applied, and these signals are connected to slots (e.g., 'update_data') in the 'ClientLookupWindow', which updates the account table and saves changes to the file.
- Error Handling and Validation: User input errors (e.g., invalid client numbers or non-numeric values) trigger events that display 'QMessageBox' alerts and guide the user.

This approach ensures the application is reactive, user-friendly, and maintainable, as components only respond to specific events rather than running in a continuous loop.

Assignment 5: Assignment 5: Filtering, Documentation, and Distribution – Enhanced the GUI with a filtering feature for account listings, generated HTML documentation using Sphinx, and packaged the application into a distributable installer using PyInstaller and Inno Setup.

## Filtering

The filtering feature was incorporated into the Client Lookup Window to enhance user interaction and data accessibility.

Once a valid client number is entered, a list of accounts is displayed. The filtering section allows the user to narrow down this list using a combination of:

- A dropdown menu (filter_combo_box) to select the filter criteria (e.g., Account Number, Balance, Date Created, Account Type).
- A text input field (filter_edit) where the user types a keyword or number to match.
- A button (filter_button) to apply or reset the filter.
- A status label (filter_label) to indicate whether the data is currently filtered.

Clicking "Apply Filter" hides all rows that do not match the typed input for the selected column. Clicking "Reset" clears the input and reveals all rows.

This functionality is implemented through the on_filter_clicked() and toggle_filter(filter_on: bool) methods in client_lookup_window.py. It uses QTableWidget.setRowHidden() to dynamically show or hide rows based on the match.

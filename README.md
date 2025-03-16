# Intermediate Software Development Automated Teller Project

This project will be developed over the course of several assignments. Each assignment will build on 
the work done in the previous assignment(s). Ultimately, an entire system will be created to manage 
bank transactions for clients who have one or more bank accounts.

## Author

Nkechi Echeta

## Assignment

Assignment 1: Bank Account Management and this assignment involves creating classes and testing for managing a bank account and its associated operations.

Assignment 2: This assignment will focus on inheritance, abstraction, and polymorphism. I created a hierarchy of classes that demonstrate these object-oriented principles, allowing for code reuse and flexibility in the overall system design.

Assignment 3: 

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

For example:

ChequingAccount uses the OverdraftStrategy to calculate service charges based on overdraft limits and rates.
InvestmentAccount applies the ManagementFeeStrategy to determine charges based on account age and management fees.

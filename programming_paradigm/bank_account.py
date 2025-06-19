# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0.0):
        # Initialize account_balance, defaulting to 0.0 if not provided
        if not isinstance(initial_balance, (int, float)):
            raise TypeError("Initial balance must be a number.")
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.account_balance = float(initial_balance) # This is the main account balance

    def deposit(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Deposit amount must be a number.")
        if amount <= 0:
            raise ValueError("Deposit amount must be a positive number.")
        
        self.account_balance += amount
        return self.account_balance # Return the new balance (optional for task, but useful)

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Withdrawal amount must be a number.")
        if amount <= 0:
            raise ValueError("Withdrawal amount cannot be zero or less.")
        
        if amount > self.account_balance:
            # Return False for insufficient funds, as required by main-0.py
            return False
        else:
            self.account_balance -= amount
            return True # Return True for successful withdrawal, as required by main-0.py

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.0f}") # Use .0f for integer amount as in example $50

 
    def __str__(self):
        return f"Account details: Current Balance: GHS {self.account_balance:.2f}"

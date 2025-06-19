# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0.0):
        if not isinstance(initial_balance, (int, float)):
            raise TypeError("Initial balance must be a number.")
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.account_balance = float(initial_balance)

    def deposit(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Deposit amount must be a number.")
        if amount <= 0:
            raise ValueError("Deposit amount must be a positive number.")
        
        self.account_balance += amount
        return self.account_balance

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Withdrawal amount must be a number.")
        if amount <= 0:
            raise ValueError("Withdrawal amount cannot be zero or less.")
        
        if amount > self.account_balance:
            return False
        else:
            self.account_balance -= amount
            return True

    def display_balance(self):
        # Corrected line: Ensures two decimal places as per "Expected" output
        print(f"Current Balance: ${self.account_balance:.2f}")

    def __str__(self):
        return f"Account details: Current Balance: GHS {self.account_balance:.2f}"

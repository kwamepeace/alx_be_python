class BankAccount:
    def __init__(self, initial_balance=0.0): # Changed parameter name for clarity
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.account_balance = float(initial_balance)
        # Removed self.amount as it's redundant for the account's state

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be a positive number.")
        else:
            self.account_balance += amount # Use += for conciseness
            # Corrected print statement to match "Expected" output format
            print(f"Deposited: ${amount:.1f}")
        return self.account_balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount cannot be zero, or less.")
        elif amount > self.account_balance: # Using elif for better logic flow
            raise ValueError(f"Insufficient funds for withdrawal. Current balance: GHS {self.account_balance:.2f}")
        else:
            self.account_balance -= amount # Use -= for conciseness
            print(f"Successfully withdrew GHS {amount:.2f}.")
        return self.account_balance

    def display_balance(self):
        # This is the corrected line to include "Current Balance:"
        return f"Current Balance: GHS {self.account_balance:.2f}"

    # It's also good practice to have a correct __str__ for general object representation
    def __str__(self):
        return f"Account details: Current Balance: GHS {self.account_balance:.2f}"

# Example Usage with corrected instantiation (assuming sufficient input will be provided)
try:
    print("Welcome to the Bank Account Management System!")

    initial_bal = float(input("Enter your initial account balance: "))
    my_account = BankAccount(initial_bal) # Pass only the initial balance

    deposit_amt = float(input("Enter amount to deposit: "))
    my_account.deposit(deposit_amt)
   

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

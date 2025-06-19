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
            print(f"Successfully deposited GHS {amount:.2f}.")
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

# Example Usage with corrected instantiation
try:
    print("Welcome to the Bank Account Management System!")

    initial_bal = float(input("Enter your initial account balance: "))
    my_account = BankAccount(initial_bal) # Pass only the initial balance

    print(my_account.display_balance()) # Call the display_balance method

    deposit_amt = float(input("Enter amount to deposit: "))
    my_account.deposit(deposit_amt)
    print(my_account.display_balance()) # Check balance after deposit

    withdraw_amt = float(input("Enter amount to withdraw: "))
    my_account.withdraw(withdraw_amt)
    print(my_account.display_balance()) # Check balance after withdrawal

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
        

            




# try:
#     print ("Welcome to the Bank Account Management System!")
#     print("What do you want to do? (deposit/withdraw/balance)")

#     actions = input() ["deposit", "withdraw"]
#     if actions == "deposit":
#         print("You can deposit money into your account.")
#         amount = float(input("Enter the amount to deposit: "))
#     elif actions == "withdraw":
#         amount = float(input("Enter the amount to withdraw: "))
#     account_balance = float(input("Enter your initial account balance: "))
#     my_account = BankAccount(amount, account_balance)

#     print(my_account)

# except Exception as e:
#     print(f"An error occurred: {e}")

















# import sys

# class BankAccount:
#     # 1. __init__: Only take the initial balance. 'amount' is for transactions, not account properties.
#     def __init__(self, initial_balance=0.0):
#         # Input validation for initial balance
#         if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
#             raise ValueError("Initial balance must be a non-negative number.")
#         self.account_balance = float(initial_balance) # This is the single source of truth for the balance

#     def deposit(self, amount):
#         # Input validation for deposit amount
#         if not isinstance(amount, (int, float)) or amount <= 0:
#             raise ValueError("Deposit amount must be a positive number.")
#         self.account_balance += amount
#         print(f"Successfully deposited GHS {amount:.2f}.")
#         return self.account_balance # Return the new balance (useful for chaining/display)

#     def withdraw(self, amount):
#         # Input validation for withdrawal amount
#         if not isinstance(amount, (int, float)) or amount <= 0:
#             raise ValueError("Withdrawal amount cannot be zero or less.")
        
#         if amount > self.account_balance:
#             raise ValueError(f"Insufficient funds for withdrawal. Current balance: GHS {self.account_balance:.2f}")
        
#         self.account_balance -= amount
#         print(f"Successfully withdrew GHS {amount:.2f}.")
#         return self.account_balance # Return the new balance (useful for chaining/display)

#     def __str__(self):
#         # __str__ should represent the current state of the object.
#         # 'Amount' is not a persistent state of the account.
#         return f"Current Account Balance: GHS {self.account_balance:.2f}"

# # --- Main Program Logic ---
# try:
#     print("Welcome to the Bank Account Management System!")

#     # 1. Get the initial balance for the account (Ghana context: GHS)
#     # This variable is local to the try block and used only once to create the object.
#     initial_balance_input = float(input("Enter your initial account balance (GHS): "))

#     # 2. Create the BankAccount object. This object now manages its own balance.
#     my_account = BankAccount(initial_balance_input)
    
#     # Print the initial state of the account using its __str__ method
#     print(my_account)

#     # 3. Perform a deposit operation
#     deposit_amount = float(input("Enter the amount to deposit (GHS): "))
#     my_account.deposit(deposit_amount) # This updates the balance INSIDE my_account
    
#     # Print the account's state again to see the updated balance
#     print(my_account)

#     # 4. Perform a withdrawal operation
#     withdraw_amount = float(input("Enter the amount to withdraw (GHS): "))
#     my_account.withdraw(withdraw_amount) # This updates the balance INSIDE my_account
    
#     # Print the final state of the account
#     print(my_account)

# except ValueError as ve:
#     print(f"Input Error: {ve}")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")

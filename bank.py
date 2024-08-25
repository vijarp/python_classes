"""Question:
Create a class BankAccount that represents a simple bank account. The class should have the following features:

Attributes:

account_holder: The name of the account holder.
balance: The current balance of the account.
Methods:

deposit(amount): Increases the balance by the specified amount.
withdraw(amount): Decreases the balance by the specified amount, but only if sufficient funds are available. If not, print an error message.
check_balance(): Returns the current balance.
transfer(amount, target_account): Transfers a specified amount to another BankAccount object, only if sufficient funds are available.
Edge Cases:

Ensure that no negative amounts can be deposited or withdrawn.
Handle the case where the withdrawal amount is greater than the balance.
"""

class BankAccount:
    def __init__(self, accountholder, initial_balance=0):
        self.accountholder = accountholder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def transfer(self, amount, target_account):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            target_account.deposit(amount)
            print(f"Transferred {amount} to {target_account.accountholder}")
        else:
            print("Invalid transfer amount or insufficient funds.")

    def check_balance(self):
        return self.balance

# Example Usage
account1 = BankAccount("Alice", 500)
account2 = BankAccount("Bob", 300)

# Deposit money
account1.deposit(200)
print(account1.check_balance())  # Output: 700

# Withdraw money
account1.withdraw(100)
print(account1.check_balance())  # Output: 600

# Transfer money
account1.transfer(200, account2)
print(account1.check_balance())  # Output: 400
print(account2.check_balance())  # Output: 500

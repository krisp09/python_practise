class InsufficientFundsError(Exception):
    """Custom exception for insufficient funds in the bank account."""
    pass
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds for this withdrawal.")
        self.balance -= amount
        return self.balance

    def get_balance(self):
        print(f"Current balance for account {self.account_number}: ${self.balance:.2f}")
        return self.balance
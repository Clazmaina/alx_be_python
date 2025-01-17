
class BankAccount:
    def _init_(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative.")
        self.account_balance += amount

    def withdraw(self, amount):
        if amount > self.account_balance:
            return False
        self.account_balance -= amount
        return True

    def display_balance(self):
        print(f"Current balance: ${self.account_balance:.2f}")
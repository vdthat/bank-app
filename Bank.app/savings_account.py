from bank_account import BankAccount

class SavingsAccount(BankAccount):

    def __init__(self, account_number, account_owner, balance=0):
        super().__init__(account_number, account_owner, balance)
        self.__interest_rate = 0.005

    def deposit(self, amount):
        interest = amount * self.__interest_rate
        super().deposit(amount + interest)
        print(f"Interest of {interest} added. New balance: {self.get_balance()}")

    def withdraw(self, amount):
        if amount <= 700000 and amount <= self.get_balance():
            super().withdraw(amount)
        elif amount > 700000:
            print("Withdrawal limit exceeded")
        else:
            print("Insufficient balance")
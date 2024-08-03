from account import Account
class ChildrensAccount(Account):
    def __init__(self, account_number, balance = 0):
        Account.__init__(self, account_number, balance)
        self.interest_rate = 0.007
        self.withdrawal_limit = 0

    def deposit(self, amount):
        Account.deposit(self, amount)
        self.balance += amount * self.interest_rate

    def withdraw(self, amount):
        print("withdrawal is not allowed for the childrens account")

children= ChildrensAccount
children.withdraw(10000)
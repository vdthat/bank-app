from bank_account import BankAccount
class CurrentAccount(BankAccount):
    def __init__(self):
        BankAccount.__init__(self, account_number=10012354, account_owner= "Hadiza Yusuf", balance= int(10000))


currentAccount = CurrentAccount()
currentAccount.deposit(15000)
currentAccount.withdraw(6000)        



        
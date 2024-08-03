print("_Bingham Bank App_")
name = input("Enter your name here: ").upper()
print("_Welcome" " " + name + "_")


class BankAccount:
    def _init_(self, account_number, account_owner, balance=10000):
        self.__account_number = account_number
        self.__account_owner = account_owner
        self.__balance = balance

    def get_account_number(self):
        return self.__account_number

    def get_account_owner(self):
        return self.__account_owner

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposit of {amount} successful. New balance: {self.__balance}")

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print(f"Withdrawal of {amount} successful. New balance: {self.__balance}")
        else:
            print("Insufficient balance")
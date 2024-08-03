class BankAccount:
    def __init__(self, name):
        self._name = name
        self._balance = 0

    @property
    def name(self):
        return self._name

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount
        print(f"Deposit of ${amount} successful. New balance: ${self._balance}")

    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient funds!")
        else:
            self._balance -= amount
            print(f"Withdrawal of ${amount} successful. New balance: ${self._balance}")


class StudentAccount(BankAccount):
    def __init__(self, name):
        super().__init__(name)
        self._withdraw_limit = 2000
        self._deposit_limit = 50000

    def deposit(self, amount):
        if amount > self._deposit_limit:
            print("Deposit amount exceeds limit!")
        else:
            super().deposit(amount)

    def withdraw(self, amount):
        if amount > self._withdraw_limit:
            print("Withdrawal amount exceeds limit!")
        else:
            super().withdraw(amount)


def main():
    name = input("Enter your name: ")
    student_account = StudentAccount(name)

    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter deposit amount: "))
            student_account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter withdrawal amount: "))
            student_account.withdraw(amount)
        elif choice == '3':
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
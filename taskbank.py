#the task on bank
class BankAccount:
    def __init__(self, account_number, balance, owner_name, date_opened):
        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name
        self.date_opened = date_opened

    def display_info(self):
        print(
            f"Account number: {self.account_number}\nBalance: {self.balance} KES\nName: {self.owner_name}\ndate opened: {self.date_opened}"
        )

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        print(f"{deposit_amount} KES deposited successfully New balance: {self.balance} KES")

    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.balance:
            print(
                f"Insufficient funds to carry out operation: you balance is:{self.balance} KES"
            )
        else:
            self.balance -= withdraw_amount
            print(
                f"{withdraw_amount} KES withdrawn successfully. New bank balance: {self.balance} KES"
            )


from datetime import date

account1 = BankAccount(128345336, 80000, "kennedy kim", date.today())

account1.display_info()
account1.deposit(1500)
account1.withdraw(15500)


account2 = BankAccount(65478736388, 78080,"sammy kama", date.today())

account2.display_info()
account2.deposit(5500)
account2.withdraw(705)

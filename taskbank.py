class BankAccount:
    def __init__(self, account_number, balance, owner_name, date_opened):
        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name
        self.date_opened = date_opened

    def display_info(self):
        return self.account_number, self.balance

from datetime import date
account1 = BankAccount(128345336,455,"kennedy kim", date.today())
print(type(account1))
account1.display_info()
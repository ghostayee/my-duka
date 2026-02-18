class BankAccount:
    def __init__(self, account_number, balance, owner_name, date_opened):
        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name
        self.date_opened = date_opened

    def display_info(self):
        print(
            f"Account number: {self.account_number}\nBalance: {self.balance}\nYour Name: {self.owner_name}\ndate opened: {self.date_opened}"
        )


from datetime import date

account1 = BankAccount(128345336, 455, "kennedy kim", date.today())

account1.display_info()

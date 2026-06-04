from wallet import UserWallet
from transactions import TransactionHistory

class User:
    def __init__(self,first_name,last_name,email,phone_bill,uid,wallet_usdt_value):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.phone_bill=phone_bill
        self.uid=uid
        self.wallet=UserWallet(wallet_usdt_value)
        self.transaction_history=TransactionHistory()

    def show_user_data(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.phone_bill)
        print(self.uid)
        self.wallet.show_wallet()
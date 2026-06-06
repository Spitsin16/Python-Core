from wallet import UserWallet
from transactions import TransactionHistory
from generate import *
from inputs import *

class User:
    def __init__(self,first_name,last_name,uid,password,wallet_usdt_value):
        self.first_name=first_name
        self.last_name=last_name
        self.password=password
        self.uid=uid
        self.wallet=UserWallet(wallet_usdt_value)
        self.transaction_history=TransactionHistory()

    def show_user_data(self):
        print(self.first_name)
        print(self.last_name)
        print(self.uid)
        self.wallet.show_wallet()

def create_user():
    first_name=input('Add first name')
    last_name = input('Add last name')
    password=create_and_check_password()
    uid = generate_uid()
    wallet_usdt_value = check_input_wallet_balance('Add your USDT balance: ')
    user=User(first_name,last_name,uid,password,wallet_usdt_value)
    return user

def  show_all_users(users):
    i=0
    for user in users:
        i+=1
        print(f'{i}. {user.uid}, {user.last_name} ')

def current_user(users):
    while True:
        added_uid = input('Add your uid: ')

        for user in users:
            if user.uid == added_uid:
                print('User found. Add your password')
                added_pass = input('Add user password: ')

                if user.password == added_pass:
                    print('Login success')
                    return user
                else:
                    print('Login unsuccess. Wrong password')
                    break

        else:
            print('Dont have user with same uid')






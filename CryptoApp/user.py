from wallet import UserWallet
from transactions import TransactionHistory
from generate import *
from inputs import *
from marketApi import MarketApi

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

def login_user(users):
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

def transfer(users,pairs,active_user,transactions):
    recipient_uid_add=input('Add the user uid to which you want to send the crypto')
    recipient=None
    for user in users:
        if user.uid==recipient_uid_add:
            recipient=user
            break

    if recipient is None:
        print('Wrong uid')
        return

    if recipient.uid == active_user.uid:
        print('You cannot transfer crypto to yourself')
        return

    coin_you_want_to_transfer= str_input('Add coin you want to transfer',pairs)
    if coin_you_want_to_transfer == 'USDT':
        coin_value_you_want_to_transfer=active_user.wallet.check_usdt_value_to_buy('Add usdt value you want to sell')
        active_user.wallet.wallet['USDT'] -= coin_value_you_want_to_transfer
        if 'USDT' in recipient.wallet.wallet:
            recipient.wallet.wallet['USDT'] += coin_value_you_want_to_transfer
        else:
            recipient.wallet.wallet['USDT'] = coin_value_you_want_to_transfer
    else:
        coin_value_you_want_to_transfer=active_user.wallet.check_coin_value_to_sell('Add coin value you want to sell', coin_you_want_to_transfer)
        coin_name= coin_you_want_to_transfer.split('/')[0]
        if coin_name in active_user.wallet.wallet.keys():
            active_user.wallet.wallet[coin_name]-= coin_value_you_want_to_transfer
            if coin_name in recipient.wallet.wallet:
                recipient.wallet.wallet[coin_name]+= coin_value_you_want_to_transfer
            else:
                recipient.wallet.wallet[coin_name] = coin_value_you_want_to_transfer
        else:
            print('Unknown coin')
    if active_user.wallet.wallet[coin_name] <= 0:
        del active_user.wallet.wallet[coin_name]
    if active_user.wallet.wallet['USDT'] <= 0:
        del active_user.wallet.wallet['USDT']
    active_user.transaction_history.add_transaction_transfer('transfer out', coin_you_want_to_transfer, coin_value_you_want_to_transfer,recipient_uid_add)
    recipient.transaction_history.add_transaction_transfer('transfer in', coin_you_want_to_transfer,
                                                             coin_value_you_want_to_transfer, active_user.uid)







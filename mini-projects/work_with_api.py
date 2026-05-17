import requests
import time

URL = "https://api.rapira.net/open/market/rates"


def get_pairs_from_rapira(url):
    message=(requests.get(url)).json()
    data=message['data']
    coins={}
    for pair in data:
        coins[pair['symbol']]={'buy':pair['askPrice'],'sell':pair['bidPrice']}
    return coins

def show_pairs(pairs):
    active_coins = list(pairs.keys())

    print(*active_coins)

def create_wallet(wallet_usdt_value):
    wallet = {'USDT': wallet_usdt_value}
    return wallet

def show_wallet(wallet):
    print('Your wallet:')
    for coin,value in wallet.items():
       print (value, coin )

def buy_coin(wallet,coin_user_want_buy,usdt_value_to_buy,pairs):
    if usdt_value_to_buy==0:
        print('Error: amount must be greater than zero')
        return
    if usdt_value_to_buy>wallet['USDT']:
        print('Error: not enough USDT')
        return
    buy_course=float(pairs[coin_user_want_buy]['buy'])
    usdt_value=wallet['USDT']
    coin_value=usdt_value_to_buy/buy_course
    wallet['USDT']=usdt_value-usdt_value_to_buy
    wallet[coin_user_want_buy.split('/')[0]]=coin_value
    print(f'Congrats you buy {coin_value} {coin_user_want_buy.split('/')[0]} on {usdt_value_to_buy} USDT')

def show_menu():
    print('\nMenu:')
    print('1 - Show available coins')
    print('2 - Show wallet')
    print('3 - Buy coin')
    print('0 - Exit')

def int_input(message):
    while True:
        user_input=input(message)
        if user_input.isdigit():
            return int(user_input)
        else:
            print('Error: enter a number')
def str_input(message,pairs):
    while True:
        user_input=input(message)
        if  user_input in list(pairs.keys()):
            return str(user_input)
        else:
            print('Error: enter correct coin')

def main():
    print('Hello on our CryptoChanger!!!')
    pairs = get_pairs_from_rapira(URL)
    wallet_usdt_value = int_input('Add your USDT balance: ')
    wallet = create_wallet(wallet_usdt_value)


    while True:
        show_menu()
        choice=int_input('Choose action:')
        if choice==1:
            pairs = get_pairs_from_rapira(URL)
            show_pairs(pairs)
        elif choice==2:
            show_wallet(wallet)
        elif choice==3:
            pairs = get_pairs_from_rapira(URL)
            coin_user_want_buy = str_input('Choose coin you want to buy: ',pairs)
            usdt_value_to_buy = int_input('Write how much USDT you want to spend to buy this coin: ')
            buy_coin(wallet, coin_user_want_buy, usdt_value_to_buy, pairs)
        elif choice==0:
            print('See you later')
            break
        else:
            print('Unknown command')


main()














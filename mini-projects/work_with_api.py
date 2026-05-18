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
    buy_course=float(pairs[coin_user_want_buy]['buy'])
    usdt_value=wallet['USDT']
    coin_value=usdt_value_to_buy/buy_course
    wallet['USDT']=usdt_value-usdt_value_to_buy
    coin_name=coin_user_want_buy.split('/')[0]
    if coin_name in wallet:
        wallet[coin_name] = coin_value+wallet[coin_name]
    else:
        wallet[coin_name]=coin_value
    print(f'Congrats you buy {coin_value} {coin_name} on {usdt_value_to_buy} USDT')

def sell_coin(wallet,coin_user_want_to_sell,coin_value_want_to_sell,pairs):
    sell_course=float(pairs[coin_user_want_to_sell]['sell'])
    coin_name=coin_user_want_to_sell.split('/')[0]
    usdt_value=coin_value_want_to_sell*sell_course
    wallet['USDT']+=usdt_value
    wallet[coin_name]-=coin_value_want_to_sell

    print(f'Congrats you sell {coin_value_want_to_sell} {coin_name} on {usdt_value} USDT')



def show_menu():
    print('\nMenu:')
    print('1 - Show available coins')
    print('2 - Show wallet')
    print('3 - Buy coin')
    print('4 - Sell coin')
    print('0 - Exit')

def float_input(message):
    while True:
        user_input=input(message)
        try:
            return float(user_input)
        except ValueError:
            print('Error: enter a number')
def str_input(message,pairs):
    while True:
        user_input=input(message)
        if  user_input in list(pairs.keys()):
            return str(user_input)
        else:
            print('Error: enter correct coin')

def check_usdt_value_to_buy(message,wallet):
    while True:
        usdt_value_to_buy=float_input(message)
        if usdt_value_to_buy==0:
            print('Amount must be greater than zero')
        elif usdt_value_to_buy>wallet['USDT']:

            print('Not enough money')
        else:
            return usdt_value_to_buy
def check_coin_value_to_sell(message,wallet,coin_user_want_to_sell):
    while True:
        coin_value_want_to_sell=float_input(message)
        if coin_value_want_to_sell==0:
            print('Amount must be greater than zero')
        elif coin_value_want_to_sell>wallet[coin_user_want_to_sell.split('/')[0]]:
            print('Not enough money')
        else:
            return coin_value_want_to_sell


def check_input_wallet_balance(message):
    while True:
        wallet_usdt_value=float_input(message)
        if wallet_usdt_value==0:
            print('Amount must be greater than zero')
        elif wallet_usdt_value<0:
            print('Amount must be positive')
        else:
            return wallet_usdt_value
def check_coin_in_wallet(message,wallet,pairs):
    while True:
        coin_user_want_to_sell = str_input(message,pairs)
        if coin_user_want_to_sell.split('/')[0] not in wallet:
            print('You havent this coin')
        else:
            return coin_user_want_to_sell


def int_input(message):
    while True:
        user_input = input(message)

        try:
            return int(user_input)
        except ValueError:
            print('Error: enter a whole number')



def main():
    print('Hello on our CryptoChanger!!!')
    pairs = get_pairs_from_rapira(URL)
    wallet_usdt_value = check_input_wallet_balance('Add your USDT balance: ')
    wallet = create_wallet(wallet_usdt_value)
    show_wallet(wallet)


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
            usdt_value_to_buy=check_usdt_value_to_buy('Write how much USDT you want to spend to buy this coin: ',wallet)
            buy_coin(wallet, coin_user_want_buy, usdt_value_to_buy, pairs)
        elif choice==4:
            pairs = get_pairs_from_rapira(URL)
            coin_user_want_to_sell=check_coin_in_wallet('Add coin you want to sell',wallet,pairs)
            coin_value_want_to_sell = check_coin_value_to_sell('Add value of coin you want to sell',wallet,coin_user_want_to_sell)
            sell_coin(wallet,coin_user_want_to_sell,coin_value_want_to_sell,pairs)
        elif choice==0:
            print('See you later')
            break
        else:
            print('Unknown command')

if __name__ == "__main__":
    main()
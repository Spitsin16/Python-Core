import requests
import time

def get_pairs_from_rapira(url):
    message=(requests.get(url)).json()
    data=message['data']
    coins={}
    for pair in data:
        coins[pair['symbol']]={'buy':pair['askPrice'],'sell':pair['bidPrice']}
    return coins

def show_pairs(pairs):
    active_coins = list(pairs.keys())
    print('Available coins:')
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
      wallet[coin_user_want_buy.split('/')[0]]=coin_value
      print(f'Congrats you buy {coin_value} {coin_user_want_buy.split('/')[0]} on {usdt_value_to_buy} USDT')

def main():
    print('Hello on our CryptoChanger!!!')
    url = "https://api.rapira.net/open/market/rates"
    pairs = get_pairs_from_rapira(url)
    wallet_usdt_value = int(input('Add your USDT balance: '))
    wallet = create_wallet(wallet_usdt_value)
    show_wallet(wallet)
    show_pairs(pairs)
    coin_user_want_buy = str(input('Choose coin you want to buy: '))

    usdt_value_to_buy = int(input('Write how much USDT you want to spend to buy this coin: '))
    buy_coin(wallet,coin_user_want_buy,usdt_value_to_buy,pairs)
    show_wallet(wallet)

main()













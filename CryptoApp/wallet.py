from generate import *
from inputs import *

class UserWallet:
    def __init__(self, wallet_usdt_value):
        self.wallet = {'USDT': wallet_usdt_value}
        self.wallet_address = generate_address()

    def show_wallet(self):
        print(f'Your wallet ({self.wallet_address}) :')
        for coin, value in self.wallet.items():
            print(value, coin)

    def buy_coin(self, coin_user_want_buy, usdt_value_to_buy, pairs, transactions):
        buy_course = float(pairs[coin_user_want_buy]['buy'])
        usdt_value = self.wallet['USDT']
        coin_value = usdt_value_to_buy / buy_course
        self.wallet['USDT'] = usdt_value - usdt_value_to_buy
        coin_name = coin_user_want_buy.split('/')[0]
        if coin_name in self.wallet:
            self.wallet[coin_name] = coin_value + self.wallet[coin_name]
        else:
            self.wallet[coin_name] = coin_value
        coin_amount = coin_value
        course = buy_course
        print(f'Congrats you buy {coin_value} {coin_name} on {usdt_value_to_buy} USDT')
        transactions.add_transaction('buy', coin_name, coin_amount, usdt_value_to_buy, course)

    def sell_coin(self, coin_user_want_to_sell, coin_value_want_to_sell, pairs, transactions):
        sell_course = float(pairs[coin_user_want_to_sell]['sell'])
        coin_name = coin_user_want_to_sell.split('/')[0]
        usdt_value = coin_value_want_to_sell * sell_course
        course = sell_course
        coin_amount = coin_value_want_to_sell
        self.wallet['USDT'] += usdt_value
        self.wallet[coin_name] -= coin_value_want_to_sell
        transactions.add_transaction('sell', coin_name, coin_amount, usdt_value, course)
        if self.wallet[coin_name] <= 0:
            del self.wallet[coin_name]
        print(f'Congrats you sell {coin_value_want_to_sell} {coin_name} on {usdt_value} USDT')


    def sell_all_value_of_coin(self, coin_user_want_to_sell, pairs, transactions):
        sell_course = float(pairs[coin_user_want_to_sell]['sell'])
        coin_name = coin_user_want_to_sell.split('/')[0]
        usdt_value = self.wallet[coin_name] * sell_course
        course = sell_course
        coin_amount = self.wallet[coin_name]
        self.wallet['USDT'] += usdt_value
        self.wallet[coin_name] -= self.wallet[coin_name]
        transactions.add_transaction('sell', coin_name, coin_amount, usdt_value, course)
        del self.wallet[coin_name]
        print(f'Congrats you sell {coin_amount} {coin_name} on {usdt_value} USDT')

    def check_coin_in_wallet(self, message, pairs):
        while True:
            coin_user_want_to_sell = str_input(message, pairs)
            if coin_user_want_to_sell.split('/')[0] not in self.wallet:
                print('You havent this coin')
            else:
                return coin_user_want_to_sell

    def check_usdt_value_to_buy(self, message):
        while True:
            usdt_value_to_buy = float_input(message)
            if usdt_value_to_buy == 0 or usdt_value_to_buy < 0:
                print('Amount must be greater than zero')
            elif usdt_value_to_buy > self.wallet['USDT']:
                print('Not enough money')
            else:
                return usdt_value_to_buy

    def check_coin_value_to_sell(self, message, coin_user_want_to_sell):
        while True:
            coin_value_want_to_sell = float_input(message)
            if coin_value_want_to_sell == 0 or coin_value_want_to_sell < 0:
                print('Amount must be greater than zero')
            elif coin_value_want_to_sell > self.wallet[coin_user_want_to_sell.split('/')[0]]:
                print('Not enough money')
            else:
                return coin_value_want_to_sell




import requests
import random
import string

class MarketApi:
    def __init__(self):
        self.url= "https://api.rapira.net/open/market/rates"
        self.pairs={}
    def get_market_api_pairs_from_rapira(self):
        message = (requests.get(self.url)).json()
        data = message['data']
        for pair in data:
            self.pairs[pair['symbol']] = {'buy': pair['askPrice'], 'sell': pair['bidPrice']}
        return self.pairs

    def show_pairs(self):
        active_coins = list(self.pairs.keys())
        print(*active_coins)

    def show_cources(self,operation):
        for item, value in self.pairs.items():
            print(item, value[operation])

class UserWallet:
    def __init__(self,wallet_usdt_value):
        self.wallet={'USDT':wallet_usdt_value}
        self.wallet_address=generate_address()

    def show_wallet(self):
        print(f'Your wallet ({self.wallet_address}) :')
        for coin,value in self.wallet.items():
            print(value,coin)

    def buy_coin(self,coin_user_want_buy, usdt_value_to_buy, pairs, transactions):
        buy_course = float(pairs[coin_user_want_buy]['buy'])
        usdt_value = self.wallet['USDT']
        coin_value = usdt_value_to_buy / buy_course
        self.wallet['USDT'] = usdt_value - usdt_value_to_buy
        coin_name = coin_user_want_buy.split('/')[0]
        if coin_name in self.wallet :
            self.wallet[coin_name] = coin_value + self.wallet[coin_name]
        else:
            self.wallet[coin_name] = coin_value
        coin_amount = coin_value
        course = buy_course
        print(f'Congrats you buy {coin_value} {coin_name} on {usdt_value_to_buy} USDT')
        transactions.add_transaction( 'buy', coin_name, coin_amount, usdt_value_to_buy, course)

    def sell_coin(self, coin_user_want_to_sell, coin_value_want_to_sell, pairs, transactions):
        sell_course = float(pairs[coin_user_want_to_sell]['sell'])
        coin_name = coin_user_want_to_sell.split('/')[0]
        usdt_value = coin_value_want_to_sell * sell_course
        course = sell_course
        coin_amount = coin_value_want_to_sell
        self.wallet['USDT'] += usdt_value
        self.wallet[coin_name] -= coin_value_want_to_sell
        transactions.add_transaction( 'sell', coin_name, coin_amount, usdt_value, course)
        if self.wallet[coin_name]<=0:
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


    def check_coin_in_wallet(self,message, pairs):
        while True:
            coin_user_want_to_sell = str_input(message, pairs)
            if coin_user_want_to_sell.split('/')[0] not in self.wallet:
                print('You havent this coin')
            else:
                return coin_user_want_to_sell

    def check_usdt_value_to_buy(self,message):
        while True:
            usdt_value_to_buy = float_input(message)
            if usdt_value_to_buy == 0 or usdt_value_to_buy <0:
                print('Amount must be greater than zero')
            elif usdt_value_to_buy > self.wallet['USDT']:
                print('Not enough money')
            else:
                return usdt_value_to_buy

    def check_coin_value_to_sell(self,message, coin_user_want_to_sell):
        while True:
            coin_value_want_to_sell = float_input(message)
            if coin_value_want_to_sell == 0 or coin_value_want_to_sell<0:
                print('Amount must be greater than zero')
            elif coin_value_want_to_sell > self.wallet[coin_user_want_to_sell.split('/')[0]]:
                print('Not enough money')
            else:
                return coin_value_want_to_sell

    def check_input_wallet_balance(self,message):
        while True:
            wallet_usdt_value = float_input(message)
            if wallet_usdt_value == 0:
                print('Amount must be greater than zero')
            elif wallet_usdt_value < 0:
                print('Amount must be positive')
            else:
                return wallet_usdt_value


class TransactionHistory:
    def __init__(self):
        self.transactions=[]


    def show_transactions(self):
        if not self.transactions:
            print('Transaction history is empty')
        else:
            print('Your transactions')
            for transaction in self.transactions:
                print(f'Operation: {transaction['type']}, coin: {transaction['coin']}, coin amount: {transaction['coin_amount']},'
                      f'usdt amount: {transaction['usdt_amount']}, course: {transaction['course']}')

    def add_transaction(self,operation_type,coin_name,coin_amount,usdt_amount,course):
        transaction = {
            'type': operation_type,
            'coin': coin_name,
            'coin_amount': coin_amount,
            'usdt_amount': usdt_amount,
            'course': course
        }
        self.transactions.append(transaction)

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



def generate_address():
    alph=string.ascii_letters+string.digits
    address='T'+ ''.join(random.choices(alph,k=33))
    return address

def generate_uid():
    alph=string.digits
    uid=''.join(random.choices(alph,k=6))
    return uid


def float_input(message):
    while True:
        user_input=input(message)
        try:
            return float(user_input)
        except ValueError:
            print('Error: enter a number')

def str_input(message,pairs):
    while True:
        user_input=input(message).upper()
        if  user_input in list(pairs.keys()):
            return str(user_input)
        else:
            print('Error: enter correct coin')

def int_input(message):
    while True:
        user_input = input(message)

        try:
            return int(user_input)
        except ValueError:
            print('Error: enter a whole number')


def check_input_wallet_balance(message):
    while True:
        wallet_usdt_value=float_input(message)
        if wallet_usdt_value==0:
            print('Amount must be greater than zero')
        elif wallet_usdt_value<0:
            print('Amount must be positive')
        else:
            return wallet_usdt_value




def show_menu():
    print('\nMenu:')
    print('1 - Show available coins')
    print('2 - Show wallet')
    print('3 - Buy coin')
    print('4 - Sell coin')
    print('5 - Check transactions')
    print('6 - Show cources')
    print('7 - My account')
    print('0 - Exit')




def main():
    market = MarketApi()
    print('Hello on our CryptoChanger!!!')
    first_name=input('Add your first_name: ')
    last_name = input('Add your last_name: ')
    email = input('Add your email: ')
    phone_bill = input('Add your phone_bill: ')
    uid = generate_uid()
    wallet_usdt_value = check_input_wallet_balance('Add your USDT balance: ')
    user1 = User(first_name, last_name, email, phone_bill, uid,wallet_usdt_value)

    while True:
        show_menu()
        choice=int_input('Choose action:')
        if choice==1:
            pairs = market.get_market_api_pairs_from_rapira()
            market.show_pairs()
        elif choice==2:
            user1.wallet.show_wallet()
        elif choice==3:
            pairs = market.get_market_api_pairs_from_rapira()
            coin_user_want_buy = str_input('Choose coin you want to buy: ',pairs)
            usdt_value_to_buy=user1.wallet.check_usdt_value_to_buy('Write how much USDT you want to spend to buy this coin: ')
            user1.wallet.buy_coin( coin_user_want_buy, usdt_value_to_buy, pairs,user1.transaction_history)
        elif choice==4:
            pairs = market.get_market_api_pairs_from_rapira()
            coin_user_want_to_sell=user1.wallet.check_coin_in_wallet('Add coin you want to sell',pairs)
            print('Do you want sell all value of coin?')
            print('1 - yes')
            print('2 - no')
            choice41=int(input())
            if choice41 == 1:
                user1.wallet.sell_all_value_of_coin(coin_user_want_to_sell,pairs,user1.transaction_history)
            elif choice41==2:
                coin_value_want_to_sell = user1.wallet.check_coin_value_to_sell('Add value of coin you want to sell',coin_user_want_to_sell)
                user1.wallet.sell_coin(coin_user_want_to_sell,coin_value_want_to_sell,pairs,user1.transaction_history)
        elif choice==5:
            user1.transaction_history.show_transactions()
        elif choice==6:
            pairs = market.get_market_api_pairs_from_rapira()
            print('1 - buy')
            print('2 - sell')
            choice_two=int_input('Choose action:')
            if choice_two==1:
                market.show_cources('buy')
            elif choice_two==2:
                market.show_cources('sell')
            else:
                print('Unknown command')
        elif choice==7:
            user1.show_user_data()
        elif choice==0:
            print('See you later')
            break
        else:
            print('Unknown command')



if __name__ == "__main__":
    main()


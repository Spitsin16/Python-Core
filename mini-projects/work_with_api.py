import requests

URL = "https://api.rapira.net/open/market/rates"


def get_pairs_from_rapira(url):
    message=(requests.get(url)).json()
    data=message['data']
    coins={}
    for pair in data:
        coins[pair['symbol']]={'buy':pair['askPrice'],'sell':pair['bidPrice']}
    return coins

class UserWallet:
    def __init__(self,wallet_usdt_value):
        self.wallet={'USDT':wallet_usdt_value}

    def show_wallet(self):
        print('Your wallet:')
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

        print(f'Congrats you sell {coin_value_want_to_sell} {coin_name} on {usdt_value} USDT')

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




def show_pairs(pairs):
    active_coins = list(pairs.keys())
    print(*active_coins)

def show_cources(pairs, operation):
    for item, value in pairs.items():
        print(item, value[operation])

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
    print('0 - Exit')




def main():
    print('Hello on our CryptoChanger!!!')
    pairs = get_pairs_from_rapira(URL)
    wallet_usdt_value = check_input_wallet_balance('Add your USDT balance: ')
    wallet = UserWallet(wallet_usdt_value)
    wallet.show_wallet()
    transactions=TransactionHistory()

    while True:
        show_menu()
        choice=int_input('Choose action:')
        if choice==1:
            pairs = get_pairs_from_rapira(URL)
            show_pairs(pairs)
        elif choice==2:
            wallet.show_wallet()
        elif choice==3:
            pairs = get_pairs_from_rapira(URL)
            coin_user_want_buy = str_input('Choose coin you want to buy: ',pairs)
            usdt_value_to_buy=wallet.check_usdt_value_to_buy('Write how much USDT you want to spend to buy this coin: ')
            wallet.buy_coin( coin_user_want_buy, usdt_value_to_buy, pairs,transactions)
        elif choice==4:
            pairs = get_pairs_from_rapira(URL)
            coin_user_want_to_sell=wallet.check_coin_in_wallet('Add coin you want to sell',pairs)
            coin_value_want_to_sell = wallet.check_coin_value_to_sell('Add value of coin you want to sell',coin_user_want_to_sell)
            wallet.sell_coin(coin_user_want_to_sell,coin_value_want_to_sell,pairs,transactions)
        elif choice==5:
            transactions.show_transactions()
        elif choice==6:
            pairs = get_pairs_from_rapira(URL)
            print('1 - buy')
            print('2 - sell')
            choice_two=int_input('Choose action:')
            if choice_two==1:
                show_cources(pairs,'buy')
            elif choice_two==2:
                show_cources(pairs, 'sell')
            else:
                print('Unknown command')

        elif choice==0:
            print('See you later')
            break
        else:
            print('Unknown command')



if __name__ == "__main__":
    main()


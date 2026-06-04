from menu import show_menu
from marketApi import MarketApi
from generate import  generate_uid
from user import User
from inputs import check_input_wallet_balance,int_input,str_input

def main():
    market = MarketApi()
    print('Hello on our CryptoChanger!!!')
    first_name = input('Add your first_name: ')
    last_name = input('Add your last_name: ')
    email = input('Add your email: ')
    phone_bill = input('Add your phone_bill: ')
    uid = generate_uid()
    wallet_usdt_value = check_input_wallet_balance('Add your USDT balance: ')
    user1 = User(first_name, last_name, email, phone_bill, uid, wallet_usdt_value)

    while True:
        show_menu()
        choice = int_input('Choose action:')
        if choice == 1:
            pairs = market.get_market_api_pairs_from_rapira()
            market.show_pairs()
        elif choice == 2:
            user1.wallet.show_wallet()
        elif choice == 3:
            pairs = market.get_market_api_pairs_from_rapira()
            coin_user_want_buy = str_input('Choose coin you want to buy: ', pairs)
            usdt_value_to_buy = user1.wallet.check_usdt_value_to_buy(
                'Write how much USDT you want to spend to buy this coin: ')
            user1.wallet.buy_coin(coin_user_want_buy, usdt_value_to_buy, pairs, user1.transaction_history)
        elif choice == 4:
            pairs = market.get_market_api_pairs_from_rapira()
            coin_user_want_to_sell = user1.wallet.check_coin_in_wallet('Add coin you want to sell', pairs)
            print('Do you want sell all value of coin?')
            print('1 - yes')
            print('2 - no')
            choice41 = int(input())
            if choice41 == 1:
                user1.wallet.sell_all_value_of_coin(coin_user_want_to_sell, pairs, user1.transaction_history)
            elif choice41 == 2:
                coin_value_want_to_sell = user1.wallet.check_coin_value_to_sell('Add value of coin you want to sell',
                                                                                coin_user_want_to_sell)
                user1.wallet.sell_coin(coin_user_want_to_sell, coin_value_want_to_sell, pairs,
                                       user1.transaction_history)
        elif choice == 5:
            user1.transaction_history.show_transactions()
        elif choice == 6:
            pairs = market.get_market_api_pairs_from_rapira()
            print('1 - buy')
            print('2 - sell')
            choice_two = int_input('Choose action:')
            if choice_two == 1:
                market.show_cources('buy')
            elif choice_two == 2:
                market.show_cources('sell')
            else:
                print('Unknown command')
        elif choice == 7:
            user1.show_user_data()
        elif choice == 0:
            print('See you later')
            break
        else:
            print('Unknown command')


if __name__ == "__main__":
    main()


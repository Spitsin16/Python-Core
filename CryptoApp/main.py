from menu import *
from marketApi import MarketApi
from generate import  generate_uid
from user import *
from inputs import check_input_wallet_balance,int_input,str_input


def main():
    users = []
    market = MarketApi()
    print('Hello on our CryptoChanger. You havent users, lets go create!')
    active_user= None
    while True:
        if active_user is None:
            show_menu_1()
            choice_1menu = int(input('Choose action:'))
            if choice_1menu == 1:
                active_user = create_user()
                print(f'Welcome, {active_user.first_name}, your uid: {active_user.uid}')
                users.append(active_user)
            elif choice_1menu == 2:
                if len(users)>0:
                    active_user = login_user(users)
                elif len(users)==0:
                    print ('There is no registered users')

            else:
                print('Unknown command')
        else:

            show_menu()
            choice = int_input('Choose action:')

            if choice == 1:
                pairs = market.get_market_api_pairs_from_rapira()
                market.show_pairs()
            elif choice == 2:
                active_user.wallet.show_wallet()
            elif choice == 3:
                pairs = market.get_market_api_pairs_from_rapira()
                coin_user_want_buy = str_input('Choose coin you want to buy: ', pairs)
                usdt_value_to_buy = active_user.wallet.check_usdt_value_to_buy(
                    'Write how much USDT you want to spend to buy this coin: ')
                active_user.wallet.buy_coin(coin_user_want_buy, usdt_value_to_buy, pairs, active_user.transaction_history)
            elif choice == 4:
                pairs = market.get_market_api_pairs_from_rapira()
                coin_user_want_to_sell =active_user.wallet.check_coin_in_wallet('Add coin you want to sell', pairs)
                print('Do you want sell all value of coin?')
                print('1 - yes')
                print('2 - no')
                choice41 = int(input())
                if choice41 == 1:
                    active_user.wallet.sell_all_value_of_coin(coin_user_want_to_sell, pairs, active_user.transaction_history)
                elif choice41 == 2:
                    coin_value_want_to_sell = active_user.wallet.check_coin_value_to_sell('Add value of coin you want to sell',
                                                                                    coin_user_want_to_sell)
                    active_user.wallet.sell_coin(coin_user_want_to_sell, coin_value_want_to_sell, pairs,
                                           active_user.transaction_history)
            elif choice == 5:
                active_user.transaction_history.show_transactions()
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
                active_user.show_user_data()
            elif choice == 8:
                active_user = None
            elif choice == 9:
                pairs = market.get_market_api_pairs_from_rapira()
                transfer(users,pairs,active_user,active_user.transaction_history)
            elif choice == 0:
                print('See you later')
                break
            else:
                print('Unknown command')


if __name__ == "__main__":
    main()


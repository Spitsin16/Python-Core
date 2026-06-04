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
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
def create_and_check_password():
    while True:
        password=input('Add password:')
        ka=0
        ki=0
        for i in password:
            if i.isalpha():
                ka+=1
            elif i.isdigit():
                ki+=1

        if len(password) > 6 and ka>=1 and ki >=1 :
            return password

        elif ka<1:
            print ('Password must contain at least one letter')
        elif ki<1:
            print('Password must contain at least one digit')

        else:
            print('Password is very short')




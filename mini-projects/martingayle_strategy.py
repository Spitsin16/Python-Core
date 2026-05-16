import random

balance = int(input('Add your balance: '))
const_bet = int(input('Add bet: '))
player_amount= int(input('Add player amount: '))
want_to_win = int(input('Add amount you want win: '))


def computer_choice():
    return random.randint(0, 1)

def human_choice():
    return random.randint(0, 1)

def game(balance,const_bet,want_to_win,player_amount):

    total_balance = []
    k_win=0
    k_lost=0
    for player in range(player_amount):
        current_balance=balance

        win_counter = 0
        lost_counter = 0
        bet = const_bet
        balanses = []

        while current_balance > 0 and current_balance < want_to_win:
            if bet > current_balance:
                bet=current_balance
            computer = computer_choice()
            human = human_choice()
            if computer == human:
                current_balance += bet
                bet = const_bet
                win_counter += 1
                balanses.append(current_balance)
            else:
                current_balance -= bet
                bet = bet * 2
                lost_counter += 1
                balanses.append(current_balance)
        if current_balance >= want_to_win:
            balanses.append(current_balance)
            k_win += 1
        else:
            k_lost+=1
        (total_balance).append(max(balanses))
        pr=(k_win/player_amount)*100

    return (k_win,k_lost,pr)

stats=game(balance,const_bet,want_to_win,player_amount)
wn,ls,pers=stats
print(f'{wn} people win')
print(f'{ls} people lost')
print(f'Win percent {pers}')







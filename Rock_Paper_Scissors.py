import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        print('You and the computer have both chosen {}.'.format(user))
        return 'It\'s a tie'

    # r > s, s > p, p > r
    if is_win(user, computer):
        print('You chose {} and the computer chose {}.'.format(user, computer))
        return 'You won!'

    print('You chose {} and the computer chose {}.'.format(user, computer))
    return 'You lost!'
       


def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())

import random

def guess_game(diff):
    times = 0
    win = 0
    lvl = [None, 10, 30, 55, 75, 100]
    secret_num = random.randint(1, lvl[diff])
    while times < 3:
        user_num = int(input(f'Choose number form 1 to {lvl[diff]}: '))
        if user_num == secret_num:
            print('Bingo!!!')
            win = 1
            break
        elif user_num < secret_num:
            print('Secret number is higher')
        elif user_num > secret_num:
            print('Secret number is lower')
        times += 1

    return secret_num, win
    
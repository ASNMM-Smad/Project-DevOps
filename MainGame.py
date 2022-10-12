from Live import welcome, load_game
from GuessGame import guess_game
from CurrencyRoulellte import get_currency_value
from MemoryGame import memory_game
from MainScores import score_server
from score import add_score
import time

def get_ready():
    for i in range(0,5):
        print(f"The game will begin in {5-i}")
        time.sleep(i)

def play(game, diff):
    get_ready()
    if game == 1:
        play = memory_game(diff)
        print (play)
        if play == True:
            print('Winner')
            return 1
        else:
            print('Losser')
            return -1

    if game == 2:
        play = guess_game(diff)
        res = play[1]
        if res == 1:
            print('Winner')
            return res
        else:
            print('Losser')
            return -1

    if game == 3:
        play = get_currency_value(diff)
        if play == True:
            print('Winner')
            return 1
        else:
            print('Losser')
            return -1

    print('Bye Bye')
    return 0
    
### Welcome
print(welcome())

### Load Game
load = 0
while True:
    if load == 0:
        loading= load_game()
        load = -1
    elif loading == -1:
        print("\nPlease, pay attentions to the instructions", end='')
        loading = load_game()
    else:
        print(loading[0])
        game = loading[1]
        diff = loading[2]
        winORlose = play(game, diff)
        if winORlose == 1:
            total_new_score = add_score(diff)
            show_new_score = score_server(total_new_score, status_code=0)
            #print(total_new_score)
        else:
            break
        break

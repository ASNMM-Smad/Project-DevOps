from Live import welcome, load_game
from GuessGame import guess_game
from CurrencyRoulellte import get_currency_value
from MemoryGame import memory_game
import time

def get_ready():
    for i in range(0,5):
        print(f"The game will begin in {5-i}")
        time.sleep(i)

def play(game, lvl):
    get_ready()
    if game == 1:
        play = memory_game(lvl)
        print (play)
        if play == True:
            print('Winner')
            return 1
        else:
            print('Losser')
            return -1

    if game == 2:
        play = guess_game(lvl)
        res = play[1]
        if res == 1:
            print('Winner')
            return res
        else:
            print('Losser')
            return -1

    if game == 3:
        play = get_currency_value(lvl)
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
        lvl = loading[2]
        play(game, lvl)
        break

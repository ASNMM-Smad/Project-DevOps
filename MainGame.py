from Live import welcome, load_game
from games_dir.GuessGame import guess_game
from games_dir.CurrencyRoulellte import get_currency_value
from games_dir.MemoryGame import memory_game
from score_service.score import add_score
import time

### Welcome
print(welcome())

def get_ready():
    for i in range(0,5):
        print(f"The game will begin in {5-i}")
        time.sleep(1)

def play(game, diff):
    if game == 1:
        get_ready()
    games_list = [None, memory_game, guess_game, get_currency_value]
    for i in range(len(games_list)):
        if i == game:
            play = games_list[i](diff)
            if play[1] == 1:
                print('Winner')
                return 1
            else:
                print('Losser')
                return -1

### Load Game
while True:
    loading = load_game()
    print(loading[0])
    play(loading[1], loading[2])
    total_new_score = add_score(loading[2])
    break

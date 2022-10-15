from Live import welcome, load_game
from games_dir.GuessGame import guess_game
from games_dir.CurrencyRoulellte import get_currency_value
from games_dir.MemoryGame import memory_game
from MainScores import score_server
from score import add_score
import time

### Welcome
print(welcome())

def get_ready():
    for i in range(0,5):
        print(f"The game will begin in {5-i}")
        time.sleep(i)

def play(game, diff):
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
    winORlose = play(loading[1], loading[2])
    if winORlose == 1:
        total_new_score = add_score(loading[2])
        show_new_score = score_server(total_new_score, status_code=0)
        #print(total_new_score)
    else:
        break
    break

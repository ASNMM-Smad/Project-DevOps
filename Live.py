def welcome():
    user_name = input("Enter your name: ")
    if isinstance(user_name, str) == True:
        return f"Hello {user_name}, and welcome to the world of games\nHere you can find many cool games."
    else:
        return False

def load_game():
    games = []
    games_list = {"Memory Game": "A sequence of numbers will appear for 1 second and you have to guess it back.", 
                "Guess Game":"Guess a number and see if you chose like the computer.",
                "Currency Roulellte": "try and guess the value of a random amount of USD in ILS."}

    print("\nChoose a game by its number:")
    count = 1
    for key, value in games_list.items():
        print(f"{count}){key}: {value}\n", end="")
        games.append(key)
        count += 1
    choose_game = input(f"#### Choose 1-{count-1}: ")
    dif_level = input("Please choose game difficulty from 1 to 5: ")

    if (choose_game.isdigit()) and (dif_level.isdigit()):
        choose_game = int(choose_game)
        dif_level = int(dif_level)
        if (3 >= choose_game >= 0) and (5 >= dif_level >= 0):
            print("#####################################")
            pass
        else:
            print('\nProvided values do NOT exist.')    
            return -1    
    else:
        print("\nProvided value is NOT a Number, try again.")
        return -1

    return f'Game = {games[choose_game-1]}, Level = {dif_level}.', choose_game, dif_level

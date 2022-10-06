import random
import time

def memory_game(diff):
    print("Game Discriptions:\nPlease enter NUMBERS only.\nNote that if you enter more numbers than need compare to the difficult, it will count the first number only.")
    difficult_list = [None, 6, 11, 16, 21, 26]
    start_game = []
    final_result = []
    for i in range(1, difficult_list[diff]):
        rand_int = random.randint(1, 100)
        start_game.append(rand_int)

    display_numbers = 0
    user_input = []
    for p in start_game:
        if display_numbers == 0:
            print (start_game, end='\r')
            time.sleep(0.7)
            display_numbers += 1
        inputing = input('Enter all the numbers you remember with space between them:\n')
        try:
            inputing = inputing.split(' ')
            for i in inputing:
                user_input.append(int(i))
        except Exception as e:
            print(e)
        if len(user_input) >= len(start_game):
            break

    if len(user_input) >= len(start_game):
        final_result = user_input[0: difficult_list[diff]-1]
        
    final_result.sort()
    start_game.sort()
    if (final_result == start_game):
        return "Winner!", True
    else:
        return "Losser!", False

        

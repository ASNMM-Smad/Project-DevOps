from currency_converter import CurrencyConverter
import random

def get_currency_value(lvl):
    conv = CurrencyConverter()
    rnd_num = random.randint(1, 100)
    get_money_interval = conv.convert(rnd_num, 'USD', 'ILS')
    diff = (get_money_interval - (5 - lvl), get_money_interval + (5 - lvl))
    user_guess = float(input('Guess the interval number: '))
    if user_guess >= diff[0] and user_guess <= diff[1]:
        return True
    else:
        return False

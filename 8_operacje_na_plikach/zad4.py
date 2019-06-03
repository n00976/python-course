#Wyświetl 3 losowe cytaty

import random

with open ('cytaty.txt', 'r' )as fopen:
    lines = fopen.readlines()
    quote_number = 0

    while quote_number < 3:
        quote = random.choice(lines)
        print(quote)
        quote_number = quote_number + 1

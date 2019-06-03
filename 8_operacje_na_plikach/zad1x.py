# Utwórz plik na pulpicie zawierający listę ok. 20 cytatów.
# Każdy cytat powinen się znaleźć w nowej linii.
# Utwórz funkcję, która losuje i wyświetla cytat na dziś.
import random
#lines = 'cytaty.txt'
def show_quote():
    with open ('cytaty.txt', 'r' )as fopen:
        lines = fopen.readlines()
        quote = random.choice(lines)
        quote = quote.split(".")
        print("*" * 100)
        for i in quote:
            print(i.center(100))
        print("*" * 100)

show_quote()
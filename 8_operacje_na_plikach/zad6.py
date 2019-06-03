#Rozpoznawanie kart. Utwórz plik zawierający numery kart kredytowych.
# Sprawdź, podziel kart do plików wg typów np. visa.txt, mastercard.txt,
# americanexpress.txt.


def is_visa(numer):
    if dlugosc not in [13, 16]:
        return False
    else:
        if numer[0] == "4":
            return True
        else:
            return False


def is_mastercard(numer):
    if dlugosc != 16:
        return False
    else:
        if int(numer[:2]) >= 51 and int(numer[:2]) <= 55:
            return True
        elif int(numer[:4]) >=2221 and int(numer[:4]) <= 2720:
            return True
        else:
            return False


def is_american_express(numer):
    if dlugosc != 15:
        return False
    else:
        if numer[:2] == '34' or numer[:2] == '37':
            return True
        else:
            return False

def save_to_file(card_type, numer):
    save_file = card_type + '.txt'
    with open (save_file, 'a') as sf:
        sf.write(numer + '\n')

def check_card(numer):
    if is_visa(numer):
        print("Visa")
        save_to_file('visa', numer)
    elif is_mastercard(numer):
        print("Mastercard")
        save_to_file('mastercard', numer)
    elif is_american_express(numer):
        print("American express")
        save_to_file('american_express', numer)
    else:
        print("błędny numer:" + numer)


with open ('numery_kart.txt', 'r') as fopen:
    karty = fopen.readlines()

for num in karty:
    num = num.replace('\n', "")
    dlugosc = len(num)
    if dlugosc not in [13, 15, 16]:
        print("to nie jest dobra karta")

    check_card(num)



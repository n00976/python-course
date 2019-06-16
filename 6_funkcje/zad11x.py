#Napisz program, który na podstawie numeru karty odpowie czy ma doczynienia z Visą,
# MasterCard, a może American Express.
#Co wiemy o tych numerach tych kart?
#All Visa card numbers start with a 4. New cards have 16 digits. Old cards have 13.
#MasterCard numbers either start with the numbers 51 through 55 or with the
# numbers 2221 through 2720. All have 16 digits.
#American Express card numbers start with 34 or 37 and have 15 digits.


numer = input("podaj numer karty:")

dlugosc = len(numer)

if dlugosc not in [13, 15, 16]:
    print("to nie jest dobra karta")


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

def check_card():
    if is_visa(numer):
        print("Visa")
    elif is_mastercard(numer):
        print("Mastercard")
    elif is_american_express(numer):
        print("American express")
    else:
        print("Spadaj gościu")


check_card()

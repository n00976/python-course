#Wróć do pierwszego zadania z lekcji o plikach, zmodyfikuj go tak, aby to użytkownik
# podawał nazwę pliku z cytatami. Pamiętaj, by użytkownik po wykonaniu błędnej akcji
# (np. literówki w nazwie pliku) miał możliwość poprawić swój błąd.

import random

def show_quote():
    file_name = input("Podaj nazwę pliku z cytatami: ")
    with open(file_name, 'r')as fopen:
        lines = fopen.readlines()
        quote = random.choice(lines)
        quote = quote.split(".")
        print("*" * 100)
        for i in quote:
            print(i.center(100))
        print("*" * 100)


def find_error():
    while True:
        try:
            show_quote()
        except FileNotFoundError as error:
            print("O nie! Taki plik nie istnieje! Błąd: ", error)
            continue
        break


def main():
    find_error()



if __name__ == "__main__":
    print ('Plik uruchomiony bezpośrednio')
    main()
else:
    print ('Plik zaimportowano jako moduł')

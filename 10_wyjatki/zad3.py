#Stwórz listę 10 elementową (różne typy!). Pozwól użytkownikowi podać dowolny index.
# Podziel 1 przez liczbę pod indexem wybranym przez użytkownika. Obsłuż błędy.


def divide_elements(x):
    element_list = ['a', 5, 6, 8.9, '9', 0, 0.2, (5, 6), {9, 'kot'}, 'lol']
    try:
        division = 1 /element_list[x]
        print('Twój wybór to: ', element_list[x])
        print('wynik dzielenia to: ', division)
    except(ZeroDivisionError, TypeError, IndexError) as error:
        print("wystąpił błąd: ", error)

def main():
    x = int(input("podaj indeks wybranej liczby, przez którą chcesz podzielić 1:"))
    divide_elements(x)

if __name__ == "__main__":
    print('Plik uruchomiony bezpośrednio')
    main()
else:
    print('Plik zaimportowano jako moduł')

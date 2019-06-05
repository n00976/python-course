#Stwórz listę składającą się z kilku elementów różnego typu.
# W pętli spróbuj wykonać dzielenie 10 przez wartość z listy.
# Złap wyjątki jakie mogą się przy tej okazji wydarzyć.


def divide_elements():
    element_list = ['a', 2, 2.5, 0, ['c', 2], {2}, (5, 6)]

    for element in element_list:
        try:
            print('wartość to: ', element)
            division = 10 / element
            print('wynik: ', division)
        except(ValueError, ZeroDivisionError, TypeError) as error:
            print("wystąpił błąd: ", error)

def main():
    divide_elements()


if __name__ == "__main__":
    print('Plik uruchomiony bezpośrednio')
    main()
else:
    print('Plik zaimportowano jako moduł')


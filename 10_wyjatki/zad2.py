#Utwórz dowolną krotkę zawierającą kilka wartości np. 10.
# Pozwól użytkownikowi podać dowolny index oraz wartość.
# Spróbuj w krotce podmienić wartość na zadanym indeksie. Obsłuż błąd



def change_item(user_index, user_element):
    my_tuple = (4, 8, 'f', 5.2, [5, 6], 'l', 'pizza')
    try:
        my_tuple[user_index] = user_element
    except TypeError as error:
        print("Oops, nie można podmieniać elementów w krotce!")

def main():
    user_index = int(input("podaj numer ideksu, pod którym wartość ma zostać zmieniona:"))
    user_element = input("Podaj, na co chcesz zmienić wybrany element:")
    change_item(user_index,user_element)

if __name__ == "__main__":
    print('Plik uruchomiony bezpośrednio')
    main()
else:
    print('Plik zaimportowano jako moduł')

# Sprawdź czy liczba podana przez użytkownika jest podzielna przez 3 bez reszty.

liczba = float(input("podaj liczbę:"))
modulo = liczba % 3

if modulo == 0:
    print("Twoja liczba jest podzielna przez 3")
else:
    print("Twoja liczba nie jest podzielna przez 3")

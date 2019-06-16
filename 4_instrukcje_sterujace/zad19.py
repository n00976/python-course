#Stwórz grę ciepło zimno.
#Komputer losuje liczbę z zakresu od 1 do 100.
#Użytkownik podaje swój traf.
#Komuter odpowiada ciepło zimno, ale nie więcej niż 6 razy.
#Jeśli użytkownik zgadnie wygrywa gracz.
#Jeśli po 6 próbach użytkonik nie zgadnie - wygrywa komputer.

import random

print("zagramy w grę ciepło-zimno.")
liczba_komp = int(random.randrange(1, 100))
liczba_player = int(input("Podaj swój traf:"))
print(liczba_komp)
while liczba_player != liczba_komp:
    if liczba_player == liczba_komp:
        print("Gratulacje, zgadłeś!")
    elif liczba_player >= liczba_komp - 5 or liczba_player >= liczba_komp + 5:
        input("Bardzo ciepło! Próbuj dalej:")
    elif liczba_player >= liczba_komp - 10 or liczba_player >= liczba_komp +10:
        input("Ciepło! Próbuj dalej:")
    else:
        input("Zimno! Próbuj dalej:")



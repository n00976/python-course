#4 Napisz grę - kamień (k) / papier (p) / nożyce (n).
# Użytkonik podaje jedną z 3 figur
# Komputer losuje jedną z 3 figur*
# Sprawdź kto wygrał tę rundę
# Zmień kod tak, by użytkownik mógł podac liczbę rund.
# Wygrana jest podawana komputer vs użytkownik.
# Zmień tak, by gracz mógł zakończyć grę w dowolnej chwili przez np. hasło ‘koniec’

import random

print("Zagramy w papier, kamień nożyce. Jeżeli będziesz chciał przerwać grę, zamiast wyboru figury wpisz 4")

n = int(input("Podaj liczbę rund:"))

for i in range(n):

    fig = int(input("\n1.kamień \n2.papier \n3.nożyce? \n4.przerwij grę \n Wpisz cyfrę odpowiadającą Twojemu wyborowi:"))
    komp = random.randrange(1, 3)

    if fig == komp:
        print("Wybrałeś " + str(fig) + " , a wybór przeciwnika to " + str(komp) + ". Remis!")
    elif fig == 1 and komp == 3:
        print("Wybrałeś kamień , a wybór przeciwnika to nożyce. Wygrywasz!")
    elif fig == 2 and komp == 1:
        print("Wybrałeś papier, a wybór przeciwnika to kamień. Wygrywasz!")
    elif fig == 3 and komp == 2:
        print("Wybrałeś nożyce, a wybór przeciwnika to papier. Wygrywasz!")
    elif fig == 1 and komp == 2:
        print("Wybrałeś kamień, a wybór przeciwnika to papier. Przegrałeś!")
    elif fig == 2 and komp == 3:
        print("Wybrałeś papier, a wybór przeciwnika to nożyce. Przegrałeś!")
    elif fig == 3 and komp == 1:
        print("Wybrałeś nożyce, a wybór przeciwnika to kamień. Przegrałeś!")
    elif fig ==4:
        break


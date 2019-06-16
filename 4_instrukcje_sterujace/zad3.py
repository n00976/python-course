#Stwórz skrypt, który przyjmuje 3 opinie użytkownika o książce.
# Oblicz średnią opinię o książce. W zależności od wyniku dodaj komunikaty.
# Jeśli uzytkownik ocenił książkę na ponad 7 - bardzo dobry, ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi.

bohaterowie =int(input("podaj swoją opinię o bohaterach książki od 1 -10:"))
okladka =int(input("podaj swoją opinię o okladce książki od 1 -10:"))
dlugosc =int(input("podaj swoją opinię o długości książki od 1 -10:"))

srednia = (bohaterowie + okladka + dlugosc)/3

if srednia > 7:
    print("książka jest bardzo dobra")
elif srednia > 4:
    print("książka jest przeciętna")
else:
    print("książka nie jest warta uwagi")
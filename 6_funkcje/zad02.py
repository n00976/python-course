#Napisz funkcję, która pyta użytkownika o pary książka + ocena i zapisuje je w programie.

def books ():
    biblioteka = {}
    ile = int(input("Ile książek?"))
    for i in range(ile):
        title = input("Podaj książkę:")
        grade = int(input("Podaj ocenę książki:"))
        biblioteka[title] = grade
    return biblioteka

def znajdz_ksiazke(title):
    print("Ocena wybranej książki to: " + title + " to: " + bibl[title])


bibl = books()
ksiazka = input("Jakiej książki ocenę chcesz sprawdzić?:")
znajdz_ksiazke(ksiazka)

if ksiazka in bibl:
    znajdz_ksiazke(ksiazka)
else:
    print("Niestety nie mamy tej pozycji w bibliotece :(")
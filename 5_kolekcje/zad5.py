#Utwórz “na sztywno” 2-wymiarową tablicę, tak, by kolejne wiersze zawierały dane osób,
# natomiast w kolumnach będzie znajdować się imię, nazwisko, zawód, np:
#Dorota, Wellman, dziennikarka
#Adam, Małysz, sportowiec
#Robert, Lewandowski, piłkarz
#Krystyna, Janda, aktorka
#Wyświetl w sposób przyjazny dla użytkownika

# lista = [
#     ["Dorota", "Wellman", "Dziennikarka"],
#     ["Ania", "Kowalska", "Lekarz"],
#     ["Adam", "Małysz", "Sportowiec"],
#     ["Krystyna", "Janda", "Aktorka"]
# ]

lista = []
for i in range(3):
    name = input("podaj imię:")
    surname = input("podaj nazwisko")
    job = input("podaj zawód:")
    lista.append([name, surname, job])

for i in lista:

    print('\t'.join(i))








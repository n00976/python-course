#Utwórz dowolną tablicę n x n zawierającą dowolny znak,
# a następnie wyświetl jej elementy w formie tabeli n x n.
# Elementy powinny być oddzielone spacją

znaki = input("Podaj dowolny znak:")

n = int(input("Podaj wymiar tablicy nxn:"))

lista = [[znaki] * n] * n

for i in lista:
    print(' '.join(i))











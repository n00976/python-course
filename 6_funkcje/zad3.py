#Napisać funkcję, która przyjmuje listę liczb i zwraca sumę wszystkich elementów na liście.

liczby = []
n = int(input("Podaj liczbę liczb, które chcesz zsumować:"))
def suma_liczb():
    for i in range(n):
        liczby.append(int(input("dodaj liczbę do listy:")))
    suma = sum(liczby)
    print(suma)

suma_liczb()



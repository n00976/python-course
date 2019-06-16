#Nie korzystając z funkcji wbudowanej min(),
#napisz funkcję znajdującą minimalną wartość z 3 liczb. minimum_of(a, b, c).

def min_of_2(a, b):
    return a if a < b else b
    #if a > b:
    #    return a
    #else:
    #    return b


def minimum_of(num1, num2, num3):
    return min_of_2(min_of_2(num1, num2), num3)

a = int(input("podaj 1 liczbę:"))
b = int(input("podaj 2 liczbę:"))
c = int(input("podaj 3 liczbę:"))
najmniejsza = minimum_of(a,b, c)
print("Najmniejsza liczba to: ", najmniejsza)
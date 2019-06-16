#Nie korzystając z funkcji wbudowanej max(),
#napisz funkcję znajdującą maksymalną wartość z 3 liczb. maximum_of(a, b, c).

def max_of_2(a, b):
    return a if a > b else b
    #if a > b:
    #    return a
    #else:
    #    return b


def maximum_of(num1, num2, num3):
    return max_of_2(max_of_2(num1, num2), num3)

a = int(input("podaj 1 liczbę:"))
b = int(input("podaj 2 liczbę:"))
c = int(input("podaj 3 liczbę:"))
najwieksza = maximum_of(a,b, c)
print("Największa liczba to: ", najwieksza)
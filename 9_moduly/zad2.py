#Stwórz moduł, który przechowuje wzór na deltę. Skorzystaj z wbudowanego modułu math.
#W nowym pliku wykorzystaj moduł.

import modul_zad2 as m2

def main():
    a = float(input("podaj współczynnik równania a:"))
    b = float(input("podaj współczynnik równania b:"))
    c = float(input("podaj współczynnik równania c:"))
    m2.calculate_delta(a, b, c)

main()


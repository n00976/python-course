# Zadanie 4
# Napisz skrypt, który zapyta użytkownika o trzy liczby całkowite,
# a następnie pomnóż dwa pierwsze. przed podzieleniem wyniku przez trzecią liczbę. 
# Wejście i wyjście powinny być zrozumiałe dla użytkownika.
print("Hej! To program, który wykonuje działania na trzech podanych przez Ciebie liczbach całkowitych.")
x = int(input("Proszę, podaj pierwszą liczbę:"))
y = int(input("Proszę, podaj drugą liczbę:"))
z = int(input("Proszę, podaj trzecią liczbę:"))
print("teraz program pomnoży przez siebie dwie pierwsze liczby")
multiply = x * y
print("wynik to:")
print(str(multiply))
print("a teraz podzieli wynik przez trzecią liczbę")
divide = multiply / z
print("wynik to:")
print(str(divide))
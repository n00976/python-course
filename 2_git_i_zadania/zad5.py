# Zadanie 5
# Napisz program, który pyta użytkownika o 2 liczby
# a następnie dzieli jedna przez drugą.
# Pokaż ile razy pierwsza liczba mieści się w drugiej
# oraz jaka jest reszta tego dzielenia. 
print("Prosze o podanie 2 liczb, które chciałbyś przez siebie podzielić:")
x = float(input("Pierwsza liczba:"))
y = float(input("Druga liczba:"))
divide = x / y
print("Wynik dzielenia tych 2 liczb przez siebie to: " + str(divide))
div = x // y
print("Pierwsza liczba mieści się w drugiej " + str(div) + " razy" )
reszta = x % y
print("a reszta z tego dzielenia to " + str(reszta))
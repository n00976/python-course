#Dla podanej przez użytkownika liście liczb całkowitych sprawdź czy pierwszy i ostatni element są takie same.

liczby = input("podaj listę liczb całkowitych przedzielonych przecinkami:")
liczby_1 = liczby.split(",")

if liczby[0] == liczby[-1]:
    print("Pierwsza i ostatnia liczba są takie same")
else:
    print("Pierwsza i ostatnia liczba nie są takie same")

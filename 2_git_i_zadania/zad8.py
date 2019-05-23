# Zadanie 8
#Ulepsz program z zadania 7, tak aby zwrócił ile banknotów
# 50, 20, 10 i 5 euro otrzyma użytkownik.

print("Przelicznik walut")
zlote = float(input("Proszę, podaj kwotę pieniędzy, którą chcesz wziąć na wakacje:"))
euro = zlote // 4.30385192
dolary = zlote // 3.82362388
print("Twoja kwota w euro to: " + str(euro))
print("Twoja kwota w dolarach to:" + str(dolary))
p = euro // 50
reszta = euro % 50
d = reszta // 20
resztad = reszta % 20
dz = resztad // 10
resztadz = resztad % 10
pi = resztadz // 5
print("Otrzymasz " + str(p) + " banknotów 50 euro, " + str(d) + " banknotów 20 euro, " + str(dz) + " banknotów 10 euro i " + str(pi)+ " banknotów 5 euro")

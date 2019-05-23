# Zadanie 6
# Zarówno lodówka, jak i winda mają wysokość, szerokość i głębokość. 
# Dowiedz się, ile miejsca pozostało w windzie, gdy lodówka jest w środku.
# Załóżmy, że wymiary lodówki zawsze będą mniejsze niż windy ( jest to prawdopodobne?)
# Wejście i wyjście powinny być zrozumiałe dla użytkownika.
print("To program, który policzy, czy lodówka, którą wniesiemy do windy się w niej zmieści i ile pozostanie miejsca w windzie.")
print("Proszę, podaj wymiary windy w cm")
wysokoscw = float(input("Wysokość:"))
szerokoscw = float(input("Szerokość:"))
glebokoscw = float(input("Głębokość:"))
vw = wysokoscw * szerokoscw * glebokoscw
print("Twoja winda ma objętość " + str(vw) + " cm3")
print("Proszę, podaj wymiary lodówki w cm")
wysokoscl = float(input("Wysokość:"))
if wysokoscl > wysokoscw :
    print("Twoja lodówka nie zmieści się w windzie!")

szerokoscl = float(input("Szerokość:"))
if szerokoscl > szerokoscw :
    print("Twoja lodówka nie zmieści się w windzie!")
glebokoscl = float(input("Głębokość:"))
if glebokoscl > glebokoscw :
    print("Twoja lodówka nie zmieści się w windzie!")
vl = wysokoscl * szerokoscl * glebokoscl
print("Twoja winda ma objętość " + str(vl) + " cm3")
miejsce = vw - vl
print("W windzie po włożeniu lodówki pozostanie " + str(miejsce) +" cm3 miejsca")

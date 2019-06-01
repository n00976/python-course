#Oblicz koszt wyprawy znając dystans, spalanie na 100km i cenę litra benzyny.
# Załóżmy, że spalanie na 100km wynosi 6,4 l, trasa to 120km, litr benzyny kosztuje 5,04 zł.
#Zmodyfikuj skrypt tak, by przyjmował wartości od użytkownika.

print("Koszt wyprawy przy spalaniu 6,4 l na 100 km, dystans - 120 km, litr benzyny kosztuje 5,04 zł")

spalanie = float(input("Ile wynosi spalanie na 100 km(l)?"))
trasa = float(input("Ile kilometrów masz do pokonania?"))
trasa = trasa/100
litr_benzyny = float(input("ile kosztuje litr benzyny? (zł):"))
benzyna = spalanie * trasa
koszt = spalanie * trasa * litr_benzyny
print("ilość benzyny potrzebnej na wyprawę to:" + str(benzyna) + " l")
print("koszt wyprawy to " + str(koszt) + "zł")
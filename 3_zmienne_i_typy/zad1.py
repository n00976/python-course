#Oblicz koszt wyprawy znając dystans, spalanie na 100km i cenę litra benzyny.
# Załóżmy, że spalanie na 100km wynosi 6,4 l, trasa to 120km, litr benzyny kosztuje 5,04 zł.

print("Koszt wyprawy przy spalaniu 6,4 l na 100 km, dystans - 120 km, litr benzyny kosztuje 5,04 zł")
b = 6.4
d = 1.2
lb = 5.04
benzyna = b * d
koszt = b * d * lb
print("ilość benzyny potrzebnej na wyprawę to:" + str(benzyna) + " l")
print("koszt wyprawy to " + str(koszt) + "zł")
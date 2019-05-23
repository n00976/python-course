wzrost = input ("Jaki jest Twój wzrost w metrach? ")
waga = input ("Ile ważysz (kg)? ")

lwzrost = float(wzrost)
lwaga = float(waga)
print()
print("Twoje BMI to:")
print(round(lwaga/(lwzrost**2), 2))


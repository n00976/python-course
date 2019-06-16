# Skorzystaj ze swojego kodu bmi.py.
# Rozbij liczenie bmi na funkcję obliczającą bmi
# na podstawie danych użytkownika oraz zwracającą
# odpowiednią wartość (niedowaga, waga normalna, nadwaga, otyłość)
# w zależności od otrzymanego parametru.

def bmi():
    wzrost = float(input ("Jaki jest Twój wzrost w metrach? "))
    waga = float(input ("Ile ważysz (kg)? "))
    wynik = round(waga/(wzrost**2), 2)
    print("Twoje BMI to: " + str(wynik))
    if wynik < 18.5:
        print("Masz niedowagę, zjedz pizzę!")
    elif 18.5 < wynik < 25:
        print("Twoje bmi jest ok!")
    elif wynik > 25:
        print("Masz nadwagę")
    elif wynik > 30:
        print("Jesteś otyły")

bmi()



#niedowaga: <18,5// prawidłowe bmi: 18,5 - 24,9// nadwaga: >25 //otylosc >30
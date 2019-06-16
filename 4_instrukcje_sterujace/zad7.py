#Rozwiń kod bmi.py z pierwszych zajęć dodając teraz instrukcję warunkową,
# która wyświetli w zależności od wyniku: niedowaga / waga normalna / nadwaga / otyłość.



wzrost = float(input ("Jaki jest Twój wzrost w metrach? "))
waga = float(input ("Ile ważysz (kg)? "))

bmi = round(waga/(wzrost**2), 2)

print("Twoje BMI to: " + str(bmi))



if bmi < 18.5:
    print("masz niedowagę")
elif 18.5 <= bmi <24.99:
    print("twoja waga jest prawidłowa")
elif bmi >= 25:
    print("masz nadwagę")

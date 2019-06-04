#Stwórz moduł, który będzie przechowywał funkcję obliczającą bmi.py.
# Zaimportuj module do pliku fitmeter.py. Nowy plik będzie informował użytkownika o jego aktualnym BMI
# i na podstawie wyniku (niedowaga, nadwaga, otyłość) sugerował zmiany w stylu życia pobierane
# z odpowiedniego pliku.


import module_bmi as mbmi

def main():
    waga = float(input("waga:"))
    wzrost = float(input("wzrost:"))
    mbmi.bmi(waga, wzrost)

main()


#W kodzie BMI ufamy, że użytkownik podaje wartość w kilogramach lub w metrach
# i rzutujemy do float. Co jeśli użytkownik poda wartość 60 kg ? Zmodyfikuj kod
# z ostatnich zajęć tak, aby wykluczyć powyższy przypadek.



def bmi(waga, wzrost):
    bmi = round(waga/(wzrost**2), 2)
    print("Twoje BMI to: " + str(bmi))
    if bmi < 18.5:
        print("niedowaga")
    elif 18.5 <= bmi <24.99:
        print("nadwaga")
    elif bmi >= 25:
        print("waga ok")
    return bmi


def main():
    while True:
        try:
            waga = float(input("waga:"))
            wzrost = float(input("wzrost:"))
            bmi(waga, wzrost)
        except (ValueError, ZeroDivisionError) as error:
            print('O nie, wpisałeś złą wartość! Błąd: ', error)
            continue
        break


if __name__ == "__main__":
    print('Plik uruchomiony bezpośrednio')
    main()
else:
    print('Plik zaimportowano jako moduł')

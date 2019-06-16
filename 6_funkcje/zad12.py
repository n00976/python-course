#Napisz program, który będzie sprawdzał, czy nasz samochód kwalifikuje się do zarejestrowania jako zabytek.
   #Program zacznie ze stworzonym słownikiem o trzech kluczach:
   #         marka (str)
    #        model (str)
     #       rocznik (int)

    #Wypisze ten słownik na ekran (bez żadnego formatowania)
    #Sprawdzi, czy samochód ma minimum 25 lat. Jeśli tak, wypisze komunikat:
    #    “Gratulacje! Twój samochód (tutaj_marka) może być zarejestrowany jako zabytek.”
    #Jeśli nie spełnia powyższego warunku, wypisze komunikat:
    #    “Twój samochód (tutaj_marka) jest jeszcze zbyt młody.”
    #Gdy program będzie poprawnie działał, pozmieniaj wartości słownika (ale nie klucze!),
    # aby zobaczyć, czy progam również zmienia swoje zachowanie.

auta = {
    "marka": "Citroen",
    "model": "2CV",
    "rocznik": 1972
}

print(auta)

def is_vintage():
    if auta["rocznik"] <= 1994:
        print("Gratulacje! Twój samochód ", auta["marka"], " może być zarejestrowany jako zabytek.")
    else:
        print("Twój samochód ", auta["marka"], " jest jeszcze zbyt młody.")

is_vintage()
#Kolejnym warunkiem, aby dostać “żółte tablice”, jest to, aby samochód posiadał
# co najmniej 75% oryginalnych części. W naszym zadaniu zakładamy, że rzeczoznawca
# określił jego oryginalność w kategorii tak/nie.
    #Poniżej stworzenia i wyświetlenia słownika w zadaniu powyżej:
    #       dopisz do słownika nowy klucz czy_oryginalny i ustaw jego wartość (typ: bool) wedle uznania.
    #      ponownie wyświetl zmieniony słownik
    #Zmodyfikuj program tak, aby uwzględnił decyzję o możliwości zarejestrowania samochodu
    # również od jego oryginalności. Dopisz odpowiednie komunikaty.

auta = {
    "marka": "Citroen",
    "model": "2CV",
    "rocznik": 1972,
    "czy_oryginalny": True
}

print(auta)

def is_vintage():
    if auta["rocznik"] <= 1994 and auta["czy_oryginalny"] == True:
        print("Gratulacje! Twój samochód ", auta["marka"], " może być zarejestrowany jako zabytek.")
    elif auta["rocznik"] <= 1994 and auta["czy_oryginalny"] == False:
        print(" Twój samochód ", auta["marka"], " nie posiada 75% oryginalnych części")
    else:
        print("Twój samochód ", auta["marka"], " jest jeszcze zbyt młody.")

is_vintage()
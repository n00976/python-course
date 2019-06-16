#Zapytaj użytkownika o numer od 1 do 100, jeśli użytkownik zgadnie liczbę
# ukrytą przez programistę wyświetl komunikat “gratulacje!”, w przeciwnym
# razie “pudło!”.

moja_liczba = 29
liczba_user = int(input("Zgadnij liczbę (1-100), którą wybrałam:"))

if liczba_user == moja_liczba:
    print("gratulacje!")
else:
    print("pudło!")
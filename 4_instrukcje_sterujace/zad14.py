# Napisz grę, w której użytkownik musi zgadnąć liczbę od 0 - 20 (np. secret_num = 5).
# Pytaj użytkownika o podanie liczby tak długo, aż nie zgadnie.

secret_num = 6

user_number = int(input("zgadnij liczbę 0-20:"))

while True:
    if user_number == secret_num:
        print("gratulacje, udało Ci się! sekretna liczba to 6!")
        break
    else:
        user_number = int(input("to nie ta! zgadnij liczbę:"))





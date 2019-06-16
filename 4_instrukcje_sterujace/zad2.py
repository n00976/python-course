#Pobierz dwie wartości int od użytkownika i oblicz ich sumę.
# Jeśli suma jest większa niż 100, wyświetl ich sumę.

first_value = int(input("podaj pierwszą liczbę:"))
second_value = int(input("podaj drugą liczbę:"))

add_values = first_value + second_value
if add_values > 100:
    print(add_values)

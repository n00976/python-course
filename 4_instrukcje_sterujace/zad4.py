#Utwórz zmienną przechowującą dowolny ciąg znaków.
# Sprawdź czy string jest dłuższy od 5 oraz czy zawiera literę a.
# Jeśli zawiera, wszystkie litery a podmień na z.

letters = input("podaj dowolny ciąg znaków:")
letters_length = len(letters)

if letters_length > 5:
    print("ciąg jest dłuższy od 5")

is_a = letters.count("a")

if is_a >= 1:
    letters = letters.replace("a", "z")
    print(letters)
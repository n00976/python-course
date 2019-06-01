#Palindrom to wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej
# np.: Kobyła ma mały bok. Pozwól użytkownikowi wprowadzić dowolne zdanie.
# Następnie sprawdź czy wprowadzone wyrażenie jest palindromem.

czy_palindrom = input("wpisz dowolne zdanie (bez kropki):")
x = czy_palindrom
print(x)
y = czy_palindrom[::-1]
print(y)
print(x == y)
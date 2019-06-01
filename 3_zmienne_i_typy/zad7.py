#Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron, a następnie:
    #Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.
    #Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich
    #Połącz dane w jeden ciąg book za pomocą spacji
    #Policz liczbę wszystkich znaków w napisie book

title = input("Podaj tytuł książki:")
author = input("Podaj nazwisko autora:")
pages = input("Podaj liczbę stron:")

print(title.isalpha())
print(author.isalpha())
print(pages.isdecimal())

title = title.capitalize()
author = author.capitalize()


book = title + " " + author + " " + pages
print(len(book))
print(book)



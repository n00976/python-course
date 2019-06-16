#Pobierz od użytkownika dowolny tekst i wyświetl tylko te znaki, które są na pozycjach parzystych.
#Wykonaj na dwa sposoby - za pomocą pętli oraz przez sting slicing ( ‘abrakadabra’ -> ‘baaar’).

user_text = input("wpisz dowolny tekst:")

#za pomocą pętli

n = 0
while n <= len(user_text):
    print(user_text[n])
    n = n + 2

#string slicing

print(user_text[::2])

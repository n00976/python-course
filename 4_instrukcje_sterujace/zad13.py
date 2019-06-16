#Napisz program zmieniający skalę w stopniach Fahrenheita na nasz Celcjusza.
# Program powinen wykonać się w pętli od 0 do 200 stopni Fahrenheit, co 20 stopni.

    #C = 5/9 * (F - 32) # wzór Celsjusz → Fahrenheit
start = 0
limit = 200
step = 20
fahrenheit = start


while (fahrenheit <= 200):
    celsius = 5/9 * (fahrenheit - 32)
    print(fahrenheit, "\t", celsius)
    fahrenheit = fahrenheit + 20

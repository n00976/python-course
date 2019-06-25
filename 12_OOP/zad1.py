#Skorzystaj z wprowadzenia do OOP. Stwórz klasę Pies, która posiada wspomniane atrybuty oraz metodę.
#       atrybuty: imię, kolor sierści, rasę
#        metody: szczekaj, machaj ogonem
#Utwórz kilka obiektów klasy Pies z różnymi parametrami.


class Dog:
    def __init__(self, name, colour, race):
        self.name = name
        self.colour = colour
        self.race = race
    def howl(self):
        print(self.name + ' says: I want to go out')
    def tail_wave(self):
        print(self.name + 'says: I\'m happy')

def main():
    pies1 = Dog('Burek', 'czarny', 'mops')
    pies2 = Dog('Legolas', 'kremowy', 'chart')

    pies2.howl()

if __name__ == "__main__":
    print('Plik uruchomiony bezpośrednio')
    main()
else:
    print('Plik zaimportowano jako moduł')




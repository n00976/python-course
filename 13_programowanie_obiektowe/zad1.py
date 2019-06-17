#Korzystając z wikipedii utwórz klasy - Kot, Pies, Człowiek.
#Każda z nich powinna dziedziczyć z nadrzędnej klasy Ssaki.
#Klasa Ssaki powinna dziedziczyć z klasy Zwierzęta.
#Utwórz obiekty klas - kot, pies i człowiek, udowodnij, że rzeczywiście korzystają z klas rodziców.
#Do klasy człowiek dodaj metodę super() tak, aby móc wyświetlić opis dostępny gdziekolwiek w klasie ssaki.

class Animals:
    def __init__(self):
        print("Animals breathe oxygen.")

    def eat(self):
        print("Animals have to eat to get energy. They consume organic material.")


class Mammals(Animals):
    def __init__(self):
        print("Mammals have constant body temperature")

    def angry(self):
        print("When mammals are angry they behave different.")


class Cat(Mammals):
    def __init__(self, name, race, colour, hair):
        self.name = name
        self.race = race
        self.colour = colour
        self.hair = hair

    def angry(self):
        super().angry()
        print("I'm angry, I hiss")


class Dog(Mammals):
    def __init__(self, name, colour, race, size):
        self.name = name
        self.colour = colour
        self.race = race
        self.size = size

    def angry(self):
        super().angry()
        print("I'm angry, I bark")


class Human(Mammals):
    def __init__(self, name, nationality, character):
        self.name = name
        self.nationality = nationality
        self.character = character
        super().__init__()

    def angry(self):
        super().angry()
        if self.character == 'shy':
            print("I'm angry, I do not talk to other people.")
        else:
            print("I'm angry, I shout at people.")


cat1 = Cat('Paweł', 'british', 'blue', 'shorthair')
person1 = Human('Kuba', 'Polish', 'bad-tempered')


person1.angry()


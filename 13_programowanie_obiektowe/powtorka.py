class Canis:
    ears = 2
    food = 'meat'

    def __init__(self, place):
        self.place = place

    def angry(self):
            print("I'm angry, I will bite")


class Dog(Canis):
    def __init__(self, name, colour, race, size):
        self.name = name
        self.colour = colour
        self.race = race
        self.size = size


    def howl(self, sound = 'howhow'):
        if self.size == 'small':
            print(self.name + ' says: ' + sound + ' I want to eat')
        elif self.size == 'medium':
            print(self.name + ' says: ' + sound + ' I want to go out')
        else:
            print(self.name + ' says: ' + sound + ' I don\'t know what I want but if you\'d give me sth to eat I\'ll be happy')

    def angry(self):
        super().angry()
        print("I'm angry, I need to eat")

dog1 = Dog('Juliusz', 'black', 'pug', 'small')

dog1.howl('ufuf')
dog1.angry()
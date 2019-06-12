#Pomyśl co sprawia, że ssak jest ssakiem? Utwórz klasę ssaki. Stwórz kilka obiektów klasy ssaki np. wilk, koń, ssaki.

class Mammals:

    def __init__(self, fur, colour, locomotion, body_temperature, food_preference, how_many_legs):
        self.fur = fur
        self.colour = colour
        self.locomotion = locomotion
        self.body_temperature = body_temperature
        self.food_preference = food_preference
        self.how_many_legs = how_many_legs

def main():
    wolf = Mammals(True, ['grey', 'white'], 'legs', 40, 'meat', 4)
    cow = Mammals(True, ['white', 'black', 'brown'], 'legs', 38, 'plants', 4)
    killer_whale = Mammals(False, ['black', 'white'], 'swim', 37, 'meat', 0)

if __name__ == "__main__":
    print('Plik uruchomiony bezpośrednio')
    main()
else:
    print('Plik zaimportowano jako moduł')

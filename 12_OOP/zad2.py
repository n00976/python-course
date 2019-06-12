#Utwórz klasę dla storczyków. Storczyki z zasady mają różne kolory, pory kwitnienia, gatunki.
# Utwórz dowolne atrybuty i metody. Dodaj atrybut wspólny dla wszystkich storczyków - królestwo roślin.

class Orchis:

    kingdom = 'plants'

    def __init__(self, species, colour, blooming_month, insolation):
        self.species = species
        self.colour = colour
        self.blooming_month = blooming_month
        self.insolation = insolation
    def search_colur(self):
        col = input("what colour do you want?")
        if col in self.colour:
            print("this flower fits in your expectation")
        else:
            print("look for something else")
    def show_info(self):
        print('blooming months:')
        for i in self.blooming_month:
            print(i)


def main():
    storczyk1 = Orchis('Italica', ['white', 'light pink'], ['march', 'april', 'may'], ['sunny', 'moist'])
    storczyk2 = Orchis('spitzelii', ['purple', 'pink'], ['may', 'june', 'july'], '...' )
    storczyk3 = Orchis('pauciflora', ['white', 'yellow'], ['April', 'may'], '...' )

    storczyk3.show_info()
    storczyk1.search_colur()

if __name__ == "__main__":
    print('Plik uruchomiony bezpośrednio')
    main()
else:
    print('Plik zaimportowano jako moduł')

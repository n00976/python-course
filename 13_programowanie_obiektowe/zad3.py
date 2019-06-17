# Zadanie inspirowane popkulturą: https://www.youtube.com/watch?v=Ct6BUPvE2sM
#Stwórz klasę PenPinapple, która dziedziczy z klas Pen oraz Pinapple. Logiki to nie ma, więc dodaj wg uznania.


class Pen:
    def __init__(self):
        print("I can write anything")


class Pineapple:
    def __init__(self):
        print("I'm yummy and yellow")


class PenPineapple(Pen, Pineapple):
    def __init__(self):
        print("I'm not really useful")
        super().__init__()


pp = PenPineapple()
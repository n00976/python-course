from warrior import Warrior


class Knight(Warrior):

    def __init__(self):
        super().__init__()
        self.health = 60

    def attack(self):
        print('Knight: I swung my sword!')
        self.exp += 0.3
        return self.exp
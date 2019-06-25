from warrior import Warrior

class Archer(Warrior):

    def __init__(self):
        super().__init__()
        self.health = 40
        self.shots = 20

    def attack(self):
        if self.shots == 0:
            print("You don't have any more shots!")
        else:
            print('Archer: I shot an arrow!')
            self.exp += 0.4
            self.shots = self.shots - 1
        return self.exp
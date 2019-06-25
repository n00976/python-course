class Warrior:
    def __init__(self):
        self.exp = 0

    def __repr__(self):
        return '{}: HP = {}, EXP =  {}'.format(self.__class__.__name__, self.health, self.exp)

    def walk(self, distance):
        print(self.__class__.__name__ + ': I walked ' + str(distance) + 'm')
        self.exp = self.exp + (distance * 0.2)
        return self.exp

from jednostki.archer import Archer
from jednostki.knight import Knight

if __name__ == '__main__':
    knights = []
    for knight in range(4):
        knights.append(Knight())
    for knight in knights:
        print(knight)

    for knight in knights:
        knight.walk(2)

    knights.append(Knight())

    for knight in knights:
        knight.attack()

    for knight in knights:
        print(knight)

    archers = []
    for archer in range(3):
        archers.append(Archer())

    army = archers + knights
    for warrior in army:
        print(warrior)

    for warrior in army:
        warrior.attack()

    for warrior in army:
        print(warrior)


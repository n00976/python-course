class UsefulStuff:
    def __init__(self, name):
        print(name + 'is used to make life easier!')


class Computer(UsefulStuff):
    def __init__(self, type):
        print('on ' + type + ' you can search a lot of things')
        super().__init__(type)


class Shoes(UsefulStuff):
    def __init__(self, colour):
        print('you can\' t walk without your' + colour )
        super().__init__(colour)


class ComShoes(Computer, Shoes):
    def __init__(self):
        print('ComShoes is super nice! You can ask google anything while walking!')
        super().__init__('ComShoes')


cs = ComShoes()
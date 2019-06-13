#Utwórz klasę sklep. Sklep posiada różne produkty. W sklepie można pordukt zobaczyc, przymierzyc, kupic, zwrocic.

class Shop:

    def __init__(self, products):
        self.products = products
    def show(self):
        for i in self.products:
            print(i)
    def buy(self):
        index_cloth = int(input("Which cloth do you want to buy? Type index:"))
        self.products.pop(index_cloth)
    def giveback(self):
        cloth = input('imię:')
        self.products.append(cloth)
    def try_on(self):
        index_cloth = int(input("Which cloth do you want to try? Type index:"))
        print(Shop([index_cloth]))
        buy_or_not = input("do you want to buy it? y/n:")
        if buy_or_not == 'y':
            self.products.pop(index_cloth)
        else:
            pass

def main():
    products = Shop(['white sweater', 'black dress', 'cool trousers', 'comfy shoes'])
    products.try_on()
    products.show()


if __name__ == "__main__":
    print('Plik uruchomiony bezpośrednio')
    main()
else:
    print('Plik zaimportowano jako moduł')

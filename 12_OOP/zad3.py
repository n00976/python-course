#Stwórz własną implementację kolejki FIFO. Klasa Kolejka powinna na starcie przyjmować listę elementów.
# Wśród metod powinny się znaleźć takie jak: wyswietlenie kolejki, sprawdzenie czy jest pusta,
# dodanie elementu do kolejki (put), wyjęcie elementu z kolejki (get).
#Utwórz kilka obiektów klasyz różnymi parametrami.


class Queue:
    def __init__(self, people):
        self.people = people
    def show(self):
        for i in self.people:
            print(i)
    def put(self):
        new_person = input('imię:')
        self.people.append(new_person)
    def get(self):
        self.people.pop(0)
    def is_empty(self):
        number_of_people = len(self.people)
        if number_of_people == 0:
            return True
        else:
            return False


def main():
    kolejka = Queue(['Ania', 'Kasia', 'Ela'])

    kolejka.get()
    kolejka.show()
    kolejka.is_empty()
    kolejka.put()


if __name__ == "__main__":
    print('Plik uruchomiony bezpośrednio')
    main()
else:
    print('Plik zaimportowano jako moduł')

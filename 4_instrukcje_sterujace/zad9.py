#Stwórz listę przedmiotów, które zabierzesz na bezludną wyspę.
# Wyświetl nazwę właśnie spakowanego przedmiotu, dla po ostatnim przedmiocie
# pokaż informację: “Great, we are ready!”

list_of_things = []

things_count = int(input("ile przedmiotów chcesz zabrać?:"))

for i in range(things_count):
    thing = input("wpisz, co chciałbyś zabrać ze sobą na wycieczkę:")
    list_of_things.append(thing)


for i in list_of_things:
    print(''.join(i))
print("Great, we are ready!")


#Utwórz 2 krotki.
# Następnie utwórz listę będącą połączeniem elementów o parzystym indeksie z pierwszej krotki,
# oraz nieparzystych elementów z drugiej.

my_tuple_1 = (1, 2, 3, 4)
my_tuple_2 = (5, 6, 7, 8)

x = my_tuple_1[0::2]
y = my_tuple_2[1::2]

lista = list(x) + list(y)
print(lista)
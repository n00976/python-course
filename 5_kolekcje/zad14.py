#W wierszu policz wystąpienie każdego wyrazu, zignoruj wielkość liter.
#"""Szybko, zbudź się, szybko, wstawaj
#Szybko, szybko, stygnie kawa
#Szybko, zęby myj i ręce"""

#Zadbaj o sposób wyświetlania np.:
#szybko : 5
#zbudź : 1

wiersz = "Szybko, zbudź się, szybko, wstawaj, Szybko, szybko, stygnie kawa, Szybko, zęby myj i ręce"
wiersz = wiersz.lower()
wiersz = wiersz.replace(",", " ")
wiersz = wiersz.split()

dict ={}
for i in wiersz:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

for k, v in dict.items():
    print(k, '\t', v)

print(dict)


#Utwórz listę, która zawiera składniki na ulubione danie. Wyświetl komunikaty co należy pokolei dodać.
# Poza pętlą umieść pozostałe instrukcje np. “Wrzuć do pierkanika”, “Podawaj schłodzone”.

ingredients = ['olive oil', 'courgette', 'basil', 'almonds', 'salt', 'pepper', '3 cloves of garlic', 'parmesan cheese']

print('prepare a pan')
print('chop a courgette')
for i in ingredients[:2]:
    print('add ' + i)
print('fry until courgette is soft')

for i in ingredients[2:]:
    print('add ' + i)

print('pound everything in mortar')
print('add mixture to the courgette-spaghetti and enjoy!')





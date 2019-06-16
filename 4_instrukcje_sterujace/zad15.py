# Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem
# (np.jako jeden string rozdzielonych przecinkiem lub białym znakiem).
# Następnie powitaj każdą osobę na liście.

osoby = input("Wprowadź listę osób (Imiona powinny być oddzielone przecinkiem):")
osoby = osoby.split(",")

for i in osoby:
    print("Hello", i)
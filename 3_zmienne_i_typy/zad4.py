#Stwórz zmienną przechowującą wyraz o długości nieparzystej większej niż 7
# i zwróć łańcuch złożony z trzech środkowych znaków danego ciągu.

txt = input("Podaj słowo o nieparzystej i większej niż 7 ilości liter :")
sr_index = len(txt)//2
print(sr_index)
txt2 = txt[sr_index -1] + txt[sr_index] + txt[sr_index + 1]
print(txt2)

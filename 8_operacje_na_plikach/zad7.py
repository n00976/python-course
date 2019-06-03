#Wisielec. Utwórz plik zawierający listę słów wg. kategorii
# np. zwierzęta, owoce etc. Poproś użytkownika o podanie kategorii
# przed rozpoczęciemy gry. Następny wczytaj listę haseł do programu,
# wylosuj jedno hasło z listy. Rozgrywka powinna być maksymalnie intuicyjna.

import random


#word = list(input())
def hangman():
    underlines = ["_"] * len(word)

    while underlines != word:
        letter = input("choose a letter:")[0]
        for i in range(len(word)):
            if letter == word[i]:
                underlines[i] = word[i]
        print(" ".join(underlines))

    print("Gratulacje, udało Ci się!")

category = input("choose category: animals/fruits/vegetables:")

if category == "animals":
    with open ('hangman_animals.txt', 'r' )as fopen:
        lines = fopen.readlines()
        word = list(random.choice(lines))
        hangman()
elif category == "fruits":
    with open('hangman_fruits.txt', 'r')as fopen:
        lines = fopen.readlines()
        word = list(random.choice(lines))
        hangman()
elif category == "vegetables":
    with open('hangman_veg.txt', 'r')as fopen:
        lines = fopen.readlines()
        word = list(random.choice(lines))
        hangman()

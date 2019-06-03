import random

print("Zagramy w papier, kamień nożyce.")


menu = {
    "start": "s",
    "poziom trudności": "p",
    "zamknij": "x"
}

poziom_trudnosci = {
    "łatwy": "e",
    "trudny": "h"
}

user_choice_easy = {
    "kamień": "k",
    "papier": "p",
    "nożyce": "n"
}

user_choice_hard = {
    "kamień": "k",
    "papier": "p",
    "nożyce": "n",
    "jaszczurka": "j",
    "Spock": "s"
}
figury_easy = ["k", "p", "n"]
figury_hard = ["k", "p", "n", "j", "s"]

statystyka = []
#statystyka = []


def win():
    print("Wybrałeś " + fig + " ,a wybór przeciwnika to " + computer_choice + ". Wygrałeś!")
    statystyka.append("win")

def lose():
    print("Wybrałeś " + fig + " ,a wybór przeciwnika to " + computer_choice + ". Przegrałeś!")
    statystyka.append("lose")

def easy():
    while(True):
        for k, v in user_choice_easy.items():
            print(k, ' : ', v)
        fig = input("Wybierz figurę:")
        computer_choice = random.choice(figury_easy)
        if fig == computer_choice:
            print("Wybrałeś " + str(fig) + " , a wybór przeciwnika to " + str(computer_choice) + ". Remis!")
        elif fig == "k" and computer_choice == "n":
            win()
        elif fig == "p" and computer_choice == "k":
            win()
        elif fig == "n" and computer_choice == "p":
            win()
        elif fig == "k" and computer_choice == "p":
            lose()
        elif fig == "p" and computer_choice == "n":
            lose()
        elif fig == "n" and computer_choice == "k":
            lose()
        continue_game = input("Czy chcesz kontynuować grę? tak/nie:")
        if continue_game == "nie":
            print(statystyka)
            break
        else:
            continue



def hard():
    while(True):
        for k, v in user_choice_hard.items():
            print(k, ' : ', v)

        fig = input("Wybierz figurę:")
        computer_choice = random.choice(figury_hard)

        if fig == computer_choice:
            print("Wybrałeś " + str(fig) + " , a wybór przeciwnika to " + computer_choice + ". Remis!")
        elif fig == "k" and computer_choice == "n":
            print("Wybrałeś kamień , a wybór przeciwnika to nożyce. Wygrywasz!")
        elif fig == "p" and computer_choice == "k":
            print("Wybrałeś papier, a wybór przeciwnika to kamień. Wygrywasz!")
        elif fig == "n" and computer_choice == "p":
            print("Wybrałeś nożyce, a wybór przeciwnika to papier. Wygrywasz!")
        elif fig == "k" and computer_choice == "j":
            print("Wybrałeś kamień, a przeciwnik wybrał jaszczurkę. Wygrywasz!")
        elif fig == "j" and computer_choice == "s":
            print("Wybrałeś jaszczurkę, a przeciwnik wybrał Spocka. Wygrywasz!")
        elif fig == "j" and computer_choice == "p":
            print("Wybrałeś jaszczurkę, a przeciwnik wybrał papier. Wygrywasz!")
        elif fig == "s" and computer_choice == "n":
            print("Wybrałeś Spocka, a przeciwnik wybrał nożyce. Wygrywasz!")
        elif fig == "s" and computer_choice == "k":
            print("Wybrałeś Spocka, a przeciwnik wybrał kamień. Wygrywasz!")
        elif fig == "p" and computer_choice == "s":
            print("Wybrałeś papier, a przeciwnik wybrał Spocka. Wygrywasz!")
        elif fig == "n" and computer_choice == "j":
            print("Wybrałeś nożyce, a przeciwnik wybrał jaszczurkę. Wygrywasz!")
        elif fig == "k" and computer_choice == "p":
            print("Wybrałeś kamień, a wybór przeciwnika to papier. Przegrałeś!")
        elif fig == "p" and computer_choice == "n":
            print("Wybrałeś papier, a wybór przeciwnika to nożyce. Przegrałeś!")
        elif fig == "n" and computer_choice == "k":
            print("Wybrałeś nożyce, a wybór przeciwnika to kamień. Przegrałeś!")
        elif fig == "j" and computer_choice == "k":
            print("Wybrałeś jaszczurkę, a przeciwnik wybrał kamień. Przegrałeś!")
        elif fig == "s" and computer_choice == "j":
            print("Wybrałeś Spocka, a przeciwnik wybrał jaszczurkę. Przegrałeś!")
        elif fig == "p" and computer_choice == "j":
            print("Wybrałeś papier, a przeciwnik wybrał jaszczurkę. Przegrałeś!")
        elif fig == "n" and computer_choice == "s":
            print("Wybrałeś nożyce, a przeciwnik wybrał Spocka. Przegrałeś!")
        elif fig == "k" and computer_choice == "s":
            print("Wybrałeś kamień, a przeciwnik wybrał Spocka. Przegrałeś!")
        elif fig == "s" and computer_choice == "p":
            print("Wybrałeś Spocka, a przeciwnik wybrał papier. Przegrałeś!")
        elif fig == "j" and computer_choice == "n":
            print("Wybrałeś jaszczurkę, a przeciwnik wybrał nożyce. Przegrałeś!")
        continue_game = input("Czy chcesz kontynuować grę? tak/nie:")
        if continue_game == "nie":
            break
        else:
            continue


while(True):
    for k, v in menu.items():
        print(k, " : ", v)
    menu_choice = input("wybierz:")
    if menu_choice == "s":
        easy()
    elif menu_choice == "p":
        for k, v in poziom_trudnosci.items():
            print(k, " : ", v)
        trudnosc_choice = input("wybierz poziom trudnosci:")
        if trudnosc_choice == "e":
            easy()
        elif trudnosc_choice == "h":
            hard()
    elif menu_choice == "x":
        print("koniec")
        break

    #Wyświetla liczbę i procent wygranych użytkownika
    #Wyświetl najdłuższą sekwencję wygranych dla użytkownika i komputera.
    #Możesz dodać własne dane, które chcesz zbierać na potrzeby statystyczne. Skorzystaj z właściwości list:

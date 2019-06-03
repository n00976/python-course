#Wyświetl tylko 5 pierwszych linii

with open ('cytaty.txt', 'r' )as fopen:
    lines = fopen.readlines()
    for i in lines[:5]:
        print("*" * 100)
        print(i.center(100))




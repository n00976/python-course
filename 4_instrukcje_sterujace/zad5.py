#Stwórz zmienną password.
# Hasło powinno składać z liter i cyfr,
# zwierać conajmniej 1 dużą literę
# i mieć długość conajmniej 8 znaków.

password = input("podaj hasło:")

dlugosc = len(password)
#print(dlugosc)
litery_i_cyfry = not password.isalpha()
#print(litery_i_cyfry)
same_cyfry = not password.isdigit()
#print(same_cyfry)
alfa_num = password.isalnum()
#print(alfa_num)
alnum_ok = alfa_num and same_cyfry and litery_i_cyfry
print(alnum_ok)
duza_litera = not password.islower() and not password.isupper()

if dlugosc < 8:
    print("Hasło jest za krótkie")
elif alnum_ok == False:
    print("Hasło powinno posiadać litery i cyfry")
elif duza_litera == True:
    print("Hasło jest ok")
#litery_i_cyfry == True:
   # print("Hasło nie zawiera cyfr")
#elif same_cyfry == True
   # print("Hasło nie zawiera liter")



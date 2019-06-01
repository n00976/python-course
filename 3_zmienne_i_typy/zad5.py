#Stwórz dwie zmienne s1 i s2 przechowujące dowolne wyrazy,
# utwórz nowy łańcuch s3, dołączając s2 w środku s1.

s1 = "niebieski"
s2 = "dinozaur"
x = len(s1)//2
print(x)
s3 = s1[:x] + s2 + s1[x:]
print(s3)
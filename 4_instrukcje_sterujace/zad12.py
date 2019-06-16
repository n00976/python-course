#Napisz program, który wyświetli kolejne wyniki dla silnii liczby naturalnej n.

number = int(input("dla jakiej liczby chcesz obliczyć silnię?"))

factorial = 1

if number in (0, 1):
    factorial = 1
else:
    for i in range(2, number + 1):
        factorial = factorial * i

print(factorial)


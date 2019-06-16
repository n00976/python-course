#Stwórz moduł, który dla dowolnej wartości n, zwróci ciąg fibonnaciego.



def fibonacci_element(n):
    if n < 1:
        fibonacci = 0
    elif n < 2:
        fibonacci = 1
    else:
        fibonacci = fibonacci_element(n - 1) + fibonacci_element(n - 2)
    return fibonacci

def fibonacci_sequence(n):
    for i in range(n):
        print(fibonacci_element(n - 1))
        n = n - 1

def main():
    n = int(input("number for Fibonacci sequence:"))
    fibonacci_sequence(n)



if __name__=='__main__':
    main()


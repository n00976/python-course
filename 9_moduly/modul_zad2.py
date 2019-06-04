import math

def calculate_delta(a, b, c):
    delta = b**2 - (4 * a * c)

    if delta == 0:
        x0 = (-1 * b) / (2 * a)
        print("równanie ma 1 podwójny pierwiastek: " + str(x0))

    elif delta > 0:
        x1 = ((-1 * b) - math.sqrt(delta)) / (2 * a)
        x2 = ((-1 * b) + math.sqrt(delta)) / (2 * a)
        print("równanie ma 2 pierwiastki: " + str(x1) + " i " + str(x2))

    elif delta < 0:
        print("Delta < 0, brak rozwiązań")


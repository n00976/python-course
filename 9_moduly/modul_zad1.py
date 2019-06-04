import random

def advice(advice_file):
    with open(advice_file, 'r') as fopen:
        porady = fopen.readlines()
        print(random.choice(porady))

def bmi(waga, wzrost):

    bmi = round(waga/(wzrost**2), 2)
    print("Twoje BMI to: " + str(bmi))
    if bmi < 18.5:
        advice("bmi_niedowaga.txt")

    elif 18.5 <= bmi <24.99:
        advice("bmi_nadwaga.txt")

    elif bmi >= 25:
        advice("bmi_wagaok.txt")

    return bmi



movie = input("Tytuł filmu:")
grade = float(input("Ocena kostiumów w skali 1-10:"))
grade1 = float(input("Ocena scenografii w skali 1-10:"))
grade2 = float(input("Ocena aktorów pierwszoplanowych w skali 1-10:"))
grade3 = float(input("Ocena aktorów drugoplanowych w skali 1-10:"))
gradeall =(grade + grade1 + grade2 + grade3)/4
print("Film pt." + movie + " oceniasz na " +str(gradeall))


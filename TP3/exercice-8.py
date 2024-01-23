a = float(input("Saisir un nombre:"))
b= float(input("Saisir un nombre:"))

if a == 0 and b == 0:
    print("l’ensemble des solutions est l’ensemble R")
elif a == 0 and b != 0:
    print(" l’ensemble des solutions est l’ensemble vide")
elif a != 0:
    print(f" la solution est (-b / a) : {-b/a}")
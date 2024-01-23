from random import randint

nombre = randint(1,6)
nb_magic = nombre
i = ""

while i != nb_magic:
    chiffre = int(input("Saisir un chiffre : "))
    if chiffre > nb_magic:
        print("Trop grand")
    elif chiffre < nb_magic:
        print("Trop petit")
    else:
        print("Gagné")
        break


    

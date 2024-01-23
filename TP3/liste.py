#Ecrire un algorithme permettant de trier une liste d'entier (saisies au clavier) dans l'ordre croissant.
nbr_chaine = int(input("Saisir le nombre de chiffre que vous voulez classer en tout : "))
list = []
for i in range(0,nbr_chaine):
    nombre = int(input("Saisir un nombre entier :"))
    if nombre >= 0:
        list.append(nombre)
list_croissant = sorted(list)
print(list)
print(list_croissant)
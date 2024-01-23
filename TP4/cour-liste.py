# ecrire un programme qui permet de générer un tableau d'entiers de 1 a n (saisie au clavier)

nombre = int(input("Saisir un nombre d'entier pour la liste : "))
list = []
cpt = 0

for i in range(0,nombre):
    cpt = i+1
    list.append(cpt)
print(list)
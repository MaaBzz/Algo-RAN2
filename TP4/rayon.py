nb_rayon = int(input("Saisir le nombre de rayon : "))
list_rayon = []
list_produit = []
for i in range(nb_rayon):
    nom_rayon = input("Saisir le nom du rayon :")
    list_rayon.append(nom_rayon)
    nb_produit = int(input("Saisir le nombre de produit par rayon : "))
    for j in range(nb_produit):
        nom_produit = input(f"saisir le nom du produit du rayon {list_rayon[i]}: ")
        list_produit.append(nom_produit)
        
print(list_rayon)
print(list_produit)
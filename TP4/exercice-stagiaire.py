
# Representation d'un stagiaire
# NOM
# Prénom
# Promo
# stagiaire_A = ["DOE","John","RAN-2"]
# stagiaire_B = ["BATROSSE","Hal","RAN-2"]

# liste_stagiaires = [
#     stagiaire_A,
#     stagiaire_B
# ]

# print(liste_stagiaires)

# for stagiaire in liste_stagiaires:
#     for prop in stagiaire:
#         print(prop, end=" ")
#     print()
   

# -----------------------------------------------------------------------------------

# À partir du code précédent, faire sorte de demander la saisie de 15 stagiaires à l'utilisateur qui seront stockés dans une liste.
# Chaque stagiaire est lui  même représenté par une liste (NOM, Prénom, Promo)

list_stagiaire = [

]

for i in range(0,15):
    stagiaire = []
    Nom = input("Saisir le nom du stagiaire : ")
    Prenom = input("Saisir le prénom du stagiaire : ")
    Promo = input("Saisir la promo du stagiaire : ")
    stagiaire += [Nom, Prenom, Promo]
    list_stagiaire += [stagiaire]

print(list_stagiaire)

for stagiaire in list_stagiaire:
    for prop in stagiaire:
        print(prop, end=" - ")
    print()
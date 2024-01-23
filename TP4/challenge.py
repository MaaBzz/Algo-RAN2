# Ecrire un programme qui intègre les fonctionnalités suivantes :
    # demander le nombre de matières à saisir
    # stocker le nom des matières
    # demander le nombre d'élève à ajouter et stocker leur nom et prénom
    # pour chaque élève saisir la note par matière
    # afficher tous les élèves avec leur moyenne générales et leurs notes par matières
    # afficher la moyenne de la classe par matière
    # donner le nom du meilleur élève
    # donner le nom du pire élève

grand = []
matiere = int(input("Saisir le nombre de matière : "))

for i in range(0,matiere):
    nom = []
    nom_matiere = input("Saisir le nom de la matière :")
    nom.append(nom_matiere)
 
nb_eleve = int(input("Saisir le nombre d'élèves :"))
for i in range(0,nb_eleve):
    nom_eleve = []
    note = []
    eleve = input("Saisir le nom et prénom de l'élève :")
    nom_eleve.append(eleve)
    grand += [nom_eleve]
    for j in range(0,matiere):
        note_eleve = float(input(f"Saisir les notes  de {nom_eleve[j]} : "))
        note.append(note_eleve)
    somme = 0
    for b in note:
        somme = somme + b
    nom_eleve += [note]
    moy = somme / matiere
    nom_eleve += [moy]

# for i in grand:
#     print(i)
# #jusque la c est bon
# moy_matiere = 0
# for i in (0,nb_eleve):
#     moy_matiere = note[0] + note[0]
#     print(nom)
#comment on reprend les matieres en boule ????
#
for i in range(nb_eleve):
    print(f"=== bulletin de {nom_eleve[i]} ===")
    for j in range(matiere):
        print(f"note de {nom[j]} : {round(note[i][j],2)}/20")
    print(f"Moyenne générale : {round(moy[i],2)}/20")

# afficher la moyenne de la classe par matière
for i in range(matiere):
    somme_note_matiere = 0
    for j in range(nb_eleve):
        somme_note_matiere += note[j][i]
    print(f"Moyenne de la classe pour {nom[i]} : {somme_note_matiere/nb_eleve}")

# donner le nom du meilleur élève
# donner le nom du pire élève
moyenne_max = 0
indice_meilleur_eleve = 0
moyenne_min = 20
indice_pire_eleve = 0
for i in range(nb_eleve):
    if moy[i] > moyenne_max:
        moyenne_max = moy[i]
        indice_meilleur_eleve = i 
    if moy[i] < moyenne_min:
        moyenne_min = moy[i]
        indice_meilleur_eleve = i
print(f"Le meilleur élève est {nom_eleve[indice_meilleur_eleve]} avec une moyenne de {moyenne_max}/20")
print(f"Le pire élève est {nom_eleve[indice_pire_eleve]} avec une moyenne de {moyenne_min}/20")
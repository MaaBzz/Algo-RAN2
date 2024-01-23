#Ecrire un programme permettant de compter le nombre de fois qu'une lettre est présente dans un texte.
#Le programme doit alors demander le texte et la lettre à rechercher.

#Vous devez ensuite afficher le nombre de fois que la lettre est présente dans le texte.

phrase = input("Veuillez saisir une phrase :")
letter = input("Veuillez saisir une lettre :")
cpt = 0

for i in phrase:
    if i == letter:
        cpt = cpt + 1
print(f"il y a {cpt} {letter} dans {phrase}")

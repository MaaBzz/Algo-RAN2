#Faire un programme permettant de trouver la lettre qui est la plus présente dans un texte et afficher le nombre de fois.
text = input("Saisir un texte :").lower()

lettre = 0
lettre_max = 0
lettre_fin = "" #stockage lettre
deja_vue = []

for i in range(0,len(text)):
    if text[i] not in deja_vue:
        for x in range(0,len(text)):
            if text[i] == text[x] and text[i] != "": #compare le texte pour compter les lettres
                lettre = lettre + 1
        if lettre > lettre_max:
            lettre_max = lettre #chiffre mais pas de lettre 
            lettre_fin = text[i]
        lettre = 0 #reinitialiser le compteur a la fin de la première boucle

        deja_vue = deja_vue + [text[i]]
print(f"la lettre la plus récurrente est {lettre_fin}")
francais = float(input("veuillez saisir la note de Français /20: "))
coef_fr = int(input("Saisir le coefficient de Français : "))
math = float(input("veuillez saisir la note de Math /20: "))
coef_math = int(input("Saisir le coefficient de Math : "))
geometrie = float(input("veuillez saisir la note de Géométrie /20: "))
coef_geo = int(input("Saisir le coefficient de Géométrie : "))
informatique = float(input("veuillez saisir la note d'informatique /20: "))
coef_info = int(input("Saisir le coefficient d'informatique : "))

moy = ((francais * coef_fr)+(math * coef_math)+(geometrie * coef_geo)+(informatique * coef_info)) / (coef_fr + coef_math + coef_geo + coef_info)

if (francais >= 0 and francais <= 20) and (math >= 0 and math <= 20) and (geometrie >= 0 and geometrie <= 20) and (informatique >= 0 and informatique <= 20) and (coef_fr >= 0 and coef_fr <= 10) and (coef_math >= 0 and coef_math <= 10) and (coef_geo >= 0 and coef_geo <= 10) and (coef_info >= 0 and coef_info <= 10):
    if moy >= 16 and moy <20:
        print("Très bien")
    elif moy >= 12 and moy <16:
        print("Bien")
    elif moy >= 8 and moy <12:
        print("Assez bien")
    elif moy >= 4 and moy <8:
        print("Insuffisant")
    elif moy >= 0 and moy <4:
        print("Nul")
else:
    print("Vous vous êtes trompé dans la saisie des données")
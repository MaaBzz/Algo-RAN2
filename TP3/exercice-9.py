francais = float(input("veuillez saisir la note de Français /20:"))
math = float(input("veuillez saisir la note de Math /20:"))
geometrie = float(input("veuillez saisir la note de Géométrie /20:"))
informatique = float(input("veuillez saisir la note d'informatique /20:"))

moy = (francais+math+geometrie+informatique) / 4
if moy >= 16 and moy <=20:
    print("Très bien")
elif moy >= 12 and moy <16:
    print("Bien")
elif moy >= 8 and moy <12:
    print("Assez bien")
elif moy >= 4 and moy <8:
    print("Insuffisant")
elif moy >= 0 and moy <4:
    print("Nul")
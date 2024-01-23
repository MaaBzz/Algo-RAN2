cpt_haut = 0


for i in range(0,20):
    cpt = 0
    nombre = float(input("Veuillez saisir un nombre : "))
    if nombre > cpt:
        cpt = nombre
    for j in range(0,20):
        if cpt > cpt_haut:
            cpt_haut = cpt
print(f"Le chiffre le plus grand de votre liste est : {cpt_haut}")
Prix_Ht = float(input("veuillez saisir un nombre:"))
TVA = 20

Calcul_TVA = (Prix_Ht / 100) * TVA
Prix_TTC = Prix_Ht + Calcul_TVA
print("Le prix TTC est de", Prix_TTC,"€")
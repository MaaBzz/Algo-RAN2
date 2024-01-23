ht = float(input("Saisir le prix:"))
quantité = int(input("Saisir la quantité:"))
tva = float(input("Saisir la TVA:"))

montant_ht = ht * quantité
prix_remise = montant_ht * 0.85
calcul_TVA = (prix_remise / 100) * tva
Prix_TTC = calcul_TVA + prix_remise
print("Le prix TTC est de", Prix_TTC,"€")
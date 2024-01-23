ttc = float(input("Saisir le prix:"))
if ttc >=500 and ttc <=1000 :
    print(f"Le taux de remise est de 2%, le prix remisé est de {ttc*0.98}")
elif ttc >1000 and ttc <=2000:
    print(f"Le taux de remise est de 5%, le prix remisé est de {ttc*0.95}")
elif ttc >2000:
    print(f"Le taux de remise est de 10%, le prix remisé est de {ttc*0.90}")

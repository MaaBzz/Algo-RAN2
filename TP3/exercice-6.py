ht = float(input("Saisir le prix:"))
print("Pour une TVA de 5,5%, saisissez 1")
print("Pour une TVA de 19,6%, saisissez 2")
print("Pour une TVA de 33%, saisissez 3")

code = int(input("Saissisez votre code"))
if code == 1:
    print(f"Le prix HT est de {ht} €, la TVA est de 5,5% et le prix TTC est de {ht*1.055} €.")
elif code == 2:
    print(f"Le prix HT est de {ht} €, la TVA est de 19,6% et le prix TTC est de {ht*1.196} €.")
else:
    print(f"Le prix HT est de {ht} €, la TVA est de 33% et le prix TTC est de {ht*1.33} €.")

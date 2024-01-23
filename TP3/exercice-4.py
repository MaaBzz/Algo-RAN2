nbr_a = int(input("Saisir le nombre de doigts:"))
nbr_b = int(input("Saisir le nombre de doigts:"))

somme = nbr_a + nbr_b
if somme%2==0:
    print("A a gagner")
else:
    print("B a gagner")
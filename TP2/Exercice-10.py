multiplication = int(input("veuillez saisir un nombre:"))
print("la table de multiplication de", multiplication,"est")
for i in range (1, 11):
    print(i, "x", multiplication, "=", multiplication * i)
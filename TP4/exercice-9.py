dimension = int(input("De quelle taille doit etre la tige ?: "))
nb = int(input("Saisir le nombre de tige voulu : "))
verticale = "|"
horizontal = "_"

print(f"{horizontal * nb}  ")
for i in range(0,dimension):
    print(f"{verticale * nb}  ")
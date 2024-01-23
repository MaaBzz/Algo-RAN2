mot = input("Veuillez saisir un mot :")

for i in range(0, len(mot)):
        if mot[i] != mot[len(mot)-1-i]:
                print("nop")
        else:
                print("yes")

#Deuxieme méthode parcourir le mot dans les deux sens

cpt = 0
for i in range(0,len(mot)):
        print(f"{i} -> {mot[i]}")
        if mot[i] == mot[len(mot)-1-i]:
                print(f"{mot[i]} = {mot[len(mot) - 1 - i]}")
                cpt = cpt + 1
        else:
                print(f"{mot[i]} != {mot[len(mot) - 1 - i]}")

if cpt == len(mot):
        print("C'est un palindrome")
else:
        print("Ce n'est pas un palindrome.")

#3 eme méthode

word = input("Saisir un mot : ")

# On essai d'inverser le mot
drow = ""
for letter in word:
    drow = letter + drow

if word == drow:
    print("C'est un palindrome")
else:
    print("Ce n'est pas un palindrome")
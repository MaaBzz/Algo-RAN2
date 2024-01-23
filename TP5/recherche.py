# Recherche :
# Créer une fonction qui permet de retourner la position d'un élément dans un tableau. La fonction doit prendre en paramètre l'élément à rechercher et le tableau concerné.

list = ["a","b","c","d","e"]
def index(elem,table):
    return table.index(elem)
print(index("e",list))

# Inverse :
# Créer une fonction qui permet d'inverser un tableau.

# Exemple : [1,2,3,4] => [4,3,2,1]
def inverse(table):
    return table[::-1]
print(inverse(list))

# Tri :
# Créer une fonction qui permet de trier un tableau dans l'ordre croissant

# Exemple : [8,5,2,7] => [2,5,7,8]
list_numero = [8,5,2,7]
def croissant(table):
    for i in range(0,len(table)):
        petit = i
        for j in range(i+1,len(table)):
            if table[j] < table[petit]:
                petit = j
        table[i],table[petit] = table[petit], table[i]
    return table
print(croissant(list_numero))


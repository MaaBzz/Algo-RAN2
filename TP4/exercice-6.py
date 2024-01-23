nombre = int(input("Saisir un nombre : "))
list_bin = ""

while nombre > 0:
    quotient = nombre  // 2
    list_bin = str(nombre - quotient * 2) + list_bin
    nombre = quotient

print(list_bin)
cpt_depart = int(input("Saisir un nombre de départ : "))
cpt_fin = int(input("Saisir un nombre de fin : "))
pas = int(input("Saisir un pas d'incrément : "))
cpt = 0
list = []

for i in range(0,cpt_fin):
        cpt = cpt_depart + (i*pas)
        list.append(cpt)
print(list)
#print(f"les valeurs comprisent entre {cpt_depart} et {cpt_fin} sont : {cpt}")
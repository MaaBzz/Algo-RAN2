date = input("Veuillez saisir une anné : AAAA/MM/JJ : ")
date = date.replace("/","")
list_date = []
list_date.append(date)

A=int(date[0]+date[1]+date[2]+date[3])
M=int(date[4]+date[5])
J=int(date[6]+date[7])

if (M==1 or M==2):
    A= A - 1
    M= M + 12

N = J + int((13 * M + 3) / 5) + int(5 * A / 4) - int(A / 100) + int(A / 400)
N = N % 7

if (M == 1):
    mois="Janvier"
elif(M == 2):
    mois="fevrier"
elif(M == 3):
    mois="Mars"
elif(M == 4):
    mois="Avril"
elif(M == 5):
    mois="Mais"
elif(M == 6):
    mois="Juin"
elif(M == 7):
    mois="Juillet"
elif(M == 8):
    mois="Aout"
elif(M == 9):
    mois="Septembre"
elif(M == 10):
    mois="Octobre"
elif(M == 11):
    mois="Novembre"
elif(M == 12):
    mois="Decembre"

if N % 7 == 0:
    print(f"Le {J} {mois} {A} est un lundi.")
elif N % 7 == 1:
    print(f"Le {J} {mois} {A} est un mardi")
elif N % 7 == 2:
    print(f"Le {J} {mois} {A} est un mercredi")
elif N % 7 == 3:
    print(f"Le {J} {mois} {A} est un jeudi")
elif N % 7 == 4:
    print(f"Le {J} {mois} {A} est un vendredi")
elif N % 7 == 5:
    print(f"Le {J} {mois} {A} est un samedi")
elif N % 7 ==6:
    print(f"Le {J} {mois} {A} est un dimanche")
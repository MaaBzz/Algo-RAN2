from datetime import datetime
annee_actuel = datetime.now().year

birth_year = int(input("Saisir l'année de naissance du bébé:"))
age = annee_actuel - birth_year
if age <= 3:
    print("l'enfant a le droit a une palette de petits pots")
else:
    print("l'enfant n'a pas le droit a une palette de petits pots")

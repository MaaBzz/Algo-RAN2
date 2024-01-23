# Double
def double(number):
    return number * 2
print(double(5))

# Carre
def carre(number):
    return number * number
print(carre(5))

# Périmétre rectanlge
def perimetre(large,long):
    return (large + long) * 2
print(perimetre(4,2))

# Périmétre d'un cercle
def cercle(rayon):
    return rayon * 2 * 3.14
print(cercle(2.8))

# Prix TTC
def ttc(prix,tva):
    return  (prix * (tva/100)) + prix
print(ttc(100,20))

# Hello
def hello(prenom):
    return "hello" + prenom
print(hello(" loic"))

# table de multiplication
def table(multiplication):
    for i in range(1,10):
        print(i , " x ", multiplication, " = ",i*multiplication)
print(table(9))
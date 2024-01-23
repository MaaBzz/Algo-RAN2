# def somme(a,b):
#     return a + b
# res = somme(5,4)

# def somme(a,b):
#     print(a+b)
# somme(5,4)

# Ecrire une fonction permettant de vérifier si un nombre et pair

def is_even(number):
    if number%2:
        return False
    else:
        return True
res = is_even(4)
print(res)

# correction
# number % 2 est la condition de dessus
# not bool pour inverser le booléen
def is_even(number):
    return not bool(number % 2)
print(is_even(4))
# Alain et Catherine organisent une soirée pour des membres de leur club informatique.
# Ils décident que pour être invité il faut :

# - être ami d’Alain et de Catherine ;
# - ou ne pas être ami d’Alain, mais être ami de Catherine ;
# - ou ne pas être ami de Catherine, mais jouer au bridge.

# Pour un membre quelconque, on définit les variables booléennes suivantes par :
# a = 1 s’il est un ami d’Alain,
# b = 1 s’il joue au bridge,
# c = 1 s’il est un ami de Catherine.



a = int(input("Etes vous amis d'alain ? si OUI saisir 1, si NON saisir 0 :"))
b = int(input("Vous jouez au bridge ? si OUI saisir 1, si NON saisir 0 :"))
c = int(input("Etes vous amis de catherine ? si OUI saisir 1, si NON saisir 0 :"))

if a == 1 and c == 1 or b == 1:
    print("Vous êtes invité")
else:
    print("Vous n'êtes pas invité")

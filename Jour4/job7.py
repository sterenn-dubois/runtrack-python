# Définition de la liste L
L = [8, 24, 48, 2, 16]

# Comptage des multiples de 3 dans la liste L
nb_multiples_de_3 = 0
for element in L:
    if element % 3 == 0:
        nb_multiples_de_3 += 1

# Affichage du résultat
print("Le nombre de multiples de 3 dans la liste L est :", nb_multiples_de_3)
# Définition de la liste L
L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

# Initialisation de la somme à 0
somme_paires = 0

# Parcours de la liste L
for element in L:
    # Vérification si l'élément est pair
    if element % 2 == 0:
        # Ajout de l'élément à la somme
        somme_paires += element

# Affichage du résultat
print("La somme de toutes les valeurs paires de la liste L est :", somme_paires)
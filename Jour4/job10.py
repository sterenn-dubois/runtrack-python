# Définition de la liste L
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

# Initialisation de la variable produit à 1
produit = 1

# Parcours de la liste L
for i in range(len(L)):
    # Vérification si la valeur actuelle de la liste est dans l'intervalle [25, 90]
    if L[i] >= 25 and L[i] <= 90:
        # Multiplie la valeur actuelle avec la variable produit
        produit *= L[i]

# Affichage du résultat
print("Le produit de toutes les valeurs de la liste comprises dans l'intervalle [25, 90] est :", produit)
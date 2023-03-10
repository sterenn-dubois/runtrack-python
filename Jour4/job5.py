# Création de la liste L
L = [1, 2, 3, 4, 5]

# Affichage de la valeur de L[1]
print("La valeur de L[1] est :", L[1])

# Définition de la fonction pour remplacer L[3] par la somme des cases voisines L[2] et L[4]
def replace_L3_with_sum_of_L2_and_L4():
    L[3] = L[2] + L[4]

# Appel de la fonction pour remplacer L[3] par la somme des cases voisines L[2] et L[4]
replace_L3_with_sum_of_L2_and_L4()

# Affichage de la valeur du dernier terme de la liste
print("La valeur du dernier terme de la liste est :", L[-1])
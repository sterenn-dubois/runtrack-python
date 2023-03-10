# Définition de la liste L
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

# Initialisation des variables max et min avec la première valeur de la liste
max = L[0]
min = L[0]

# Parcours de la liste L à partir de la deuxième valeur
for i in range(1, len(L)):
    # Vérification si la valeur actuelle est plus grande que la valeur maximale
    if L[i] > max:
        max = L[i]
    # Vérification si la valeur actuelle est plus petite que la valeur minimale
    if L[i] < min:
        min = L[i]

# Affichage des résultats
print("Le maximum de la liste est :", max)
print("Le minimum de la liste est :", min)
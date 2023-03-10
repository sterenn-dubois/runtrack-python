def my_long_word(n, chaine):
    mots = chaine.split()  # diviser la chaine en mots
    longs_mots = [mot for mot in mots if len(mot) > n]  # filtrer les mots de longueur > n
    return " ".join(longs_mots)  # retourner les mots concaténés avec un espace entre eux

# exemple d'utilisation
chaine = "La peur est le chemin vers le côté obscur la peur mène à la colère la colère mène à la haine la haine mène à la souffrance"
longs_mots = my_long_word(3, chaine)
print(longs_mots)
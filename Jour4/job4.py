def add_mango_to_fruits():
    fruits = ["pomme", "cerise", "orange, Melon"]
    fruits.insert(2, "Mangue")
    return fruits

ma_liste_de_fruits = add_mango_to_fruits()
print(ma_liste_de_fruits)
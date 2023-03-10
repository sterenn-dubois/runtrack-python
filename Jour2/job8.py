def afficher_aliments(type_aliment, saison):
    if type_aliment == "fruits" and saison == "hiver":
        print("Orange, mandarine et kiwi")
    elif type_aliment == "fruits" and saison == "ete":
        print("Poire, fraise, cassis")
    elif type_aliment == "legume" and saison == "hiver":
        print("Carotte, topinambour, endive")
    elif type_aliment == "legume" and saison == "ete":
        print("Artichaut, aubergine, navet")
    else:
        print("Aucune suggestion disponible")

afficher_aliments("fruits", "hiver")
afficher_aliments("fruits", "ete")
afficher_aliments("legume", "hiver")
afficher_aliments("legume", "ete")
afficher_aliments("viande", "printemps")
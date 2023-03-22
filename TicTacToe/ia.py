def ia(board, signe):
    """
    Retourne l'emplacement où l'IA souhaite jouer (0-8) en utilisant l'algorithme de minimax.
    """
    joueur = 1 if signe == "X" else 2
    adversaire = 2 if signe == "X" else 1

    def evaluer_etat(etat):
        """
        Évalue l'état du plateau de jeu et retourne un score correspondant à la qualité du
        plateau pour le joueur actuel.
        """
        if etat["gagnant"] == joueur:
            return 1
        elif etat["gagnant"] == adversaire:
            return -1
        else:
            return 0

    def minimax(etat, joueur_actuel):
        """
        Implémente l'algorithme minimax pour trouver le meilleur coup à jouer.
        """
        if etat["gagnant"] is not None:
            return evaluer_etat(etat)

        if joueur_actuel == joueur:
            meilleur_score = float("-inf")
            for coup in etat["coups_possibles"]:
                etat_suivant = etat.copy()
                etat_suivant["plateau"][coup] = joueur
                etat_suivant["coups_possibles"].remove(coup)
                score = minimax(etat_suivant, adversaire)
                if score > meilleur_score:
                    meilleur_score = score
                    meilleur_coup = coup
            return meilleur_score if meilleur_score != float("-inf") else 0
        else:
            meilleur_score = float("inf")
            for coup in etat["coups_possibles"]:
                etat_suivant = etat.copy()
                etat_suivant["plateau"][coup] = adversaire
                etat_suivant["coups_possibles"].remove(coup)
                score = minimax(etat_suivant, joueur)
                if score < meilleur_score:
                    meilleur_score = score
                    meilleur_coup = coup
            return meilleur_score if meilleur_score != float("inf") else 0

    etat_initial = {"plateau": board.copy(), "coups_possibles": [i for i, x in enumerate(board) if x == 0], "gagnant": None}
    score_max = float("-inf")
    meilleur_coup = None
    for coup in etat_initial["coups_possibles"]:
        etat_suivant = etat_initial.copy()
        etat_suivant["plateau"][coup] = joueur
        etat_suivant["coups_possibles"].remove(coup)
        score = minimax(etat_suivant, adversaire)
        if score > score_max:
            score_max = score
            meilleur_coup = coup

    return meilleur_coup if meilleur_coup is not None else False

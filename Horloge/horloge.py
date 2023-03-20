import time

# Fonction pour afficher l'heure
def afficher_heure(heure):
    print("{:02d}:{:02d}:{:02d}".format(heure[0], heure[1], heure[2]))

# Fonction pour régler l'heure
def regler_heure():
    heures = int(input("Entrez les heures : "))
    minutes = int(input("Entrez les minutes : "))
    secondes = int(input("Entrez les secondes : "))
    return (heures, minutes, secondes)

# Fonction pour régler l'alarme
def regler_alarme():
    heures = int(input("Entrez les heures de l'alarme : "))
    minutes = int(input("Entrez les minutes de l'alarme : "))
    secondes = int(input("Entrez les secondes de l'alarme : "))
    return (heures, minutes, secondes)

# Récupération de l'heure actuelle
heure_actuelle = time.localtime()
heure = (heure_actuelle.tm_hour, heure_actuelle.tm_min, heure_actuelle.tm_sec)

# Affichage de l'heure toutes les secondes
while True:
    afficher_heure(heure)
    time.sleep(1)
    heure = (heure[0], heure[1], heure[2]+1)

    # Vérification si l'heure correspond à l'heure de l'alarme
    alarme = regler_alarme()
    if heure == alarme:
        print("L'alarme a été déclenchée !")
    
    # Régler l'heure
    reponse = input("Voulez-vous régler l'heure ? (O/N) ")
    if reponse.upper() == "O":
        heure = regler_heure()
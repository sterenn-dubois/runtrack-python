def verifier_signe(nombre):
    if nombre > 0:
        print("positif")
    elif nombre < 0:
        print("negatif")
    else:
        print("nul")

verifier_signe(5)
verifier_signe(-3)
verifier_signe(0)
verifier_signe(10.5)
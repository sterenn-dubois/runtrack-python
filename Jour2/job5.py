def calcule(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "Impossible de diviser par zéro"
    elif operator == '%':
        try:
            return num1 % num2
        except ZeroDivisionError:
            return "Impossible de diviser par zéro"
    else:
        return "Opérateur invalide"

resultat = calcule(10, '+', 5)
print(resultat)

resultat = calcule(10, '/', 0)
print(resultat) 
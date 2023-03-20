import re
def password_is_valid(password):
    if len(password) < 8:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[!@#$%^&*]", password):
        return False
    return True

password_valid = False
while not password_valid:
    password = input("Choisissez un mot de passe : ")
    if password_is_valid(password):
        print("Votre mot de passe est valide.")
        password_valid = True
    else:
        print("Le mot de passe doit contenir au moins 8 caractères, au moins une lettre majuscule, au moins une lettre minuscule, au moins un chiffre, et au moins un caractère spécial (!, @, #, $, %, ^, &, *). Veuillez réessayer.")

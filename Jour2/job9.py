def determiner_triangle(a, b, c):
    # Vérifier si les longueurs peuvent former un triangle
    if a + b > c and b + c > a and c + a > b:
        # Vérifier le type de triangle
        if a == b == c:
            print("Le triangle est équilatéral.")
        elif a == b or b == c or c == a:
            if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
                print("Le triangle est isocèle et rectangle.")
            else:
                print("Le triangle est isocèle.")
        elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
            print("Le triangle est rectangle.")
        else:
            print("Le triangle est quelconque.")
    else:
        print("Ces longueurs ne peuvent pas former un triangle.")

determiner_triangle(5, 5, 5)
determiner_triangle(3, 4, 5)
determiner_triangle(2, 2, 3)
determiner_triangle(1, 2, 3)
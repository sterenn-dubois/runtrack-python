def round_grades(grades):
    rounded_grades = []
    for grade in grades:
        if grade < 40:
            rounded_grades.append(grade)
        else:
            next_multiple_of_5 = 5 * round(grade / 5)
            if next_multiple_of_5 - grade < 3:
                rounded_grades.append(next_multiple_of_5)
            else:
                rounded_grades.append(grade)
    return rounded_grades

grades = [72, 65, 89, 78, 82, 60, 49]
rounded_grades = round_grades(grades)
print(rounded_grades)
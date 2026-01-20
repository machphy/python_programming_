def unique_grades(student_grades):
    all_grades = set()
    for grades in student_grades.values():
        all_grades.update(grades)
    return all_grades


grades_dict = {"John": [85, 90], "Jane": [78, 85], "Doe": [78, 92]}
print(unique_grades(grades_dict))

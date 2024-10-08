def map_students_to_scores(student_list):
    return {name: score for name, score in student_list}


students = [("John", 85), ("Jane", 90), ("Doe", 78)]
print(map_students_to_scores(students))

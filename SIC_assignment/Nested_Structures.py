def map_students_to_scores(student_list):
    return {name: score for name, score in student_list}


students = [("bhoot", 21), ("rohan", 35), ("Chandan", 22)]
print(map_students_to_scores(students))

def print_sorted_students(scores_dict):
    sorted_students = sorted(scores_dict.items(), key=lambda x: x[1], reverse=True)
    for name, score in sorted_students:
        print(f"{name} scored {score} marks!")

student_scores = {"Raj": 85, "Priya": 90, "Amit": 78, "Neha": 92}
print_sorted_students(student_scores)

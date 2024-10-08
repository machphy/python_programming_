def print_sorted_students(scores_dict):
    sorted_students = sorted(scores_dict.items(), key=lambda x: x[1], reverse=True)
    for name, score in sorted_students:
        print(f"Student: {name}, Score: {score}")

student_scores = {"John": 85, "Jane": 90, "Doe": 78, "Alice": 92}
print_sorted_students(student_scores)

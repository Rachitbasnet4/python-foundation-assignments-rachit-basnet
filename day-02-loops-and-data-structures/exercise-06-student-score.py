'''
Exercise 6: Student Score Dictionary
Name: Rachit Basnet
Day 2
'''

# input student score Dictionary
student_scores = {
    "Anisha": 78,
    "Ravi": 55,
    "Maya": 92,
    "Sagar": 61,
    "Nima": 48
}

# printing all student name and score
for student, score in student_scores.items():
    print(f"{student}:{score}")

# creating dictionary of student who scored at least 60
student_60 = {
    student:score
    for student, score in student_scores.items()
    if score >= 60
}

# highest scoring student with student score
highest_student = max(student_scores, key=student_scores.get)
highest_score = student_scores[highest_student]

# calculating the average score
avg_score = sum(student_scores.values()) / len(student_scores)

# output
print(f"Student with score above 60: {student_60}")
print(f"Highest scoring student: {highest_student}({highest_score})")
print(f"Average score: {avg_score}")

# Student Grading System

def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"

def generate_student_report(name, score):
    grade = calculate_grade(score)
    return f"{name} has scored {score} and received grade {grade}"

# Test the grading system
students = [
    ("Aman", 80),
    ("Sarah", 95),
    ("John", 55),
    ("Lisa", 72),
    ("Mike", 35)
]

# Generate reports for all students
print("Student Reports:")
for student_name, student_score in students:
    report = generate_student_report(student_name, student_score)
    print(report)
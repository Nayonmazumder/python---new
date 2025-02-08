# Problem: Assign a letter grade based on a student's
# score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

score = int(input("Please Enter the Score: "))


def grade_cal(score):
    if score > 100:
        return '"Please Check Your score and try again: "'
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


print(f"Your grade is {grade_cal(score)}")

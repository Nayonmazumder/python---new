# 1. Age Group Categorization
# Classify a person's age group: Child (< 13), Teenager (13-19),
# Adult (20-59), Senior (60+).

age = int(input("Please Specify Age Value: "))


def group_cal(age):
    if age < 13:
        return "Child"
    elif age < 20:
        return "Teenager"
    elif age < 60:
        return "Adult"
    else:
        return "Senior"


print(f"Your Inputed Age Group is : {group_cal(age)}")

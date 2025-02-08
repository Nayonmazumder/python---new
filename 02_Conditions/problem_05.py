# 5. Weather Activity Suggestion
# Problem: Suggest an activity based on the weather
# (e.g., Sunny - Go for a walk,
#  Rainy - Read a book, Snowy - Build a snowman).

weather = input("What is the weather : ")
weather = weather.capitalize()


def activity(*args):
    if weather == "Sunny":
        return "Go for a walk"
    elif weather == "Rainy":
        return "Read a Book!"
    elif weather == "Snowy":
        return "Build a snowman!!"
    else:
        return "Enjoy the day !!!"


print(f"Tody is {weather}. You can {activity(weather)}")

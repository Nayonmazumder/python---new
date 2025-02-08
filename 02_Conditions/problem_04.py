# 4. Fruit Ripeness Checker
# Problem: Determine if a fruit is ripe, overripe, or
# unripe based on its color.
# (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

def fruit_ripness(*args):
    if fruit == "BANANA" and color == "GREEN":
        return "Unripe"
    elif fruit == "BANANA" and color == "YELLOW":
        return "Ripe"
    else:
        return "Overripe"


fruit = input("Please Enter Your Frout name : ")
color = input("Please Secify its Color : ")
fruit = fruit.upper()
color = color.upper()
print(
    f"Your fruit is : {fruit} and it is : {fruit_ripness(fruit,color)}")

# 6. Transportation Mode Selection
# Problem: Choose a mode of transportation based on the distance
# (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

distance = int(input("Please Specify the distance: "))


def mode_sel(*args):
    if distance < 3:
        return "Walk"
    elif distance < 15:
        return "Bike"
    else:
        return "Car"


print(f"You should go to the {distance} km by {mode_sel(distance)}")

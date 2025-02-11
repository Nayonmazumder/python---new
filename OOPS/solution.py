class Car:                 # Class and Object Exmaple
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def FullName(self):
        return f"Full Details : {self.__brand} {self.model}"

    def get_brand(self):                    # Encapsulation!
        return f"{self.__brand} is your Brand !"


class ElectricCar(Car):  # Inheritances Example
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


my_New_car = ElectricCar("Telsa", "Model S", "85 kWh")
print(my_New_car.get_brand())
print(my_New_car.FullName())
print(my_New_car.battery_size)

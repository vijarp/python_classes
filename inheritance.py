"""Class Inheritance
Create a subclass called ElectricCar that inherits from the Car class. The ElectricCar class should have an additional attribute called battery_size (in kWh).

Task:
Define the ElectricCar class that inherits from the Car class.
Initialize the battery_size attribute in the ElectricCar class.
Override the car_info method to include the battery size in the string. The format should be:
"Car: [make] [model], Year: [year], Battery Size: [battery_size] kWh"

Create an instance of the ElectricCar class and call the car_info method."""
from simple_class import Car

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        # Initialize the parent class attributes
        super().__init__(make, model, year)
        # Initialize the ElectricCar-specific attribute
        self.battery_size = battery_size

    def car_info(self):
        return f"Car: {self.make} {self.model}, Year: {self.year}, Battery Size: {self.battery_size} kWh"

# Creating an instance of ElectricCar and calling car_info
electric_car = ElectricCar('Tesla', 'Model S', 2022, 100)
print(electric_car.car_info())

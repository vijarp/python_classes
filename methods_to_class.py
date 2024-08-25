"""Adding Methods to a Class
Extend the Car class to include the following methods:

start_engine: A method that prints "The engine of the [make] [model] is now running."
stop_engine: A method that prints "The engine of the [make] [model] has been turned off."
Task:
Add the start_engine and stop_engine methods to the Car class.
Create an instance of the Car class.
Call both methods (start_engine and stop_engine) and print the results.

Previous Class was 

class Car
make: The make of the car (e.g., "Toyota").
model: The model of the car (e.g., "Corolla").
year: The year the car was manufactured (e.g., 2020).


"""
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"The engine of the {self.make} {self.model} is now running.")

    def stop_engine(self):
        print(f"The engine of the {self.make} {self.model} has been turned off.")

    def car_info(self):
        return f"Car: {self.make} {self.model}, Year: {self.year}"

# Creating an instance and calling the methods
car = Car('Honda', 'Civic', 2015)
car.start_engine()
car.stop_engine()

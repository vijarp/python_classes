"""Creating a Simple Class
Create a Python class called Car that has the following attributes:

make: The make of the car (e.g., "Toyota").
model: The model of the car (e.g., "Corolla").
year: The year the car was manufactured (e.g., 2020).


The class should also have a method called car_info that returns a string in the format:


"Car: [make] [model], Year: [year]"

Task:
Define the Car class with the above attributes.
Create an instance of the Car class.
Call the car_info method and print the result."""


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def car_info(self):
        return f"Car: {self.make} {self.model}, Year: {self.year}"
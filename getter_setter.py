"""Encapsulation and Getters/Setters
Modify the Car class to make the year attribute private. Add a method to get the value of year and another method to set the value of year, ensuring that it can only be set to a value greater than or equal to 1886 (the year the first car was invented).

Task:
Modify the Car class to make year a private attribute.
Add a getter method called get_year to retrieve the year.
Add a setter method called set_year to set the year, with validation to ensure it’s greater than or equal to 1886.
Create an instance of the Car class and test setting and getting the year.
"""

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.__year = year  # Initialize the private year attribute

    def get_year(self):
        return self.__year

    def set_year(self, year):
        if year >= 1886:  # Ensure the year is valid
            self.__year = year
        else:
            print("Invalid year. Please enter a year greater than or equal to 1886.")

# Creating an instance and testing the getter and setter
car = Car('Ford', 'Mustang', 1967)
print(car.get_year())  # Should print 1967

car.set_year(1988)
print(car.get_year())  # Should print 1988

car.set_year(1800)  # Should print an error message

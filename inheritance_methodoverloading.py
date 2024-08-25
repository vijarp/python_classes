"""Class Inheritance with Method Overriding
Create a base class Shape with a method area that returns None (this will be a placeholder method). Then create two subclasses:

Rectangle with attributes width and height. Override the area method to return the area of the rectangle.
Circle with an attribute radius. Override the area method to return the area of the circle.
Task:
Define the Shape class with the placeholder area method.
Define the Rectangle class that inherits from Shape and implements the area method.
Define the Circle class that inherits from Shape and implements the area method.
Create instances of Rectangle and Circle, and print their areas.
Here is a format you can follow for the area methods:

For Rectangle: width * height
For Circle: 3.14159 * radius * radius (use 3.14159 as an approximation for π)
"""


import math

class Shape:
    def area(self):
        pass  # Placeholder method

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

# Creating instances and printing areas
rectangle = Rectangle(10, 5)
print(f"Rectangle area: {rectangle.area()}")  # Should print 50

circle = Circle(7)
print(f"Circle area: {circle.area()}")  # Should print approximately 153.94

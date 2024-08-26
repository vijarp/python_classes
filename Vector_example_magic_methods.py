"""Create a class Vector that represents a 2D vector. The class should include the following:

Initialization: The class should initialize with two attributes, x and y, representing the vector components.

Magic Methods:

Implement the __add__ method to add two Vector objects using the + operator.
Implement the __sub__ method to subtract one Vector object from another using the - operator.
Implement the __mul__ method to perform a dot product of two Vector objects using the * operator.
Implement the __repr__ method to return a string representation of the vector in the form Vector(x, y).
Bonus: Implement the __len__ method to return the magnitude (length) of the vector, calculated as the square root of the sum of the squares of x and y.
"""

import math  # Import the math module for square root calculation

class Vector: 
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y  # Dot product

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __len__(self):
        return int(math.sqrt(self.x**2 + self.y**2))

# Example usage
v1 = Vector(3, 4)
v2 = Vector(1, 2)

v3 = v1 + v2  # Vector(4, 6)
v4 = v1 - v2  # Vector(2, 2)
dot_product = v1 * v2  # 11 (3*1 + 4*2)
magnitude = len(v1)  # 5 (sqrt(3^2 + 4^2))

print(v3)  # Output: Vector(4, 6)
print(v4)  # Output: Vector(2, 2)
print(dot_product)  # Output: 11
print(magnitude)  # Output: 5

"""Composition and Nested Classes
Create a class Person that contains a nested class Address. The Address class should have the following attributes:

street
city
postal_code
The Person class should have the following attributes:

name
age
address (an instance of the Address class)
Task:
Define the Address nested class within the Person class.
Initialize the Address attributes within Person through an Address instance.
Add a method person_info in the Person class that returns a string with the person’s name, age, and address details

Create an instance of Person, set the address, and call the person_info method to display the result.
"""

class Person:
    class Address:
        def __init__(self, street, city, postal_code):
            self.street = street
            self.city = city
            self.postal_code = postal_code

    def __init__(self, name, age, street, city, postal_code):
        self.name = name
        self.age = age
        self.address = self.Address(street, city, postal_code)

    def person_info(self):
        return f"Name: {self.name}, Age: {self.age}, Address: {self.address.street}, {self.address.city}, {self.address.postal_code}"

# Creating an instance of Person and calling person_info
p = Person('C', 32, 'TT', 'NY', '222333')
print(p.person_info())

# Object-Oriented Programming (OOP) in Python is a powerful way to structure code by modeling 
# real-world entities as objects. It helps make your programs more modular, reusable, and easier to maintain


# Class --->
# A blueprint for creating objects.
# Defines attributes (data) and methods (functions).

# Object--->
# An instance of a class.
# Has its own data and can use the class’s methods.

# self parameter-->
# it is used inside class methods to refer to the current instance of the class
# a is for Raj
# b is for nikita

class Person:
    name = "Tiding"
    occupation = "Software Developer"
    networth = 100

    def info(self):
        print(f"{self.name} is a {self.occupation}")


a = Person() #object -- instance of Person class
a.name = "Raj"
a.occupation = "Software Tester"
print(a.name, a.occupation)
a.info()

b = Person()
b.name = "Nikita"
b.occupation = "HR"
print(b.name, b.occupation)
b.info()

c = Person()
print(c.name, c.occupation) # it will take default values
c.info()

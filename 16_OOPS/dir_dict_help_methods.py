# dir() 
# - Discover Attributes and Methods
# - Purpose: Lists all valid attributes and methods of an object

x = [1,2,3]
print(dir(x))
print(x.__add__)

y = (1,2,3)
print(dir(y))
print(y.__add__)


# dict() — Create a Dictionary
# Purpose: Constructs a dictionary object

class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age
        self.version = 1

p = Person("John",30)
print(p.__dict__)


# help() — Get Documentation
# Purpose: Displays documentation for modules, classes, functions, or keywords

print(help(Person))
# Instance Variable

# Defined inside methods, typically in __init__() using self
# Unique to each object (instance) of the class
# Used to store data specific to that object

class Car:
    def __init__(self, color):
        self.color = color  # instance variable

car1 = Car("red")
car2 = Car("blue")

print(car1.color)  # red
print(car2.color)  # blue



# Class Variable

# Defined directly inside the class, but outside any methods
# Shared across all instances of the class
# Used for properties common to all objects


class Car1:
    wheels = 4  # class variable

    def __init__(self, color):
        self.color = color  # instance variable

car1 = Car1("red")
car2 = Car1("blue")

print(car1.wheels)  # 4
print(car2.wheels)  # 4

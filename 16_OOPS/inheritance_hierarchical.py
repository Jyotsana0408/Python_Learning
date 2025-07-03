# Hierarchical Inheritance
# Definition: One base class is inherited by multiple child classes. Each child gets the same base functionality but can add its own.


class Animal:
    def sound(self):
        print("Animals make sounds")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

# Usage
d = Dog()
c = Cat()
d.sound()  # Dog barks
c.sound()  # Cat meows

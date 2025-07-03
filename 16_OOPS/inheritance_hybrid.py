# Hybrid Inheritance
# Definition: A combination of two or more types of inheritance (e.g., multiple + multilevel + hierarchical).
# It’s used to model complex relationships.

class Vehicle:
    def move(self):
        print("Vehicle moves")

class Car(Vehicle):
    def drive(self):
        print("Car drives")

class Boat(Vehicle):
    def sail(self):
        print("Boat sails")

class Amphibious(Car, Boat):
    def action(self):
        print("Can drive and sail")

# Usage
a = Amphibious()
a.move()    # From Vehicle
a.drive()   # From Car
a.sail()    # From Boat
a.action()  # Own method

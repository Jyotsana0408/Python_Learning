# Single inheritance -->
# simplest form of inheritance where a child class inherits from one parent class. 
# It allows the child class to reuse the methods and attributes of the parent, promoting cleaner and more maintainable code.


class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def welcome(self):
        print("Welcome from Child")

# Usage
c = Child()
c.greet()    # Inherited from Parent
c.welcome()  # Defined in Child


# Real world example

class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Employee: {self.name}")

class Manager(Employee):
    def show(self):
        super().show()
        print("Role: Manager")

m = Manager("Jyotsna")
m.show()


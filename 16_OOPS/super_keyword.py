# super keyword -->
# used to give access to methods and properties of a parent class from within a child class.
# useful when a class inherits from multiple parent classes and you want to call a method from one of the parent classes.

# Creates a proxy object Lets you call methods from a parent class without naming it directly.
# Used to call parent’s methods Most often __init__() but also useful for other methods.
# Supports code reuse Avoids rewriting shared logic in child classes.
# Works with multiple inheritance Python uses MRO (Method Resolution Order) to decide which method gets called.
# Cleaner and maintainable Keeps your code modular and avoids hardcoding class names.


class ParentClass:

    def parent_method(self):
        print("This is the parent method.")
    

class ChildClass(ParentClass):
    def parent_method(self):
        print("Harry")
        super().parent_method()

    def child_method(self):
        print("This is the child method.")
        super().parent_method()


child_object = ChildClass()
child_object.child_method()
child_object.parent_method()


class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)  # Calls Person's constructor
        self.employee_id = employee_id

# Usage
e = Employee("Jyotsna", "E123")
print(e.name)         # Output: Jyotsna
print(e.employee_id)  # Output: E123

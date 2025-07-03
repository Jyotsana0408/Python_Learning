# Inheritance -->
# lets you reuse and extend existing code by creating new classes based on existing ones
# Child inherits all methods and attributes from Parent
# You can override or extend them as needed

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of employee: {self.id} is {self.name}")


class Programmer(Employee):
    def showLanguage(self):
        print(f"The default language is Python")

e1 = Employee("Rohan", 400)
e1.showDetails()

e2 = Employee("Neha", 321)
e2.showDetails()
# e2.showLanguage() --> it will throw an error (Attribute Error)

e3 = Programmer("Raj",234)
e3.showDetails()
e3.showLanguage() #it will not throw an error (due to Inheritance)
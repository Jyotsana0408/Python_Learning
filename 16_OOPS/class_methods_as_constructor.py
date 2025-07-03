# class methods -->
# can act as alternative constructors—meaning they provide different ways to create and initialize objects beyond
# the standard __init__() method. This is especially useful when you want to create objects from formatted data like strings,
# dictionaries, or external sources.


# Create objects from non-standard formats (e.g. strings, JSON, CSV)
# Add custom logic before object creation
# Improve readability and modularity


class Employee:
    def __init__(self,name, salary):
        self.name = name 
        self.salary = salary

    @classmethod
    def fromString(cls,str):
        return cls(str.split("-")[0], int(str.split("-")[1]))


e1 = Employee("Harry", 30000)
print(e1.name)
print(e1.salary)

# no code readability
# str = "Raj-40000"
# e2 = Employee(str.split("-")[0], str.split("-")[1])
# print(e2.name)
# print(e2.salary)

str = "Raj-40000"
e2 = Employee.fromString(str)
print(e2.name)
print(e2.salary)


#  class methods are methods that are bound to the class rather than its instances.
#  They’re useful when you want to work with class-level data or create factory methods that return instances in a controlled way.

# Decorated with @classmethod
# First parameter is cls, which refers to the class itself
# Can access or modify class variables, but not instance variables

class Employee:
    company = "Apple"
    def show(self):
        print(f"The name of {self.name} and company is {self.company}")

    # def changeCompany(cls, newCompany): # acting as instance not class, cls is woring as instance
    #     cls.company = newCompany

    @classmethod
    def changeCompany(cls, newCompany): # acting as instance not class, cls is woring as instance
        cls.company = newCompany



e1 = Employee()
e1.name = "Harry"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Employee.company)

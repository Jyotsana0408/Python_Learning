# constructor -->
# it is a special method used to initialize objects when a class is instantiated


class Person:
    # name = "Vijay"
    # occ = "Data Analyst"

    def __init__(self): # Default constructor
        print("You are inside contructor") #--> this methos will run every when object is created
  
    def info(self):
        print(f"{self.name} is a {self.occ}")


a = Person()
a.name = "Divya"
a.occ = "HR"
a.info()

b = Person()
b.name = "Kirti"
b.occ = "Manager"
b.info()



# The __init__() Method --->

# The constructor method in Python is named __init__
# It runs automatically when you create an object from a class
# The first parameter is always self, which refers to the current object
# it will always return None

class Person2:

    def __init__(self,n,o): #Parametrized constructor -- self is first arguments, so total arguments are 3 here
        print("You are inside contructor") #--> this methos will run every when object is created
        self.name = n # n is local variable for this function
        self.occ = o

    def info(self):
        print(f"{self.name} is a {self.occ}")


a = Person2("Samay","Data Analyst")
a.info()
b = Person2("Neha", "Sales Manager")
b.info()
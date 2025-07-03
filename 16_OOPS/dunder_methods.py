# dunder methods ---> (short for double underscore methods, like __init__, __str__, etc.)
# special methods that let you customize how your objects behave with built-in operations. 
# They're also called magic methods or special methods

# They start and end with double underscores: __method__
# Python calls them automatically in response to certain actions
# You don’t call them directly—they’re triggered behind the scenes


# Why Use Dunder Methods -->

# Make your classes behave like built-in types
# Enable operator overloading
# Improve readability and debugging
# Support Pythonic idioms like iteration, comparison, and context management


class Employee:
    def __init__(self, name):
        self.name = name 

    def __len__(self):
        i = 0
        for c in self.name:
            i = i +1
        return i
    


e1 = Employee("Aditya")
print(e1.name)
print(len(e1)) 


#  Custom __str__ method 

# __init__ is the constructor — sets up initial values.
# __str__ returns a readable string representation of the object.
# Without __str__, print(b) would show something like <__main__.Book object at 0x...>.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"

# Usage
b = Book("Python Basics", "Jyotsna")
print(b)  # Output: 'Python Basics' by Jyotsna


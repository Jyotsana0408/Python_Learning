# Multilevel inheritance -->
# class inherits from a class that already inherits from another class—creating a chain of inheritance like Grandparent → Parent → Child.
# Each level passes down its attributes and methods to the next.


class Grandparent:
    def show_grandparent(self):
        print("I am the grandparent")

class Parent(Grandparent):
    def show_parent(self):
        print("I am the parent")

class Child(Parent):
    def show_child(self):
        print("I am the child")

# Usage
c = Child()
c.show_grandparent()  # Inherited from Grandparent
c.show_parent()       # Inherited from Parent
c.show_child()        # Defined in Child



# Real-World Analogy

# Person as the base class
# Student extending Person
# Graduate extending Student

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course

    def show_student(self):
        print(f"Student ID: {self.student_id}, Course: {self.course}")


class Graduate(Student):
    def __init__(self, name, age, student_id, course, graduation_year):
        super().__init__(name, age, student_id, course)
        self.graduation_year = graduation_year

    def show_graduate(self):
        print(f"Graduation Year: {self.graduation_year}")


g = Graduate("Jyotsna", 25, "ST101", "Python OOP", 2025)

g.show_person()     # From Person
g.show_student()    # From Student
g.show_graduate()   # From Graduate


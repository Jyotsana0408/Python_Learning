# Access specifiers (also called access modifiers) -->
# control how class members (attributes and methods) can be accessed from outside the class


# Public Access-->
# Default in Python — no underscore prefix
# Accessible from anywhere: inside or outside the class

class Student:
    def __init__(self):
        self.name = "Jyotsna"  # public

s = Student()
print(s.name)  # Accessible


# Protected Access -->
# Prefix with a single underscore _var
# Suggests internal use or subclass access
# Still accessible from outside (not enforced)

class Student:
    def __init__(self):
        self._roll = 123  # protected

s = Student()
print(s._roll)  # Accessible, but discouraged


# Private Access -->
# Prefix with double underscore __var
# Triggers name mangling: Python renames it internally to _ClassName__var
# Not directly accessible from outside

# Name mangling -->
# a mechanism that helps protect class attributes from being accidentally accessed or overridden, 
# especially in inheritance scenarios

class Student:
    def __init__(self):
        self.__branch = "CS"  # private

s = Student()
# print(s.__branch)  # AttributeError
print(s._Student__branch)  # Access via name mangling

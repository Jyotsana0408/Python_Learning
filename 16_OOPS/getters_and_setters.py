# Encapsulation means--->
# Hiding internal state of an object
# Interacting only through methods
# Controlling access to attributes using access modifiers

#  getters and setters ---> 
# methods used to access and modify private attributes of a class while maintaining control and encapsulation

# Getters -->
# used to access the values of an object's properties (show that method is a property) 

# @property -->(act like a getter if we write a @property on method)
# Turns a methos into read-only attribute
# built-in way to make methods behave like attributes, while still allowing you to add logic behind the scenes.
# It’s a clean and Pythonic way to implement getters and setters without changing how the attribute is accessed.

class MyClass:
    def __init__(self, value):
        self._value = value
    
    def show(self):
        print(f"Value is {self._value}")
    
    @property 
    def value(self):
        return self._value
    
    @property
    def ten_value(self):
        return 10 * self._value
    
    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value/10
    

obj = MyClass(10)
print(obj._value)
print(obj.ten_value)
obj.show()
# obj.ten_value = 67 --> throw error without setter
obj.ten_value = 67
obj.show()
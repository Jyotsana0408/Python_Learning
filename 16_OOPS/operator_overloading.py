# Python uses special methods (aka dunder methods) like __add__, __eq__, __lt__, etc.
# These methods are automatically called when you use operators like +, ==, <, etc.
# You can redefine them to make your objects behave like built-in types.


class Vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k 

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self,x):
        return Vector(self.i + x.i , self.j + x.j , self.k + x.k)

v1 = Vector(3,5,6)
print(v1)

v2 = Vector(1,4,7)
print(v2)

print(v1 + v2)
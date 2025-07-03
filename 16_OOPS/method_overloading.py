# method overloading -->
# having multiple methods with the same name but different parameters

class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y
    

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        super().__init__(radius, radius)

    def area(self):
        return 3.14 * super().area()

rectangle = Shape(3,4)
print(rectangle.area())

c = Circle(3)
print(c.area())
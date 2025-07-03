# Static mehod -->

# It’s decorated with @staticmethod
# It doesn’t take self or cls as its first parameter
# It can be called using either the class name or an instance
# Use static methods when the logic relates to the class but doesn’t need object data.

class Math:
    def __init__(self,num):
        self.num = num

    def addToNum(self, n):
        self.num = self.num + n

    @staticmethod
    def add(a,b):
        return a+b

# result = Math.add(1,2)
# print(result)

a = Math(5)
print(a.num)
a.addToNum(7)
print(a.num)
print(Math.add(4,3))


# Multiple inheritance --> 
# a class can inherit from more than one parent class, allowing it to combine features from multiple sources. 
# It’s powerful—but can get tricky if not used carefully.


# Car inherits from both Engine and Radio
# No method name conflicts, so everything works smoothly

class Engine:
    def start(self):
        print("Engine started")

class Radio:
    def play_music(self):
        print("Playing music")

class Car(Engine, Radio):
    def drive(self):
        print("Car is driving")

# Usage
c = Car()
c.start()        # From Engine
c.play_music()   # From Radio
c.drive()        # From Car


# Diamond Problem & MRO -->
# If multiple parent classes share a method name, Python uses Method Resolution Order (MRO) to decide which one to call.


# D inherits from both B and C, which both inherit from A
# Python uses Method Resolution Order (MRO) to resolve conflicts
# Since B is listed before C, D.show() calls B.show()


class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):
    pass

d = D()
d.show()  # Output: Class B
print(D.__mro__)  # Shows method resolution order


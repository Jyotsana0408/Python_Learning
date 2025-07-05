class Car:

    def __init__(self,brand,milege):
        self.brand = brand
        self.milege = milege

    def showDetails(self):
        print(f"Brand of car is {self.brand} and milege is {self.milege}")


car = Car("Toyota",70)
car.showDetails()
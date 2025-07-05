class Vehicle:

    def __init__(self, brand, model, fuel_type, color, max_speed):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type
        self.color = color
        self.max_speed = max_speed

    def display_details(self):
        print(f"Vehicle Details:")
        print(f"Brand       : {self.brand}")
        print(f"Model       : {self.model}")
        print(f"Fuel Type   : {self.fuel_type}")
        print(f"Color       : {self.color}")
        print(f"Max Speed   : {self.max_speed} km/h")



class Bike(Vehicle):
    def __init__(self, brand, model, fuel_type, color, max_speed, has_gear, helmet_included):
        super().__init__(brand, model, fuel_type, color, max_speed)
        self.has_gear = has_gear
        self.helmet_included = helmet_included

    def display_details(self):
        super().display_details()
        print("Bike Specifics:")
        print(f"Gear System : {'Yes' if self.has_gear else 'No'}")
        print(f"Helmet      : {'Included' if self.helmet_included else 'Not Included'}")


b = Bike("Honda", "Shine", "Petrol", "Red", 95, True, True)
b.display_details()


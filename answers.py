#ASSIGNMENT ONE
#Create class representing a smartphone
class Smartphone:
    def __init__(self, brand, model, battery_life, os):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life  # In percentage
        self.os = os

    def show_specs(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Battery Life: {self.battery_life}%")
        print(f"Operating System: {self.os}")

    def make_call(self, number):
        print(f"Calling {number}...")

    def charge(self, charge_percent):
        self.battery_life += charge_percent
        if self.battery_life > 100:
            self.battery_life = 100
        print(f"Phone charged! Battery life is now {self.battery_life}%")

# Example of creating an object
my_phone = Smartphone("Apple", "iPhone 13", 85, "iOS")
my_phone.show_specs()
my_phone.make_call("123-456-7890")
my_phone.charge(15)

#Polymorphism challenge
#we will define different types of vehicles (Car and Plane and Boat) with a method called move(), but each class will have a different implementation of move().
class Vehicle:
    def move(self):
        pass  

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Example of polymorphism
def vehicle_action(vehicle):
    vehicle.move()

# Creating objects
car = Car()
plane = Plane()
boat = Boat()

# Calling the move method on different objects
vehicle_action(car)    # Output: Driving 🚗
vehicle_action(plane)  # Output: Flying ✈️
vehicle_action(boat)   # Output: Sailing 🚤

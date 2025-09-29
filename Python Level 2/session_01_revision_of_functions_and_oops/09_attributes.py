# Attributes = Variables inside classes (instance or class attributes).

class Car:
    wheels = 4  # class attribute (same for all cars)

    def __init__(self, brand, color):
        self.brand = brand   # instance attribute
        self.color = color

# Create objects
car1 = Car("Tesla", "Red")
car2 = Car("BMW", "Black")

print(car1.brand, car1.color, car1.wheels)  # Tesla Red 4
print(car2.brand, car2.color, car2.wheels)  # BMW Black 4

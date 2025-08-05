# Define a class
class Car:
    # Constructor (called when object is created)
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    # Method to display car information
    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")

# Create objects (instances of the class)
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Tesla", "Model 3", 2023)

# Call method on objects
car1.display_info()   # Output: 2020 Toyota Corolla
car2.display_info()   # Output: 2023 Tesla Model 3

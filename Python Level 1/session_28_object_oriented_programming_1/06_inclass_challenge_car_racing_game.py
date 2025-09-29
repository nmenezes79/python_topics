# Creating a Car class using OOP
class Car:
    def __init__(self, brand, color, weight, height, length):
        self.brand = brand
        self.color = color
        self.weight = weight
        self.height = height
        self.length = length
        self.speed = 0
        self.headlights_on = False
        self.engine_started = False

    def start(self):
        if not self.engine_started:
            self.engine_started = True
            print(f"{self.brand} engine started.")
        else:
            print(f"{self.brand} engine is already running.")

    def stop(self):
        if self.engine_started:
            self.speed = 0
            self.engine_started = False
            print(f"{self.brand} has stopped.")
        else:
            print(f"{self.brand} is already stopped.")

    def increase_speed(self, increment):
        if self.engine_started:
            self.speed += increment
            print(f"{self.brand} speed increased to {self.speed} km/h.")
        else:
            print(f"Start the engine of {self.brand} first.")

    def decrease_speed(self, decrement):
        if self.engine_started:
            self.speed = max(0, self.speed - decrement)
            print(f"{self.brand} speed decreased to {self.speed} km/h.")
        else:
            print(f"Start the engine of {self.brand} first.")

    def turn_on_headlights(self):
        if not self.headlights_on:
            self.headlights_on = True
            print(f"{self.brand} headlights turned ON.")
        else:
            print(f"{self.brand} headlights are already ON.")

    def turn_off_headlights(self):
        if self.headlights_on:
            self.headlights_on = False
            print(f"{self.brand} headlights turned OFF.")
        else:
            print(f"{self.brand} headlights are already OFF.")

# Creating different car objects
car1 = Car("Ferrari", "Red", 1500, 1.2, 4.5)
car2 = Car("Lamborghini", "Yellow", 1600, 1.1, 4.6)
car3 = Car("Tesla", "White", 1800, 1.4, 4.7)

# Using methods on car1
car1.start()
car1.increase_speed(50)
car1.turn_on_headlights()
car1.decrease_speed(20)
car1.turn_off_headlights()
car1.stop()

print("\n---\n")

# Using methods on car2
car2.start()
car2.increase_speed(70)
car2.stop()

print("\n---\n")

# Using methods on car3
car3.start()
car3.turn_on_headlights()
car3.increase_speed(100)
car3.decrease_speed(30)
car3.stop()

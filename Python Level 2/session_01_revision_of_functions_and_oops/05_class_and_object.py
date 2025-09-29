# Class and Object

class Car:
	def __init__(self, brand, model):
		self.brand = brand
		self.model = model

	def show(self):
		print(f"Car: {self.brand} {self.model}")

# Creating Objects
c1 = Car("Toyota", "Cololla")
c1.show() # Output: Car: Toyota Corolla
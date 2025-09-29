# Polymorphism

class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Bark")

# Polymorphism Example
for animal in [Cat(), Dog()]:
    animal.sound()

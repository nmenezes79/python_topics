# Inheritance

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):   # Dog inherits Animal
    def sound(self):
        print("Dog barks")

d = Dog()
d.sound()  # Output: Dog barks

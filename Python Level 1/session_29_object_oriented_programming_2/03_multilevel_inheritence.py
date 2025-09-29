# Base class
class Animal:
    def eat(self):
        print("Eating...")

# Derived class inheriting from Animal
class Mammal(Animal):
    def walk(self):
        print("Walking...")

# Derived class inheriting from Mammal (multilevel inheritance)
class Dog(Mammal):
    def bark(self):
        print("Barking...")

# Create object of Dog class
dog = Dog()

dog.eat()    # Inherited from Animal
dog.walk()   # Inherited from Mammal
dog.bark()   # Defined in Dog

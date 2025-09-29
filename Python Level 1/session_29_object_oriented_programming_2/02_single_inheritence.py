# Parent class
class Animal:
    def speak(self):
        print("Animal Speaks")

# Child class (inherits from Animal)
class Dog(Animal):
    def bark(self):
        print("Dog Barks")

# Creating an object of Dog
my_dog = Dog()

# Accessing methods
my_dog.speak()  # Inherited from Animal
my_dog.bark()   # Defined in Dog

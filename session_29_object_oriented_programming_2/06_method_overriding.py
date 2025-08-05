class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

# Create objects
animal = Animal()
dog = Dog()

animal.sound()  # Output: Animal makes a sound
dog.sound()     # Output: Dog barks

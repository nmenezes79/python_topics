# Parent class
class Animal:
    def sound(self):
        print("Some generic animal sound")

# Child class 1
class Dog(Animal):
    def sound(self):
        print("Bark")

# Child class 2
class Cat(Animal):
    def sound(self):
        print("Meow")

# Child class 3
class Cow(Animal):
    def sound(self):
        print("Moo")

# Creating objects of child classes
dog = Dog()
cat = Cat()
cow = Cow()

dog.sound()  # Output: Bark
cat.sound()  # Output: Meow
cow.sound()  # Output: Moo

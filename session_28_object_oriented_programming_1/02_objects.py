# Define a class
class Person:
    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create an object of the Person class
person1 = Person("Alice", 25)

# Access attributes and call methods
print(person1.name)   # Output: Alice
print(person1.age)    # Output: 25
person1.greet()       # Output: Hello, my name is Alice and I am 25 years old.

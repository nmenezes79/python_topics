class Student:
    def __init__(self, name, age):  # Constructor
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Creating an object of the class
s1 = Student("Alice", 20)

# Calling the method
s1.display_info()

class Student:
    # Constructor
    def __init__(self, name, age):
        self.name = name           # Public data member
        self.__age = age           # Private data member (note the double underscore)

    # Public method to access private data
    def show(self):
        print("Name:", self.name)
        print("Age:", self.__age)

    # Private method (just for demo; not used here)
    def __secret_method(self):
        print("This is a private method")

# Create an object
s1 = Student("Alice", 21)

# Access public data member
print(s1.name)  # Works fine

# Try to access private data member directly
# print(s1.__age)  # ❌ This will raise an AttributeError

# Correct way to access private data using public method
s1.show()

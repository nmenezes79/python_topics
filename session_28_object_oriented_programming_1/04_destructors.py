class Student:
    # Constructor
    def __init__(self, name):
        self.name = name
        print(f"Student {self.name} has been created.")

    # Destructor
    def __del__(self):
        print(f"Student {self.name} is being deleted.")

# Creating an object
s1 = Student("John")

# Deleting the object explicitly
del s1

# Output:
# Student John has been created.
# Student John is being deleted.

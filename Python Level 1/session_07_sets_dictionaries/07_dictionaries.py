# A dictionary in Python is an unordered,mutable collection of key-value pairs.
# It allows you to store and retrieve data efficiently using unique keys.
# Creating a Dictionary
# You can create a dictionary using {} or the dict() constructor.
# Using curly braces

student = {
    "name": "Alice",
    "age": 25,
    "course": "Computer Science"
}

# Using dict() constructor
employee = dict(name="John", age=30, department="HR")

# Accessing Values
# You can access values using keys.
print(student["name"])  # Alice
print(student.get("age"))  # 25

# Adding & Updating Values
# You can add new key-value pairs or update existing ones.
student["age"] = 26  # Updating value
student["grade"] = "A"  # Adding a new key-value pair
print(student.get("age")) # 26

# Removing Items
# You can remove elements using pop(), del, or popitem().
student.pop("grade")  # Removes "grade"
del student["age"]  # Deletes "age"
student.popitem()  # Removes the last inserted item (Python 3.7+)

# Looping Through a Dictionary
# You can iterate over keys, values, or key-value pairs.
for key in student:
    print(key, student[key])  # Key-Value

for value in student.values():
    print(value)  # Only values

for key, value in student.items():
    print(key, ":", value)  # Both keys and values
    
# Checking for a Key
# Use the in keyword.
if "name" in student:
    print("Key exists!")
    
# Dictionary Comprehension
# You can create dictionaries using comprehension.
squares = {x: x*x for x in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
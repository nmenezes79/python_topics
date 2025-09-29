# Deleting an Element from a List by Index
numbers = [10, 20, 30, 40, 50]
print(numbers)
del numbers[2]  # Deletes the element at index 2 (30)
print(numbers)  # Output: [10, 20, 40, 50]

# Deleting a Slice of Elements from a List
numbers = [10, 20, 30, 40, 50]
print(numbers)
del numbers[1:3]  # Deletes elements at index 1 and 2 (20, 30)
print(numbers)  # Output: [10, 40, 50]

# Deleting a Key-Value Pair from a Dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}
print(person)
del person["age"]  # Deletes the key 'age'
print(person)  # Output: {'name': 'Alice', 'city': 'New York'}

# Deleting an Entire List, Dictionary, or Variable
numbers = [1, 2, 3]
print(numbers)
del numbers  # Deletes the entire list
# print(numbers)  # Raises a NameError since 'numbers' no longer exists

# Deleting an Element from a Tuple (Not Possible Directly)
numbers = (10, 20, 30, 40)
print(numbers)
numbers = numbers[:2] + numbers[3:]  # Removes the element at index 2 (30)
print(numbers)  # Output: (10, 20, 40)
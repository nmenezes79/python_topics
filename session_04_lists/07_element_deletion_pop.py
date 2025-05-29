# Using pop() with a List
# The pop(index) method removes and returns the element at the specified index.
numbers = [10, 20, 30, 40, 50]
print(numbers)

# Removing the element at index 2 (30)
removed_element = numbers.pop(2)
print("Updated List:", numbers)  # Output: [10, 20, 40, 50]
print("Removed Element:", removed_element)  # Output: 30

# If no index is specified, pop() removes the last element.
numbers = [1, 2, 3, 4, 5]
last_element = numbers.pop()
print(numbers)  # Output: [1, 2, 3, 4]
print(last_element)  # Output: 5

# Using pop() with a Dictionary
# For dictionaries, pop(key) removes the specified key-value pair and returns the value.
student = {"name": "Alice", "age": 25, "grade": "A"}
print(student)

# Removing the key "age"
removed_value = student.pop("age")
print("Updated Dictionary:", student)  # Output: {'name': 'Alice', 'grade': 'A'}
print("Removed Value:", removed_value)  # Output: 25

# If the key does not exist, it raises a KeyError. You can provide a default value to avoid this:
removed_value = student.pop("score", "Not Found")
print(removed_value)  # Output: Not Found
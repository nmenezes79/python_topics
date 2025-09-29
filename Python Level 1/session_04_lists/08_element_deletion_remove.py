# Remove an element from a list
# Using remove(value): Removes the first occurrence of the specified value.
# Using pop(index): Removes an element at a specific index.
# Using del: Deletes an element at a given index.

# Using remove()
nums = [1, 2, 3, 4, 5]
nums.remove(3)  # Removes the first occurrence of 3
print(nums)  # Output: [1, 2, 4, 5]

# Using pop()
nums.pop(1)  # Removes the element at index 1
print(nums)  # Output: [1, 4, 5]

# Using del
del nums[0]  # Removes the first element
print(nums)  # Output: [4, 5]

# Remove a key from a dictionary
# Using del: Deletes a key-value pair.
# Using pop(key): Removes a key and returns its value.
# Using del
person = {"name": "John", "age": 30, "city": "New York"}
del person["age"]
print(person)  # Output: {'name': 'John', 'city': 'New York'}

# Using pop()
city = person.pop("city")
print(person)  # Output: {'name': 'John'}
print(city)  # Output: 'New York'

# Remove an element from a set
# Using remove(value): Removes an element (raises an error if not found).
# Using discard(value): Removes an element (does not raise an error if not found).
# Using pop(): Removes a random element.
# Using remove()
s = {1, 2, 3, 4}
s.remove(3)
print(s)  # Output: {1, 2, 4}

# Using discard()
s.discard(2)
print(s)  # Output: {1, 4}

# Using pop()
removed_element = s.pop()
print(s)  # Output: Remaining elements after popping
print(removed_element)  # Output: The removed element
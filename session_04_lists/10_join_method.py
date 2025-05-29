# Basic join() Example
words = ["Hello", "World", "Python"]
result = " ".join(words)
print(result)  # Output: Hello World Python

# Joining with Different Separators
# Using a comma
items = ["apple", "banana", "cherry"]
print(", ".join(items))  # Output: apple, banana, cherry

# Using a hyphen
numbers = ["1", "2", "3"]
print("-".join(numbers))  # Output: 1-2-3

# Joining Characters of a String
text = "Python"
print("-".join(text))  # Output: P-y-t-h-o-n

# Joining a List of Numbers (Convert to String First)
numbers = [1, 2, 3, 4]
result = " - ".join(map(str, numbers))
print(result)  # Output: 1 - 2 - 3 - 4
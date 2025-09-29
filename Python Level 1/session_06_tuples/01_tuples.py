# 01_tuples
# A tuple in Python is an ordered, immutable collection of elements.
# It is defined using parentheses () and can contain elements of different data types.

# Creating and Accessing a Tuple
# Creating a tuple
my_tuple = (10, 20, 30, "Hello", 3.14)

# Accessing elements using indexing
print(my_tuple[0]); # Output: 10
print(my_tuple[3]); # Output: Hello

# Tuple Packing and Unpacking
# Packing a tuple
person = ("Alice", 25, "Engineer")

# Unpacking a tuple
name, age, profession = person

print(name)       # Output: Alice
print(age)        # Output: 25
print(profession) # Output: Engineer

# Tuple slicing
numbers = (1, 2, 3, 4, 5, 6)

print(numbers[1:4])   # Output: (2, 3, 4)
print(numbers[:3])    # Output: (1, 2, 3)
print(numbers[-2:])   # Output: (5, 6)

# Iterating through a tuple
colors = ("red", "green", "blue")

for color in colors:
    print(color)

# Tuple methods
fruits = ("apple", "banana", "cherry", "apple")

print(fruits.count("apple"))  # Output: 2 (Counts occurrences of "apple")
print(fruits.index("banana")) # Output: 1 (Finds index of "banana")
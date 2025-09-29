# 05_tuples_assignment

# Basic Tuple Assignment
# Assigning a tuple
my_tuple = (10, 20, 30)
print(my_tuple)  # Output: (10, 20, 30)

# Tuple Packing and Unpacking
# Packing
numbers = 1, 2, 3  # Parentheses are optional
print(numbers)  # Output: (1, 2, 3)

# Unpacking
a, b, c = numbers
print(a, b, c)  # Output: 1 2 3

# Swapping Variables Using Tuples
x, y = 5, 10
x, y = y, x  # Swaps values
print(x, y)  # Output: 10 5

# Assigning a Tuple with the * Operator
a, *b, c = (1, 2, 3, 4, 5)
print(a)  # Output: 1
print(b)  # Output: [2, 3, 4] (List of middle elements)
print(c)  # Output: 5
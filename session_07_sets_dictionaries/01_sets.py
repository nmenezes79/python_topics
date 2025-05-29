# Creating a set
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Creating an empty set (Note: {} creates an empty dictionary)
empty_set = set()
print(type(empty_set))  # Output: <class 'set'>

# Adding Elements to a Set
my_set.add(6)  # Adding a single element
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

my_set.update([7, 8, 9])  # Adding multiple elements
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Removing Elements
my_set.remove(3)  # Removes 3; raises an error if not found
print(my_set)  # Output: {1, 2, 4, 5, 6, 7, 8, 9}

my_set.discard(10)  # No error if 10 is not in the set

# Set Operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)   # Union: {1, 2, 3, 4, 5, 6}
print(A & B)   # Intersection: {3, 4}
print(A - B)   # Difference: {1, 2}
print(A ^ B)   # Symmetric Difference: {1, 2, 5, 6}

# Checking Membership
print(2 in A)   # Output: True
print(5 not in A)  # Output: True

# Iterating Through a Set
for item in A:
    print(item)
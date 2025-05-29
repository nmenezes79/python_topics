# 07_inbuilt_functions
# Tuples in Python are immutable sequences that support various inbuilt functions.

# len(tuple)
# Returns the number of elements in the tuple
t = (10, 20, 30)
print(len(t))  # Output: 3

# max(tuple)
# Returns the maximum element from the tuple.
t = (5, 10, 15, 20)
print(max(t))  # Output: 20

# min(tuple)
# Returns the minimum element from the tuple.
t = (5, 10, 15, 20)
print(min(t))  # Output: 5

# sum(tuple)
# Returns the sum of all elements in the tuple.
t = (1, 2, 3, 4, 5)
print(sum(t))  # Output: 15

# tuple(iterable)
# Converts an iterable (like a list, string, or dictionary) into a tuple.
list = [1, 2, 3]
print(tuple(list))  # Output: (1, 2, 3)

# index(value, start, end)
# Returns the first occurrence index of a specified value.
t = (10, 20, 30, 40, 20)
print(t.index(20))  # Output: 1

# count(value)
# Returns the number of times a specified value appears in the tuple.
t = (1, 2, 2, 3, 2, 4)
print(t.count(2))  # Output: 3

# sorted(tuple)
# Returns a sorted list from the tuple.
t = (3, 1, 4, 2)
print(sorted(t))  # Output: [1, 2, 3, 4]

# any(tuple)
# Returns True if at least one element in the tuple is truthy.
t = (0, False, 5)
print(any(t))  # Output: True

# all(tuple)
# Returns True if all elements in the tuple are truthy.
t = (1, 2, 3, True)
print(all(t))  # Output: True
# The symmetric difference between two sets is the set of elements that 
# are in either of the sets but not in their intersection. 
# In Python, you can find the symmetric difference using
# Using the ^ operator (preferred for sets)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

sym_diff = set1 ^ set2
print(sym_diff)  # Output: {1, 2, 5, 6}

# Using the symmetric_difference() method
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

sym_diff = set1.symmetric_difference(set2)
print(sym_diff)  # Output: {1, 2, 5, 6}

# Using list comprehension (for lists)
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

sym_diff = list(set(list1) ^ set(list2))
print(sym_diff)  # Output: [1, 2, 5, 6]

# Using set operations manually
sym_diff = (set1 - set2) | (set2 - set1)
print(sym_diff)  # Output: {1, 2, 5, 6}

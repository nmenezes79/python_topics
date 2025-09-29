# Adding an Element to a Set
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}

# Adding Multiple Elements (Using update())
my_set = {1, 2, 3}
my_set.update([4, 5, 6])
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# Combining Two Sets (Using union() or |)
set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = set1.union(set2)  # OR set1 | set2
print(set3)  # Output: {1, 2, 3, 4, 5, 6}
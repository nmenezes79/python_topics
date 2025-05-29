# Using the | Operator
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1 | set2
print(union_set)  # Output: {1, 2, 3, 4, 5}

# Using the union() Method
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}

# Union of Multiple Sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {5, 6, 7}

union_set = set1.union(set2, set3)
print(union_set)  # Output: {1, 2, 3, 4, 5, 6, 7}
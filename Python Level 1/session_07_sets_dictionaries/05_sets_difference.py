# Using difference() method
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

diff = set1.difference(set2)  # Elements in set1 but not in set2
print(diff)  # Output: {1, 2}

# Using - Operator
diff = set1 - set2
print(diff)  # Output: {1, 2}
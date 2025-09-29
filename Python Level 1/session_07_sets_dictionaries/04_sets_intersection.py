# Using & Operator
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

intersection_set = set1 & set2
print(intersection_set)  # Output: {3, 4, 5}

# Using .intersection() Method
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {40, 30}

# Intersection of Multiple Sets
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
set3 = {4, 5, 6, 7, 8}

intersection_set = set1.intersection(set2, set3)
print(intersection_set)  # Output: {4, 5}
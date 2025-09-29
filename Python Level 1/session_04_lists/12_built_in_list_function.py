# Built In List Methods
# append()
numbers = [1, 2, 3]
numbers.append(4)
print(numbers) # Output: [1, 2, 3, 4]

# extend()
numbers = [1, 2, 3]
numbers.extend([4, 5, 6])
print(numbers) # Output: [1, 2, 3, 4, 5, 6]

# insert()
numbers = [1, 2, 4]
numbers.insert(2, 3)
print(numbers) # Output: [1, 2, 3, 4]

# remove()
numbers = [1, 2, 3, 2, 4]
numbers.remove(2)
print(numbers) # Output: [1, 3, 2, 4]

# pop()
numbers = [1, 2, 3]
print(numbers.pop()) # Output: 3
print(numbers) # Output: [1, 2]

# index()
numbers = [10, 20, 30, 40]
print(numbers.index(30)) # Output: 2

# count()
numbers = [1, 2, 2, 3, 4, 2]
print(numbers.count(2)) # Output: 3

# sort()
numbers = [5, 2, 9, 1]
numbers.sort()
print(numbers) # Output: [1, 2, 5, 9]

# reverse()
numbers = [1, 2, 3, 4]
numbers.reverse()
print(numbers) # Output: [4, 3, 2, 1]

# copy()
numbers = [1, 2, 3]
new_numbers = numbers.copy()
print(new_numbers) # Output: [1, 2, 3]

# clear()
numbers = [1, 2, 3]
numbers.clear()
print(numbers) # Output: []
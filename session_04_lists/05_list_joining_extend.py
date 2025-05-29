# In Python, the extend() method is used to join two lists by appending elements from an iterable 
# (like another list) to the end of the calling list
# extend() modifies the original list (list1) in place
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)  # Adding elements of list2 to list1
print(list1)  # Output: [1, 2, 3, 4, 5, 6]

# Example with Other Iterables
list1 = [1, 2, 3]

# Extending with a tuple
list1.extend((4, 5))
print(list1)  # Output: [1, 2, 3, 4, 5]

# Extending with a string (adds each character)
list1.extend("67")
print(list1)  # Output: [1, 2, 3, 4, 5, '6', '7']
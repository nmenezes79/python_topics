# 04_tuples_deleting

# In Python, tuples are immutable, meaning their elements cannot be changed, added, or removed after creation. 
# However, you can delete an entire tuple using the del keyword.
# Creating a tuple
my_tuple = (10, 20, 30, 40)

# Deleting the entire tuple
del my_tuple

# Trying to access the tuple after deletion will raise an error
print(my_tuple)  # This will cause a NameError 

# Output: NameError: name 'my_tuple' is not defined
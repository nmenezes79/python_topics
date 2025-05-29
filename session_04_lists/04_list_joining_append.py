# Using append() to add elements to a list
# .append() is used to add an item to the list

# Creating an empty list
fruits = []
print(fruits)

# Appending elements to the list
fruits.append("Apple")
fruits.append("Banana")
fruits.append("Cherry")
print(fruits) # Output: ['Apple', 'Banana', 'Cherry']

# Using join() to combine a list of strings
# join() works with lists of strings and concatenates them using a specified separator
# Joining list elements into a single string with ', ' separator
fruits_string = ", ".join(fruits)
print(fruits_string)  # Output: Apple, Banana, Cherry
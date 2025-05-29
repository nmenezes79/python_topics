# In Python, key values typically refer to key-value pairs used in dictionaries (dict). 
# Dictionaries store data in a {key: value} format, where each key is unique,
# and each value is associated with a specific key.

# Dictionary Syntax:
my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# Accessing Values Using Keys
print(my_dict["name"])  # Output: Alice

# Adding or Updating Key-Value Pairs
my_dict["age"] = 26  # Updates the value of "age"
my_dict["country"] = "USA"  # Adds a new key-value pair

# Checking If a Key Exists
if "city" in my_dict:
    print("City exists!")
    
# Looping Through Key-Value Pairs
for key, value in my_dict.items():
    print(f"{key}: {value}")
    
# Removing a Key-Value Pair
my_dict.pop("age")  # Removes the "age" key and its value
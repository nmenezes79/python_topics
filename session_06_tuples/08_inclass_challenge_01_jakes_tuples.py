# Taking 5 string inputs from the user and storing them in a list
string_list = [input(f"Enter string {i+1}: ") for i in range(5)]

# Converting the list to a tuple
string_tuple = tuple(string_list)

# Checking if the conversion is successful
if isinstance(string_tuple, tuple):
    print("Conversion successful! The tuple is:")
    print(string_tuple)
else:
    print("Conversion failed!")

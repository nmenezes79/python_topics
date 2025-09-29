# Initialize an empty list
elements = []

# Loop to take 5 strings inputs from the user
for i in range(5):
	user_input = input(f"Enter String {i+1}: ")
	elements.append(user_input)

# Concatenate the elements at index 2 and 4
result = elements[1] + " " + elements[3]

# Print the concatenated result
print("Concatenated Result: ", result)
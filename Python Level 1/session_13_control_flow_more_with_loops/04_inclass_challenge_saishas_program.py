# Python program to convert a sentence to PascalCase

# Take input from the user
sentence = input("Enter a sentence: ")

# Initialize an empty string to store the result
result = ""

# Initialize a flag to track word beginnings
capitalize_next = True

# Loop through each character in the sentence
for char in sentence:
    # If the character is a space, skip it and set flag to capitalize next letter
    if char == " ":
        capitalize_next = True
        continue  # Skip the rest of the loop for spaces

    # Capitalize the character if it's the start of a new word
    if capitalize_next:
        result += char.upper()
        capitalize_next = False
    else:
        result += char.lower()

# Print the result
print("Converted Sentence:", result)

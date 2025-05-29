# String Slicing
# Define a String
text = "Python Programming"
print(text)

# Slicing Example
print(text[0:6]) # Output: "Python" (characters from index 0 to 5)
print(text[7:])  # Output: "Programming" (from index 7 to the end)
print(text[:6])  # Output: "Python" (from the start to index 5)
print(text[-11:-1]) # Output: "Programmin" (negative indexing)
print(text[::2]) # Output: "Pto rgamn" (every second character)
print(text[::-1])# Output: "gnimmargorP nohtyP" (reversed string)
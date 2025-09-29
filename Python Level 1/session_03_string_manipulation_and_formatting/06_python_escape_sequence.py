# Escape Sequence

# Newline (\n): Add a new line
print("Hello\nWorld!")
# Output:
# Hello
# World!

# Tab (\t): Add a tab space
print("Hello\tWorld!")
# Output: Hello    World!

# Backslash (\\): Prints a backslash
print("This is a backslash: \\")
# Output: This is a backslast: \

# Single Quote (\'): Prints a single quote inside single-quoted strings
print('It\'s a beautiful day!')
# Output: It's a beautiful day!

# Double Quote (\"): Prints a double quote inside double-quoted strings
print("He said, \"Python is great!\"")
# Output: He said, "Python is great!"

# Carriage Return (\r): Moves the cursor to the begning of the line
print("Hello\rWorld!")
# Output: World!

# Octal Value (\ooo): Represents a based on its octal value
print("\101") # octal value for 'A'
# Output: A

# Hexadecimal Value (\xhh): Represents a character based on its hexadecimal value
print("\x41") # Hexadecimal value for 'A'
# Output: A

# Unicode Character (\u or \U): Represents a unicode character 
print("\u263A") # Unicode for a imly face
# Output: ☺

# Raw String
print(r"C:\new_folder\test")
# Output: C:\new_folder\test
# F Strings

# Python f-strings (formatted string literals) are a way to embed expressions inside string literals using curly braces {}
name = "Alice"
age = 30
job = "Software Engineer"

# Using an f-string
greeting = f"Hello, my name is {name}. I am {age} years old, and I work as a {job}."
print(greeting)

# Expressions in f-strings: You can directly embed expressions
x = 5
y = 3
print(f"The sum of {x} and {y} is {x + y}.")
# Output: The sum of 5 and 3 is 8.

# Formatting inside f-strings: You can use formatting options
pi = 3.14159
print(f"Pi rounded to 2 decimal places is {pi:.2f}.")
# Output: Pi rounded to 2 decimal places is 3.14.

# Function calls
def greet(name):
	return f"Hi {name}!"

print(f"{greet('Bob')}")
# Output: Hi Bob!
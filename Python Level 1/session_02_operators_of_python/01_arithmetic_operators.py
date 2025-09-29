# Arithmetic Operators

# Addition (+) Adds two numbers.
a = 10
b = 5
result = a + b
print("Addition:", result)  # Output: 15

# Subtraction (-) Subtracts the second number from the first.
result = a - b
print("Subtraction:", result)  # Output: 5

# Multiplication (*) Multiplies two numbers.
result = a * b
print("Multiplication:", result)  # Output: 50

# Division (/) Divides the first number by the second. Always returns a float.
result = a / b
print("Division:", result)  # Output: 2.0

# Floor Division (//) Divides and returns the integer part (truncates the decimal).
result = a // b
print("Floor Division:", result)  # Output: 2

# Modulus (%) Returns the remainder of the division.
result = a % b
print("Modulus:", result)  # Output: 0

# Exponentiation ()** Raises the first number to the power of the second.
result = a ** b
print("Exponentiation:", result)  # Output: 100000

# Example with multiple operators combined
x = 8
y = 3
result = (x + y) * y - x ** y // y
print("Combined operations result:", result) # Output: -137
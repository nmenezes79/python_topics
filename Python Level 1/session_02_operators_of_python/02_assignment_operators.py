# Assignment Operators

# Basic Assignment (=) Assigns the value on the right to the variable on the left.
x = 10
print("Basic Assignment:", x) # Output: 10

# Add and Assign (+=) Adds the right operand to the left operand and assigns the result to the left operand.
x = 5
x += 3
print("Add and Assign:", x) # Output: 8

# Subtract and Assign (-=) Subtracts the right operand from the left operand and assigns the result to the left operand.
x = 10
x -= 4
print("Subtract and Assign:", x) # Output: 6

# Multiply and Assign (*=) Multiplies the left operand by the right operand and assigns the result to the left operand.
x = 3
x *= 2
print("Multiply and Assign:", x) # Output: 6

# Divide and Assign (/=) Divides the left operand by the right operand and assigns the result to the left operand.
x = 10
x /= 2
print("Divide and Assign:", x) # Output: 5.0

# Floor Divide and Assign (//=) Performs floor division and assigns the result to the left operand.
x = 15
x //= 4
print("Floor Divide and Assign :", x) # Output: 3

# Modulus and Assign (%=) Calculates the modulus and assigns the result to the left operand.
x = 10
x %= 3
print(x) # Output: 1

# Exponentation and Assign (**=) Raises the left operand to the power of the right operand and assigns the result to the left operand.
x = 2
x **= 3
print(x) # Output: 8

# Bitwise OR and Assign (|=) Performs bitwise OR operation and assigns the result.
x = 5 # Binary: 101
x |= 3 # Binary: 011
print(x) # Output: 7 (Binary: 111)

# Bitwise AND and Assign (&=) Performs bitwise AND operation and assigns the result.
x = 5 # Binary: 101
x &= 3 # Binary: 011
print(x) # Output: 1 (Binary: 001)

# Bitwise XOR and Assign (^=) Performs bitwise XOR operation and assigns the result.
x = 5 # Binary: 101
x ^= 3 # Binary: 011
print(x) # Output: 6 (Binary: 110)

# Bitwise Left Shift and Assign (<<=) Shifts the bits to the left by the specified number of positions.
x = 5 # Binary: 101
x <<= 1
print(x) # Output: 10 (Binary: 1010)

# Bitwise Right Shift and Assign (>>=) Shifts the bits to the right by the specified number of positions.
x = 5 # Binary: 101
x >>= 1
print(x) # Output: 2 (Binary: 10)
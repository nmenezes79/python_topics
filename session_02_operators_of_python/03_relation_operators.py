# Relation Operators

# Equal to (==) Checks if two values are equal.
a = 100
b = 35
print(a == b) # False

# Greater than (>) Checks if the left operand is greater than the right.
a = 100
b = 35
print(a > b) # True

# Less than (<) Checks if the left operand is less than the right.
a = 100
b = 35
print(a < b) # False

# Greater than or equal to (>=) Checks if the left operand is greater than or equal to the right.
a = 100
b = 35
print(a >= b) # True

# Less than or equal to (<=) Checks if the left operand is less than or equal to the right.
a = 100
b = 35
print(a <= b) # False

# Not equal to (!=) Checks if two values are not equal.
a = 100
b = 35
print(a != b) # True

# Example with Variables
x = 10
y = 20

print(x == y) # False
print(x != y) # True
print(x > y) # False
print(x < y) # True
print(x >= 10) # True
print(y <= 20) # True

# Usage in Conditions
x = 15
if x >= 10:
	print("x is greater than or equal to 10")
else:
	print("x is less than 10")
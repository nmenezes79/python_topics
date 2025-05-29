# Logical Operators

# and Operator Returns True if both conditions are true.
a = 10
b = 20

# Example
if a > 5 and b > 15:
	print("Both conditions are True.")
else:
	print("At least 1 condition is False.")

# or Operator Returns True if at least one condition is true.
a = 10
b = 5

# Example
if a > 15 or b < 10:
	print("At least 1 condition is True.")
else:
	print("Both conditions are False.")

# not Operator Returns the opposite of the logical condition.
x = True

# Example
print("x is:", x)
print("not x is:", not x)

# Combining Logical Operators
a = 10
b = 20
c = 30

if(a > 5 and b > 15) or not (c < 25):
	print("Complex condition is True.")
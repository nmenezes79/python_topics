# Lambda Function
def double(x):
	return x * 2
print(double(5)) # Output: 10

double = lambda x: x * 2
print(double(5)) # Output: 10

numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, numbers))
print(squares) # Output: [1, 4, 9, 16]
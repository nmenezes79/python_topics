# Function to calculate factorial using recursion
def factorial(n):
	if n == 0 or n == 1:
		return 1
	return n * factorial(n - 1)

# Function to get the nth Fibonacci number using recursion
def fibonacci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	return fibonacci(n - 1) + fibonacci(n - 2)

# Function to print Fibonacci series using recursion (no loop)
def print_fibonacci_series(n, current = 0):
	if current < n:
		print(fibonacci(current), end="")
		print_fibonacci_series(n, current + 1)

# Main code
num = int(input("Enter a Number: "))
print(f"\nFactorial of {num} is: {factorial(num)}")
print(f"\nFibonacci series up to {num} terms:")
print_fibonacci_series(num)
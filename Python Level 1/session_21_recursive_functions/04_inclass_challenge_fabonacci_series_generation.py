# Recursive function to return nth Fibonacci number
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Prompt user for number of terms
num_terms = int(input("Enter the number of Fibonacci terms to display: "))

print("Fibonacci Series:")
for i in range(num_terms):
    print(fibonacci(i), end=" ")

# If user enters 6
# Fibonacci Series: 0 1 1 2 3 5
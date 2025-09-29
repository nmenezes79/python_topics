#  Factorial Calculation Using Iteration

def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Example usage
num = 5
print(f"Factorial of {num} is {factorial_iterative(num)}")

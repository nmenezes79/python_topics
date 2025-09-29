def recursive_sum(n):
    if n == 0:
        return 0
    else:
        return n + recursive_sum(n - 1)

# Example
num = int(input("Enter a positive number: "))
if num < 0:
    print("Please enter a positive number.")
else:
    result = recursive_sum(num)
    print(f"Sum of numbers from 1 to {num} is: {result}")

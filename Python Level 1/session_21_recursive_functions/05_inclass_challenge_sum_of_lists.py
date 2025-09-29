def recursive_sum(numbers):
    # Base case: if the list is empty, the sum is 0
    if not numbers:
        return 0
    else:
        # Recursive case: add the first number to the sum of the rest
        return numbers[0] + recursive_sum(numbers[1:])

# Example usage
my_list = [5, 10, 15, 20]
result = recursive_sum(my_list)
print("Sum of the list:", result)

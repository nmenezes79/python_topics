#  Number Classification

def classify_numbers(numbers):
    for num in numbers:
        if num > 0:
            print(f"{num} is positive.")
        elif num < 0:
            print(f"{num} is negative.")
        else:
            print(f"{num} is zero.")

# Example usage
num_list = [10, -5, 0, 3, -1]
classify_numbers(num_list)
# Inclass Challenge 1 Chirags Big Problem
def product_of_list(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

# Example usage:
my_list = [2, 3, 4, 5]
result = product_of_list(my_list)
print("Product of all elements:", result)
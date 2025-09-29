# Try with Finally Clause
def divide_numbers(a, b):
    try:
        result = a / b
        print("Result:", result)
    finally:
        print("Execution of finally block complete.")

# Test the function
divide_numbers(10, 2)
divide_numbers(10, 0)

# ZeroDivisionError: division by zero
# Groupby Task
# Function to add two numbers
def add_numbers(a, b):
    return a + b

# Function to subtract two numbers
def subtract_numbers(a, b):
    return a - b

# Function to multiply two numbers
def multiply_numbers(a, b):
    return a * b

# Main program - calls the functions
def main():
    # Inputs
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Using the functions
    sum_result = add_numbers(num1, num2)
    diff_result = subtract_numbers(num1, num2)
    prod_result = multiply_numbers(num1, num2)

    # Output the results
    print("\nResults:")
    print("Addition:", sum_result)
    print("Subtraction:", diff_result)
    print("Multiplication:", prod_result)

# Call the main function to run the program
main()

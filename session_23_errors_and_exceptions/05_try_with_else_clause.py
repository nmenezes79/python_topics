# Try with Else Clause
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    else:
        print("Division successful. The result is:", result)

# Test the function
divide(10, 2)   # No exception, so else runs
divide(10, 0)   # Triggers exception, else is skipped

# Division successful. The result is: 5.0
# Error: Cannot divide by zero.

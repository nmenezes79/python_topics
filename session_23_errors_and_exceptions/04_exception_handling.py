# Handling Division by Zero
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
    print("Result:", result)
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid integers.")
finally:
    print("Execution complete.")

# Enter the numerator: 10
# Enter the denominator: 0

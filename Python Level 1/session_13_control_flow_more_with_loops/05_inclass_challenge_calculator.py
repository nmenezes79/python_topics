print("Welcome to Rishi's Basic Calculator!")

while True:
    print("\nSelect operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulo (%)")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '6':
        print("Exiting calculator. Goodbye!")
        break

    # Get input numbers only if a valid operation is selected
    if choice in ['1', '2', '3', '4', '5']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        if choice == '1':
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif choice == '3':
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        elif choice == '4':
            if num2 != 0:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
            else:
                print("Error: Division by zero is not allowed.")
        elif choice == '5':
            if num2 != 0:
                print(f"Result: {num1} % {num2} = {num1 % num2}")
            else:
                print("Error: Modulo by zero is not allowed.")
    else:
        print("Invalid choice! Please select a valid operation (1-6).")

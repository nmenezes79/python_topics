def check_number_properties(number):
    # Check even or odd
    if number % 2 == 0:
        print(f"{number} is an Even number.")
    else:
        print(f"{number} is an Odd number.")
    
    # Check prime or composite
    if number < 2:
        print(f"{number} is neither Prime nor Composite.")
    else:
        is_prime = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            print(f"{number} is a Prime number.")
        else:
            print(f"{number} is a Composite number.")

# Input from the user
try:
    user_input = int(input("Enter a positive integer: "))
    if user_input < 0:
        print("Please enter a non-negative integer.")
    else:
        check_number_properties(user_input)
except ValueError:
    print("Invalid input. Please enter an integer.")

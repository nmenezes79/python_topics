# Compound Interest
# Function to calculate simple interest
def calculate_simple_interest(principal, rate, time):
    si = (principal * rate * time) / 100
    return si

# Function to calculate compound interest
def calculate_compound_interest(principal, rate, time):
    amount = principal * ((1 + rate / 100) ** time)
    ci = amount - principal
    return ci

# Main program to test the functions
p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time in years: "))

simple_interest = calculate_simple_interest(p, r, t)
compound_interest = calculate_compound_interest(p, r, t)

print(f"\nSimple Interest = {simple_interest:.2f}")
print(f"Compound Interest = {compound_interest:.2f}")

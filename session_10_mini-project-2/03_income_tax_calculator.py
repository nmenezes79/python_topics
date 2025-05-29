# Income Tax Calculator
print("=" * 40)
print(" " * 10 + "Income Tax Calculator")
print("=" * 40)

# Getting User Input
annual_income = float(input("\nEnter Your Total Annual Income (in $): "))

# Define Tax Slabs
tax = 0
if annual_income <= 250000:
	tax = 0 # No Tax For Income Upto $2,50,000
elif annual_income <= 500000:
	tax = (annual_income - 250000) * 0.05 # 5% Tax On Income Above $2,50,000
elif annual_income <= 1000000:
	tax = (annual_income - 500000) * 0.2 # 20% Tax On Income Above $5,00,000
else:
	tax = (250000 * 0.05) + (500000 * 0.2) + (annual_income - 1000000) * 0.3 # 30% Tax on Income above $10,00,000

# Display Results
print("\n" + "=" * 40)
print(f" Your Total Tax To Be Paid: ${tax:,.2f}")
print("=" * 40)
print("Thank you for Using the Income Tax Calculator!")
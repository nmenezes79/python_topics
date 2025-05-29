# Fertilizer cost calculator

def main():
	print("\nWelcme to the Fertilizer Cost Calculator!\n")

# Constants
radius = 7 # radius in meters
pi = 3.14  # approximate value of pi

# Calculate the area of the circular patch
area = pi * (radius ** 2)
print(f"The total area to be fertilized is: {area:.2f} square meters\n")

# Get user input for fertilizer cost per KG
cost_per_kg = float(input("Enter the cost of 1KG of fertilizer: "))

# Calculate total cost
total_cost = area * cost_per_kg
print(f"Total fertilizer required: {area:.2f} KG")
print(f"Total cost for fertilization: ${total_cost:.2f}\n")

# Check affordability
if total_cost > 150:
	print("The cost is too high. It is NOT affordable!\n")
else:
	print("The cost is affordable! You can proceed with fertilization. \n")

	print("thank you for using the fertilizer cost calculator!")

# Run the program
if __name__ == "_main_":
	main()
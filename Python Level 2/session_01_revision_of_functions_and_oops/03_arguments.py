# Arguments = Inputs to functions.

def calculate_total_cost(item_prices):
	total_cost = sum(item_prices)
	return total_cost

# Example
grocery_list_prices = [2.50, 1.99, 3.25, 4.50]
total_cost = calculate_total_cost(grocery_list_prices)
print("Total cost of Groceries:", total_cost)

# Default Argument
def greet(name = "World"):
	print(f"Hello, {name}!")

greet()
greet("Alice")

# Keyword Argument (Named Argument)
def describe_person(name, age, city):
	print(f"{name} is {age} years old and lives in {city}")

describe_person(name = "John", age = 30, city = "New York")
describe_person(city = "Paris", age = 25, name = "Bob")

# Positional Argument
def power_levels(hero, strength, agility, intelligence):
	print(f"{hero} has:")
	print(f"Strength: {strength}")
	print(f"Agility: {agility}")
	print(f"Intelligence: {intelligence}")

# Arbitrary Argument (Variable Length Argument)
def make_pizza(*toppings):
	print("Making a Pizza with the following Toppins:")
	for topping in toppings:
		print(f"- {topping}")

# Default Argument
greet() # Output: Hello, World!
greet("Alice") # Output: hello, Alice

# Keyword Argument (Named Arguments)
describe_person(name='Alice', age=30, city='Ney York')
describe_person(city='Paris', age=25, name='Bob')

# Positional Arguments
power_levels("Superman", 100, 90, 95)

# Arbitrary Arguments (Variable Length Arguments)
make_pizza("Cheese", "Mushrooms", "Pepperroni")
make_pizza("Onions", "Bell Peppers", "Pineapple", "Sausage")
# BMI Calculator

def calculate_bmi(weight, height):
	bmi = weight / (height ** 2)
	return bmi

# Take user input
weight = float(input("Enter your Weight in kg: "))
height = float(input("Enter youe height in meters: "))

# Calculate BMI
bmi = calculate_bmi(weight, height)

# determine BMI category
if bmi < 18.5:
	category = "Underweight"
elif 18.5 <= bmi < 24.9:
	category = "Normal Weight"
elif 25 <= bmi < 29.9:
	category = "Overweight"
else:
	category = "Obses"

print(f"Your BMI is: {bmi:.2f}")
print(f"You are classified as: {category}")
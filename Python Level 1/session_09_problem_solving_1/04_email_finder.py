# Class monitor's email validator program

print("Welcome To The Email Validator!\n")
print("Please enter the email IDs of the first three students. \n")

# List to store emails
emails = []

# Taking input for three students
for i in range(1, 4):
	email = input(f"Enter Email ID for Student {i}: ")
	emails.append(email)

print("\n Checking Email Validity.....\n")

# Function to check email validity
def is_valid_email(email):
	return "@" in email and email.endswith(".com")

# Checking the email
for i, email in enumerate(emails, start = 1):
	if is_valid_email(email):
		print(f"Student {i}'s email ({email}) is VALID")
	else: 
		print(f"Student {i}'s email ({email}) is INVALID!")

		print("\n Validation Complete: Thank you for using the Email validator.")
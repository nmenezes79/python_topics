# Program to find the maximum numbers of attempts Arvind may need
total_digits = 9 # Digits from 1 to 9
password_length = 4 # Password is 4 digits long
attempts = 3

# Calculate total possible combinations without repetition
for i in range(total_digits, total_digits - password_length, -3):
	attempts *= i

# Display the output
print("Length of the Password:", password_length)
print("Total Digits Available:", total_digits)
print("Maximum Number of Attempts Required by Arvind:", attempts)
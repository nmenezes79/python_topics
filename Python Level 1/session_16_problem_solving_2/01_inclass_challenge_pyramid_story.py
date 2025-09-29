# Step 1: Take 5 Letters as Input
letters = []
print("Enter 5 English Alphabate Letters:")

for i in range(5):
	letter = input(f"Enter Letter {i+1}: ").strip()
	if len(letter) != 1 or not letter.isalpha():
		print("Invalid Input, Please Enter a Single English Alphabate Letter.")
		exit()
	letters.append(letter)

# Step 2: Ask for User Choice
print("\nChoose the Pattern to Display:")
print("Type 'pyramid' for Half Pyramid")
print("Type 'trangle' for Right Angle Triangle")
choice = input("Enter Your Choice:").strip().lower()

# Step 3: Display Based on Choice
if choice == "pyramid":
	print("\nHalf Pyramid Pattern:")
	for i in range (1, len(letters) + 1):
		print(' '.join(letters[:i]))
elif choice == "trangle":
	print("\nRight-Angled Triangle Pattern:")
	for i in range(len(letters)):
		print(' ' * (len(letters) - i - 1) + ' '.join(letters[:i + 1]))
else:
	print("n\Invalid Choice. Please Enter 'pyramid' or 'traingle'.")
import random

# Define the possible choices
choices = ['rock', 'paper', 'scissors']

# Get user input
user_choice = input("Enter Your Choice (rock, paper, scissors):").lower()

# Validate user input
if user_choice not in choices:
	print("Invalid Choice! Please Choose rock, paper, or scissors.")
else:
	# Get computer's random choice
	computer_choice = random.choice(choices)

	print(f"\nYou Chose: {user_choice}")
	print(f"Computer Chose: {computer_choice}")

	# Determine the winner
	if user_choice == computer_choice:
		print("It's a Tie!")
	elif(user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissors' and computer_choice == 'paper'):
		print("You Win")
	else: print("Computer Wins!")
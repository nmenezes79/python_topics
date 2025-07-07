import random

# List of possible moves
moves = ['rock', 'paper', 'scissors']

# Scoreboard initialization
user_score = 0
computer_score = 0
draws = 0

# Ask the user how many times they want to play
while True:
    try:
        rounds = int(input("How many rounds would you like to play? "))
        if rounds <= 0:
            print("Please enter a positive number.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

print("\nLet's begin the game!\n")

# Start the game loop
for round_num in range(1, rounds + 1):
    print(f"\nRound {round_num} of {rounds}")
    user_move = input("Enter your move (rock, paper, scissors): ").lower()

    if user_move not in moves:
        print("Invalid move. Please enter rock, paper, or scissors.")
        continue

    computer_move = random.choice(moves)
    print(f"Computer chose: {computer_move}")

    # Determine the result
    if user_move == computer_move:
        print("It's a draw!")
        draws += 1
    elif(user_move == 'rock' and computer_move == 'scissors') or \
        (user_move == 'paper' and computer_move == 'rock') or \
        (user_move == 'scissors' and computer_move == 'paper'):
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

# Final Scoreboard
print("\n🎯 Game Over! Here's the final scoreboard:")
print(f"Your Wins:     {user_score}")
print(f"Computer Wins: {computer_score}")
print(f"Draws:         {draws}")

if user_score > computer_score:
    print("🎉 Congratulations, You won the game!")
elif computer_score > user_score:
    print("💻 Computer wins the game. Better luck next time!")
else:
    print("🤝 It's a tie game!")

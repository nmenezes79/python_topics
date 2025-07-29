# Here's how Nidhi can create her custom random module named myRandom with the required functions: evenChoice(), oddChoice(), and primeChoice().

# Step 1: Create the module file myRandom.py

import myRandom

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13]

print("Random Even Number:", myRandom.evenChoice(numbers))
print("Random Odd Number:", myRandom.oddChoice(numbers))
print("Random Prime Number:", myRandom.primeChoice(numbers))

# Output Example (will vary each time):
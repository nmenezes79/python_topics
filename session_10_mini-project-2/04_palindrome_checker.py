def check_palindrome():
	print("\n====== Palindrome Checker ======")
	word = input("Enter A Three Letter Word: ")

	if len(word) != 3:
		print("\n Please Enter Only A 3 Letter Word!")
		return

	reversed_word = word[::-1]

	print("\nOriginal Word :", word)
	print("Reversed Word :", reversed_word)

	if word == reversed_word:
		print("\n It's A Plaindrome!")
	else: 
		print("\n Not A Palindrome!")
check_palindrome()

# Palindrome 3 Letter Words : aha, bub, dad, dud, eve, eye, mom
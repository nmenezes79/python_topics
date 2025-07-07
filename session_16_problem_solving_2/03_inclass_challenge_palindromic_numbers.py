def is_palindrome(number):
    return str(number) == str(number)[::-1]

def find_palindromes(start, end):
    palindromes = []
    for num in range(start, end + 1):
        if is_palindrome(num):
            palindromes.append(num)
    return palindromes

# Input from user
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Get palindromic numbers
palindrome_numbers = find_palindromes(start, end)

# Display results
print(f"\nPalindromic numbers between {start} and {end}:")
print(palindrome_numbers)

print(f"\nTotal number of palindromic numbers: {len(palindrome_numbers)}")

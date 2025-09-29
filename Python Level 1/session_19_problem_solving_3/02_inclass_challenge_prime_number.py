# Function to check if a number is Prime
def is_prime(num):
	if num <= 1:
		return False
	for i in range(2, int(num**0.5) + 1):
		if num % i == 0:
		# More efficient than checking till num - 1
			return False
		return True

# Function to get all prime numbers in a given range
def get_primes_in_range(start, end):
	primes = []
	for number in range(start, end + 1):
		if is_prime(number):
			primes.append(number)
	return primes

# Input from the user
start_range = int(input("Enter the Start of the Range: "))
end_range = int(input("Enter the End of the Range: "))

# Get prime numbers and display
prime_numbers = get_primes_in_range(start_range, end_range)
print("Prime numbers in the range", start_range, "to", end_range, "are:")
print(prime_numbers)
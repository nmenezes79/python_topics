# Using sorted()
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers)  # Returns a new sorted list
print("Original:", numbers)
print("Sorted:", sorted_numbers)

# Using .sort()
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()  # Sorts the list in place
print("Sorted in place:", numbers)

# Sorting with Custom Key
words = ["apple", "banana", "cherry", "date"]
sorted_by_length = sorted(words, key=len)
print("Sorted by length:", sorted_by_length)

# Sorting in Descending Order
numbers = [5, 2, 9, 1, 5, 6]
sorted_desc = sorted(numbers, reverse=True)
print("Sorted Descending:", sorted_desc)
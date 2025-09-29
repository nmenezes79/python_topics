# Inclass Challenge 2 Pascals Triangle
def print_pascals_triangle(n):
    for i in range(n):
        # Print leading spaces for triangle shape
        print(' ' * (n - i - 1), end='')

        # Calculate and print the values in the ith row
        val = 1
        for j in range(i + 1):
            print(val, end=' ')
            # Update val for the next element in the row using Pascal's rule
            val = val * (i - j) // (j + 1)
        print()  # Newline after each row

# Get number of rows from the user
rows = int(input("Enter number of rows for Pascal's Triangle: "))
print_pascals_triangle(rows)
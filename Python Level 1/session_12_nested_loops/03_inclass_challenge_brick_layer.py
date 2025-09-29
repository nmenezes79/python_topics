# Dimensions of the floor
rows = 9      # Number of rows (height)
columns = 12  # Number of columns (width)

# Loop through each row
for i in range(rows):
    # Loop through each column in the current row
    for j in range(columns):
        print("*", end=" ")
    print()  # Move to the next line after each row

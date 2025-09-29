# Dimensions of the cube
layers = 6     # Height (z-axis)
rows = 6       # Rows (y-axis)
columns = 6    # Columns (x-axis)

# Initialize brick counter
brick_count = 0

# Loop through each layer
for z in range(layers):
    # Loop through each row in the layer
    for y in range(rows):
        # Loop through each column in the row
        for x in range(columns):
            brick_count += 1

# Print the total number of bricks
print("Total number of bricks:", brick_count)

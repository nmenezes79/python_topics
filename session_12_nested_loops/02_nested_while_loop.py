# Print multiplication tables from 1 to 3
i = 1
while i <= 3:
    j = 1
    while j <= 5:
        print(f"{i} x {j} = {i*j}")
        j += 1
    print()  # Empty line between tables
    i += 1
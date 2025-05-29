# The continue statement skips the current iteration and moves to the next one.
for num in range(1, 6):
    if num == 3:
        print("Skipping", num)
        continue
    print("Current number:", num)

# Hollow Rectangle Pattern
def hollow_rectangle_pattern(rows, cols):
    for i in range(1, rows + 1):
        if i == 1 or i == rows:
            print('*' * cols)
        else:
            print('*' + ' ' * (cols - 2) + '*')

hollow_rectangle_pattern(4, 5)

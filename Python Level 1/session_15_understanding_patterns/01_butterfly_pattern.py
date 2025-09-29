# Butterfly Pattern
def butterfly_pattern(n):
    for i in range(1, n + 1):
        print('*' * i + ' ' * (2 * (n - i)) + '*' * i)
    for i in range(n, 0, -1):
        print('*' * i + ' ' * (2 * (n - i)) + '*' * i)

butterfly_pattern(5)

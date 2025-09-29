# Pyramid Pattern
def pyramid_pattern(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '* ' * i)

pyramid_pattern(5)

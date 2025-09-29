# Full Pyramid Pattern
def full_pyramid_pattern(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '* ' * i)

full_pyramid_pattern(5)

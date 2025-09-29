# myRandom.py

import random

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def evenChoice(lst):
    evens = [num for num in lst if num % 2 == 0]
    if evens:
        return random.choice(evens)
    else:
        return None

def oddChoice(lst):
    odds = [num for num in lst if num % 2 != 0]
    if odds:
        return random.choice(odds)
    else:
        return None

def primeChoice(lst):
    primes = [num for num in lst if is_prime(num)]
    if primes:
        return random.choice(primes)
    else:
        return None

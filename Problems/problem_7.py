# Problem 7: 10001st Prime

import math


def is_prime(num):
    """Return if 'num' is prime."""
    if num < 2:
        return False
    elif num == 2:
        return True
    elif not any([num % i == 0 for i in range(2, math.ceil(math.sqrt(num)) + 1)]):
        return True
    else:
        return False


def nth_prime(N):
    """Return the 'Nth' prime number."""
    prime_count = 0
    test = 2

    while prime_count < N:
        if is_prime(test):
            prime_count += 1
        test += 1


print(nth_prime(10001))

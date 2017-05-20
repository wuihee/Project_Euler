# Problem 10: Summation of Primes


def sieve(num):
    """Uses the Sieve of Erastosthenes to calculate all primes up to 'num'."""
    A = [True for i in range(num)]

    for i in range(2, int(num ** 0.5)):  # Square root as j starts at i ** 2.
        if A[i] is True:
            for j in range(i ** 2, len(A), i):  # The first multiple is i ** 2.
                A[j] = False  # Change all multiples to False

    return [i for i in range(len(A)) if A[i] is True][2:]  # Remove 0 and 1.


print(sum(sieve(2000000)))

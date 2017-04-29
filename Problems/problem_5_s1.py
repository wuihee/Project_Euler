# Problem 5: Smallest Multiple


def factorize(num):
    """Accept a number and return its prime factors."""
    factors = []
    divisor = 2

    while num >= divisor:  # Divide until 'num == 1'.
        # Continue to divide 'num' by 'divisor' until no longer divisible.
        if num % divisor == 0:
            factors.append(divisor)
            num /= divisor
        else:
            divisor += 1

    return factors


def union(arr_1, arr_2):
    """Find the union between two lists."""
    unique = list(set(arr_1 + arr_2))  # Merge two lists into a set to remove repetitions.
    union_arr = []
    count = 0

    for n in unique:
        count = max(arr_1.count(n), arr_2.count(n))  # 'count' refers to the largest occurence of 'n' in the two lists.
        union_arr.extend([n for i in range(count)])  # Extend 'union_arr' with a list containing 'count' number of number 'n'.

    return union_arr


def multiply(nums):
    """Given a list of numbers, multiply them together."""
    first, *rest = nums

    for i in rest:
        first *= i

    return first


def smallest_multiple(nums):
    """
    Accept a list of numbers and find the smallest multiple.
    Remove redundant numbers through the union of prime factors.
    Returns the product of 'primes'.
    """
    primes = []

    for i in nums:
        primes = union(primes, factorize(i))

    return multiply(primes)


print(smallest_multiple(list(range(1, 21))))

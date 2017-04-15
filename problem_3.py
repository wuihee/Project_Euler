# Largest Prime Factor


def largest_prime_factor(num):
    divisor = 2

    while divisor <= num:
        if num % divisor == 0:
            num /= divisor
        else:
            divisor += 1

    return divisor


print(largest_prime_factor(600851475143))

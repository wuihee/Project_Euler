# Multiples of 3 and 5


def multiples_sum(n):
    return sum([i for i in range(n) if i % 3 == 0 or i % 5 == 0])


print(multiples_sum(1000))

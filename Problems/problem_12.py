# Problem 12: Highly Divisible Triangle Number


def triangle_numbers():
    num = 0
    count = 1

    while True:
        num += count
        count += 1
        yield num


def factorize(num):
    pass

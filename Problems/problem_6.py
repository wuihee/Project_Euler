# Problem 6: Sum Square Difference


def sum_square(num):
    total_sum = sum([i for i in range(1, num + 1)])
    squared_sum = total_sum ** 2
    return squared_sum


def square_sum(num):
    total_sum = sum([i ** 2 for i in range(1, num + 1)])
    return total_sum


print(sum_square(100) - square_sum(100))

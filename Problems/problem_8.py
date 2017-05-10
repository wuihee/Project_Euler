# Problem 8: Largest Product In a Series


def product(numbers):
    """Given a string of numbers, find the product of each number."""
    total = 1

    for i in numbers:
        total *= int(i)

    return total


number = "".join([line.rstrip() for line in open("Files/p8_number.txt")])
largest_product = 0

for i in range(len(number) - 13):
    test = product(number[i:i + 13])
    if test > largest_product:
        largest_product = test

print(largest_product)

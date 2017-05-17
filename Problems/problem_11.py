# Problem 11: Largest Product In a Grid


def product_of(nums):
    first, *rest = nums

    for n in rest:
        first *= n

    return first


grid = [[int(n) for n in line.rstrip().split()] for line in open("Files/p11_numbers.txt")]
grid_len = len(grid)
row_len = len(grid[0])
seq_len = 4
largest = 0

# Vertical
for row in range(grid_len - 3):
    for col in range(row_len):
        seq = [grid[row + i][col] for i in range(seq_len)]
        product = product_of(seq)
        if product > largest:
            largest = product

# Horizontal
for row in range(grid_len):
    for col in range(row_len - 3):
        seq = [grid[row][col + i] for i in range(seq_len)]
        product = product_of(seq)
        if product > largest:
            largest = product

# Right Diagonal
for row in range(grid_len - 3):
    for col in range(row_len - 3):
        seq = [grid[row + i][col + i] for i in range(seq_len)]
        product = product_of(seq)
        if product > largest:
            largest = product

# Left Diagonal
for row in range(grid_len - 3):
    for col in range(3, row_len):
        seq = [grid[row + i][col - i] for i in range(seq_len)]
        print(seq)
        product = product_of(seq)
        if product > largest:
            largest = product

print(largest)

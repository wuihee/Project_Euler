# Problem 9: Special Pythagorean Triplet


def is_pythagorean(a, b, c):
    """Check if 'a', 'b', and 'c' are pythagorean"""
    if a ** 2 + b ** 2 == c ** 2:
        return True
    else:
        return False


for a in range(1, 332):  # Max 'a' = 332
    for b in range(a, 499):  # Max 'b' = 499
        c = 1000 - a - b
        if is_pythagorean(a, b, c):
            print(a * b * c)
            break

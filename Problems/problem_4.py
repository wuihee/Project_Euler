# Problem 4: Largest Palindrome Product


def is_palindrome(num):
    """Check if 'num' is equal to 'num' reversed."""
    num = str(num)
    return True if num == num[::-1] else False


palindromes = []

for i in range(999, 0, -1):
    for j in range(999, 0, -1):
        check = i * j
        if is_palindrome(check):
            palindromes.append(check)

print(max(palindromes))

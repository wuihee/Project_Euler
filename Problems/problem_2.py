# Problem 2: Even Fibonacci Numbers


def fibonacci_seq(limit):
    total = 0
    curr_term = 1
    prev_term = 1

    while curr_term < limit:
        if curr_term % 2 == 0:
            total += curr_term
        prev_term, curr_term = curr_term, curr_term + prev_term

    return total


print(fibonacci_seq(4000000))

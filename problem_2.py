# Even fibonacci numbers


def fibonacci_seq():
    seq = [1, 2]
    while seq[1] <= 100:
        seq.append(seq[-2] + seq[-1])

    return seq


print(fibonacci_seq())

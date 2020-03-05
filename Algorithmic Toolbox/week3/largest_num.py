# python3


def is_greater_or_equal(digit, max_digit):
    n = int(''.join([str(digit), str(max_digit)]))
    n1 = int(''.join([str(max_digit), str(digit)]))

    if n >= n1:
        return True
    else:
        return False


def naive_largest_num(n):
    ln = []
    max_index = None
    while len(n) >= 1:
        for i in range(len(n)):
            if max_index is None or is_greater_or_equal(n[i], n[max_index]):
                max_index = i

        ln.append(str(n.pop(max_index)))
        max_index = None

    return int(''.join(ln))


if __name__ == "__main__":
    num = int(input())
    n = [int(i) for i in input().split()]
    print(naive_largest_num(n))

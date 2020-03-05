# python3


def max_prizes(n):
    prizes, i = [], 1
    while n > 0:
        if i <= n:
            n -= i
            prizes.append(i)
            i += 1
        else:
            prizes[-1] += n
            n = 0

    return prizes


if __name__ == "__main__":
    n = int(input())

    prizes = max_prizes(n)
    print(len(prizes))
    [print(i) for i in prizes]
    print()

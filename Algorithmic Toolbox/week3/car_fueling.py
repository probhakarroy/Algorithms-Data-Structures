# python3


def min_refills(x, n, L):
    num_refills, current_refill = 0, 0
    while current_refill <= n:
        last_refill = current_refill

        while current_refill <= n and x[current_refill+1] - x[last_refill] <= L:
            current_refill += 1

        if current_refill == last_refill:
            return -1

        if current_refill <= n:
            num_refills += 1

    return num_refills


if __name__ == "__main__":
    d = int(input())
    m = int(input())
    n = int(input())
    x = [int(i) for i in input().split()]

    x.insert(0, 0)
    x.append(d)
    print(min_refills(x, n, m))
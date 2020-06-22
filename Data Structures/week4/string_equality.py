# python3
import random


def precompute_hashes(T, x, m1, m2):
    h1, h2 = [None]*(len(T)+1), [None]*(len(T)+1)
    h1[0], h2[0] = 0, 0

    for i in range(1, len(T)+1):
        h1[i] = (x*h1[i-1] + ord(T[i-1])) % m1
        h2[i] = (x*h2[i-1] + ord(T[i-1])) % m2

    return h1, h2


if __name__ == "__main__":
    T = input()
    q = int(input())

    m1, m2 = 1000000007, 1000000009
    x = random.randint(1, 1000000006)
    h1, h2 = precompute_hashes(T, x, m1, m2)


    for i in range(q):
        a, b, l = [int(i) for i in input().split()]
        y = x**l
        aHash1 = (h1[a + l] - (y * h1[a])) % m1
        bHash1 = (h1[b + l] - (y * h1[b])) % m1
        aHash2 = (h2[a + l] - (y * h2[a])) % m2
        bHash2 = (h2[b + l] - (y * h2[b])) % m2

        if aHash1 == bHash1 and aHash2 == bHash2:
            print('Yes')
        else:
            print('No')

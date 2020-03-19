# python3
import random


def naive_lottery(segments, points):
    payoff = []

    for i in points:
        count = 0
        for j in segments:
            if i >= j[0] and i <= j[1]:
                count += 1

        payoff.append(count)

    return payoff


def lottery(s, p, segments, points):
    count = [0]*len(points)
    pass


def lottery_count(A):
    n = len(A)
    if n <= 1:
        return A

    mid = n//2
    B = lottery_count(A[:mid])
    C = lottery_count(A[mid:])
    A_dash = lottery_merge(B, C)

    return A_dash


def lottery_merge(B, C):
    D = []
    i = j = 0

    while i < len(B) and j < len(C):
        if isinstance(B[i], list) and isinstance(C[j], list):
            if B[i][1] <= C[j][0]:
                D.append(B[i])
                i += 1
            else:
                D.append(C[j])
                j += 1
        elif isinstance(B[i], list):
            if B[i][1] < C[j]:
                D.append(B[i])
                i += 1
            else:
                D.append(C[j])
                j += 1

    while i < len(B):
        D.append(B[i])
        i += 1

    while j < len(C):
        D.append(C[j])
        j += 1

    return D


if __name__ == "__main__":
    s, p = [int(i) for i in input().split()]
    segments = [[int(i) for i in input().split()] for j in range(s)]
    points = [int(i) for i in input().split()]

    # print(naive_lottery(segments, points))
    # payoff = lottery(s, p, segments, points)
    # [print(i, end=' ') for i in payoff]
    # print()

# python3
import random


def naive_inversion(A):
    n_inversion = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i] > A[j]:
                n_inversion += 1

    return n_inversion


def inversion_dnc(A):
    n = len(A)
    if n <= 1:
        return 0, A

    m = n//2
    i1, B = inversion_dnc(A[:m])
    i2, C = inversion_dnc(A[m:])
    i, A_dash = inversion_merge(B, C)

    return (i+i1+i2), A_dash


def inversion_merge(B, C):
    D = [0 for i in range(len(B)+len(C))]
    i = j = k = 0
    n_inversion = 0

    while i < len(B) and j < len(C):
        if B[i] <= C[j]:
            D[k] = B[i]
            i += 1
            k += 1
        else:
            D[k] = C[j]
            j += 1
            k += 1
            n_inversion += len(B)-i

    while i < len(B):
        D[k] = B[i]
        i += 1
        k += 1

    while j < len(C):
        D[k] = C[j]
        j += 1
        k += 1

    return n_inversion, D


def stress_test(N, M):
    while True:
        n = random.randint(1, N)
        arr = [random.randint(1, M) for i in range(n)]
        print(arr, end=' -> ')

        result1 = naive_inversion(arr)
        result2, _ = inversion_dnc(arr)

        if result1 == result2:
            print('PASS')
        else:
            print('FAIL!\tnaive: {}\tefficient: {}'.format(result1, result2))
            break


if __name__ == "__main__":
    n = int(input())
    arr = [int(i) for i in input().split()]

    n_inversions, _ = inversion_dnc(arr)
    print(n_inversions)

    # stress_test(10**3, 10**9)

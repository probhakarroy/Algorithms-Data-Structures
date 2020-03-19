# python3
import random


def quick_sort(A, l, r):
    if l >= r:
        return

    m = partition(A, l, r)
    quick_sort(A, l, m-1)
    quick_sort(A, m+1, r)


def partition(A, l, r):
    x = A[l]
    j = l

    for i in range(l+1, r+1):
        if A[i] <= x:
            j += 1
            A[j], A[i] = A[i], A[j]

    A[l], A[j] = A[j], A[l]

    return j


def randomized_quick_sort(A, l, r):
    if l >= r:
        return A

    k = random.randint(l, r)
    A[l], A[k] = A[k], A[l]

    m1, m2 = partition3(A, l, r)
    randomized_quick_sort(A, l, m1-1)
    randomized_quick_sort(A, m2+1, r)


def partition3(A, l, r):
    x = A[l]
    j = l

    # for m1
    for i in range(l+1, r+1):
        if A[i] < x:
            j += 1
            A[j], A[i] = A[i], A[j]

    A[l], A[j] = A[j], A[l]

    # for m2
    k = j
    for i in range(j+1, r+1):
        if A[i] == x:
            k += 1
            A[k], A[i] = A[i], A[k]

    return j, k


def stress_test(N, M):
    while True:
        n = random.randint(1, N)
        arr = [random.randint(1, M) for i in range(n)]
        print(n, arr, end=' -> ')

        result1 = sorted(arr)
        randomized_quick_sort(arr, 0, n-1)

        if result1 == arr:
            print('Pass')
        else:
            print('FAIL!\t naive: {}\tquick: {}'.format(result1, arr))
            break


if __name__ == "__main__":
    n = int(input())
    arr = [int(i) for i in input().split()]

    randomized_quick_sort(arr, 0, n-1)
    [print(i, end=' ') for i in arr]
    print()
    # stress_test(10**5, 10**9)

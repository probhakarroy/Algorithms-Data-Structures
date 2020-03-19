# python3
import random


def majority_elements_efficient(A):
    count = {i: 0 for i in A}
    for i in A:
        count[i] += 1

    if max(count.values()) > len(A)//2:
        return 0
    else:
        return -1


def majority_elements_dnc(A):
    n = len(A)
    if n <= 1:
        return -1
    elif n == 2:
        return A[0]

    mid = n//2
    left_element = majority_elements_dnc(A[:mid])
    right_element = majority_elements_dnc(A[mid:])

    lc = 0
    for i in A:
        if i == left_element:
            lc += 1

    if lc > n//2:
        return left_element

    rc = 0
    for i in A:
        if i == right_element:
            rc += 1

    if rc > n//2:
        return right_element

    return -1


def stress_test(M, N):
    while True:
        n = random.randint(1, M)
        arr = [random.randint(0, N) for i in range(n)]

        if majority_elements_efficient(arr) != -1:
            result1 = 1
        else:
            result1 = 0

        if majority_elements_dnc(arr) != -1:
            result2 = 1
        else:
            result2 = 0

        if result1 == result2:
            print('Pass')
        else:
            print('FAIL!\t naive: {}\tdnc: {}'.format(result1, result2))
            break


if __name__ == '__main__':
    n = int(input())
    arr = [int(i) for i in input().split()]

    # if majority_elements_efficient(arr) != -1:
    #     print(1)
    # else:
    #     print(0)

    if majority_elements_dnc(arr) != -1:
        print(1)
    else:
        print(0)

    # stress_test(10**5, 10**9)

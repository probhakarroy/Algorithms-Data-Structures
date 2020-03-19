# python3
import random


def naive_polynomial_multiplication(A, B, n):
    product = [0 for i in range(2*n-1)]

    for i in range(n):
        for j in range(n):
            product[i+j] += A[i]*B[j]

    return product


def naive_polynomial_multiplication_dnc(A, B, n, al, bl):
    product = [0 for i in range(2*n-1)]

    if n == 1:
        product[0] = A[al]*B[bl]
        return product

    product[0:n-1] = naive_polynomial_multiplication_dnc(A, B, n//2, al, bl)
    product[n:2*n-1] = naive_polynomial_multiplication_dnc(A, B, n//2, al+(n//2), bl+(n//2))

    D0E1 = naive_polynomial_multiplication_dnc(A, B, n//2, al, bl+(n//2))
    D1E0 = naive_polynomial_multiplication_dnc(A, B, n//2, al+(n//2), bl)

    for i in range(n-1):
        product[(n//2)+i] += (D0E1[i] + D1E0[i])

    return product


def karatsuba_algorithm(A, B, n, al, bl):
    product = [0 for i in range(2*n-1)]

    if n == 1:
        product[0] = A[al]*B[bl]
        return product

    D0E0 = karatsuba_algorithm(A, B, n//2, al, bl)
    D1E1 = karatsuba_algorithm(A, B, n//2, al+(n//2), bl+(n//2))
    product[0:n-1] = D0E0
    product[n:2*n-1] = D1E1

    D0_plus_D1 = [0 for i in range(n//2)]
    E0_plus_E1 = [0 for i in range(n//2)]
    for i in range(n//2):
        D0_plus_D1[i] = A[al+i] + A[al+(n//2)+i]
        E0_plus_E1[i] = B[bl+i] + B[bl+(n//2)+i]
    
    mid_term = karatsuba_algorithm(D0_plus_D1, E0_plus_E1, n//2, 0, 0)

    for i in range(n-1):
        product[(n//2)+i] += (mid_term[i] - (D0E0[i] + D1E1[i]))

    return product


def stress_test_naive(M, N):
    while True:
        n = 2**random.randint(1, N)

        A = [random.randint(0, M) for i in range(n)]
        B = [random.randint(0, M) for i in range(n)]
        print(A, B, end=' -> ')

        result1 = naive_polynomial_multiplication(A, B, len(A))
        result2 = naive_polynomial_multiplication_dnc(A, B, len(A), 0, 0)

        if result1 == result2:
            print('PASS')
        else:
            print('FAIL!\tnaive: {}\tefficient: {}'.format(result1, result2))


def stress_test(M, N):
    while True:
        n = 2**random.randint(1, N)

        A = [random.randint(0, M) for i in range(n)]
        B = [random.randint(0, M) for i in range(n)]
        print(A, B, end=' -> ')

        result1 = naive_polynomial_multiplication_dnc(A, B, len(A), 0, 0)
        result2 = karatsuba_algorithm(A, B, len(A), 0, 0)

        if result1 == result2:
            print('PASS')
        else:
            print('FAIL!\tnaive: {}\tefficient: {}'.format(result1, result2))


if __name__ == "__main__":
    # A = [int(i) for i in input().split()]
    # B = [int(i) for i in input().split()]

    # print(naive_polynomial_multiplication(A, B, len(A)))
    # print(naive_polynomial_multiplication_dnc(A, B, len(A), 0, 0))
    # print(karatsuba_algorithm(A, B, len(A), 0, 0))

    # stress_test_naive(10, 10)
    stress_test(10, 10)
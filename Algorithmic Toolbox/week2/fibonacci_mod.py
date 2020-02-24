# python3
import random


def fibonacci(n):
    if n <= 1:
        return n

    F = [0 for i in range(0, n+1)]
    F[0] = 0
    F[1] = 1

    for i in range(2, n+1):
        F[i] = F[i-1] + F[i-2]

    return F[n]


def fibonacci_mod(n, m):
    if n <= 1:
        return n

    F, i = [0, 1], 2

    while True:
        F.append((F[i-1] + F[i-2]) % m)

        if F[i] == 1 and F[i-1] == 0:
            break

        i += 1

    i -= 1

    return F[n % i]


# STRESS TESTS
def fibonacci_mod_stress_test(N, M):
    while True:
        n, m = [random.randint(0, N), random.randint(2, M)]
        print(n, m, end=' --> ')

        result1 = fibonacci(n) % m
        result2 = fibonacci_mod(n, m)

        if result1 == result2:
            print('PASS')
        else:
            print('Fail!\tsolution: {}\tnaive solution: {}'.format(result2, result1))
            break


if __name__ == "__main__":
    n, m = [int(i) for i in input().split()]
    print(fibonacci_mod(n, m))

    # STRESS TESTS
    # fibonacci_mod_stress_test(30000, 10**3)

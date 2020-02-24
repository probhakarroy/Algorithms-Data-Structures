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


def last_digit_fibonacci(n):
    if n <= 1:
        return n

    F = [0 for i in range(0, n+1)]
    F[0] = 0
    F[1] = 1

    for i in range(2, n+1):
        F[i] = (F[i-1] + F[i-2]) % 10

    return F[n]


# STRESS TESTS
def last_digit_fibonacci_no_stress_test(N):
    while True:
        n = random.randint(0, N)
        print(n, end=' --> ')

        result1 = fibonacci(n) % 10
        result2 = last_digit_fibonacci(n)

        if result1 == result2:
            print('PASS')
        else:
            print('Fail!\tsolution: {}\tnaive solution: {}'.format(result2, result1))
            break


if __name__ == "__main__":
    n = int(input())
    print(last_digit_fibonacci(n))

    # STRESS TESTS
    # last_digit_fibonacci_no_stress_test(30000)

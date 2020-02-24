# python3
import random


def last_digit_sum_fibonacci(n):
    F, i = [0, 1], 2

    while True:
        F.append((F[i-1] + F[i-2]) % 10)

        if F[i] == 1 and F[i-1] == 0:
            break

        i += 1

    i -= 1
    sum = 0

    for j in range(0, n % i + 1):
        sum += F[j]

    return sum % 10


def last_digit_partial_sum_fibonacci(m, n):
    F, i = [0, 1], 2

    while True:
        F.append((F[i-1] + F[i-2]) % 10)

        if F[i] == 1 and F[i-1] == 0:
            break

        i += 1

    i -= 1
    sum, sum1 = 0, 0

    for j in range(0, (m-1) % i + 1):
        sum += F[j]

    for j in range(0, n % i + 1):
        sum1 += F[j]

    return (sum1 - sum) % 10


# STRESS TESTS
def last_digit_partial_sum_fibonacci_stress_test(N):
    while True:
        n, m = [random.randint(0, N) for i in range(2)]
        if n < m:
            n, m = m, n

        print(n, m, end=' --> ')

        result1 = (last_digit_sum_fibonacci(n) -
                   last_digit_sum_fibonacci(m - 1)) % 10
        result2 = last_digit_partial_sum_fibonacci(m, n)

        if result1 == result2:
            print('PASS')
        else:
            print('Fail!\tsolution: {}\tnaive solution: {}'.format(result2, result1))
            break


if __name__ == "__main__":
    m, n = [int(i) for i in input().split()]
    print(last_digit_partial_sum_fibonacci(m, n))

    # STRESS TESTS
    # last_digit_partial_sum_fibonacci_stress_test(10**14)

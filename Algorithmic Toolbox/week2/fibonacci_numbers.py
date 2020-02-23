# python3
import random


def naive_fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return naive_fibonacci_recursive(n-1) + naive_fibonacci_recursive(n-2)


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


def last_digit_sum_square_fibonacci(n):
    if n <= 1:
        return n

    F, i = [0, 1], 2

    while True:
        F.append((F[i-1] + F[i-2]) % 10)

        if F[i] == 1 and F[i-1] == 0:
            break

        i += 1

    i -= 1
    sum = 0

    for j in range(0, n % i + 1):
        sum += F[j]**2

    return sum % 10


# STRESS TESTS
def stress_test(N):
    while True:
        n = random.randint(0, N)
        print(n, end=' --> ')

        result1 = naive_fibonacci_recursive(n)
        result2 = fibonacci(n)

        if result1 == result2:
            print('PASS')
        else:
            print('Fail!\tsolution: {}\tnaive solution: {}'.format(result2, result1))
            break


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


def last_digit_sum_fibonacci_stress_test(N):
    while True:
        n = random.randint(0, N)
        print(n, end=' --> ')

        result1 = 0
        for i in range(n+1):
            result1 += last_digit_fibonacci(i)

        result1 %= 10
        result2 = last_digit_sum_fibonacci(n)

        if result1 == result2:
            print('PASS')
        else:
            print('Fail!\tsolution: {}\tnaive solution: {}'.format(result2, result1))
            break


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


def last_digit_sum_square_fibonacci_stress_test(N):
    while True:
        n = random.randint(0, N)
        print(n, end=' --> ')

        result1 = 0
        for i in range(n+1):
            result1 += last_digit_fibonacci(i)**2

        result1 %= 10
        result2 = last_digit_sum_square_fibonacci(n)

        if result1 == result2:
            print('PASS')
        else:
            print('Fail!\tsolution: {}\tnaive solution: {}'.format(result2, result1))
            break


if __name__ == "__main__":
    # n = int(input())
    # print(naive_fibonacci_recursive(n))
    # print(fibonacci(n))
    # print(last_digit_fibonacci(n))
    # print(last_digit_sum_fibonacci(n))
    # print(last_digit_sum_square_fibonacci(n))

    # n, m = [int(i) for i in input().split()]
    # print(fibonacci_mod(n, m))
    
    m, n = [int(i) for i in input().split()]
    print(last_digit_partial_sum_fibonacci(m, n))

    # STRESS TESTS
    # stress_test(30)
    # last_digit_fibonacci_no_stress_test(30000)
    # fibonacci_mod_stress_test(30000, 10**3)
    # last_digit_sum_fibonacci_stress_test(1000)
    # last_digit_partial_sum_fibonacci_stress_test(10**14)
    # last_digit_sum_square_fibonacci_stress_test(1000)

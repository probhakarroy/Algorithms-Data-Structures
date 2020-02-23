# python3
import random
import math


def naive_gcd(a, b):
    best = 0
    for i in range(1, a+b):
        if a % i == 0 and b % i == 0:
            best = i

    return best


def euclid_gcd(a, b):
    if b > a:
        a, b = b, a

    if b == 0:
        return a

    return euclid_gcd(b, a % b)


def extended_euclid_gcd(a, b):
    if b > a:
        a, b = b, a

    if b == 0:
        return (1, 0, a)

    x, y, d = extended_euclid_gcd(b, a % b)
    return (y, x - ((a//b)*y), d)


#STRESS TESTS
def stress_test(N):
    while True:
        a, b = [random.randint(0, N) for i in range(2)]
        print('a: {}\tb: {} --> '.format(a, b), end='')
        result1 = naive_gcd(a, b)
        result2 = euclid_gcd(a, b)

        if result1 == result2:
            print('PASS')
        else:
            print('FAIL! naive solution: {}\teuclid solution: {}'.format(
                result1, result2))
            break


def euclid_stress_test(N):
    while True:
        a, b = [random.randint(0, N) for i in range(2)]
        if b > a:
            a, b = b, a
        print('a: {}\tb: {} --> '.format(a, b), end='')

        result1 = euclid_gcd(a, b)
        x, y, result2 = extended_euclid_gcd(a, b)
        result3 = a*x + b*y

        if result1 == result2 and (result3 == result2):
            print('PASS')
        else:
            print('FAIL! naive solution: {}\teuclid solution: {}'.format(
                result1, result2))
            break


if __name__ == "__main__":
    a, b = [int(i) for i in input().split()]
    # print(naive_gcd(a, b))
    print(euclid_gcd(a, b))

    # x, y, d = extended_euclid_gcd(a, b)
    # print('a.{} + b.{} = {}'.format(x, y, d))

    #STRESS TESTS
    # stress_test(15000)
    # euclid_stress_test(10000000)

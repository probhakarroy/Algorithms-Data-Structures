# python3
import random


def naive_lcm(a, b):
    for i in range(1, a*b + 1):
        if i % a == 0 and i % b == 0:
            return i

    return a*b


def lcm(a, b):
    if b > a:
        a, b = b, a

    for i in range(a, a*b + 1, a):
        if i % b == 0:
            return i

    return a*b


def euclid_gcd(a, b):
    if b > a:
        a, b = b, a

    if b == 0:
        return a

    return euclid_gcd(b, a % b)


def efficient_lcm(a, b):
    return ((a*b)//euclid_gcd(a, b))


#STRESS TESTS
def stress_test(N):
    while True:
        a, b = [random.randint(1, N) for i in range(2)]
        print(a, b, end=' --> ')

        result1 = naive_lcm(a, b)
        result2 = lcm(a, b)

        if result1 == result2:
            print('PASS')
        else:
            print('FAIL!\tnaive solution: {}\tsolution: {}'.format(result1, result2))
            break


def euclid_stress_test(N):
    while True:
        a, b = [random.randint(1, N) for i in range(2)]
        print(a, b, end=' --> ')

        result1 = lcm(a, b)
        result2 = efficient_lcm(a, b)

        if result1 == result2:
            print('PASS')
        else:
            print('FAIL!\tnaive solution: {}\tsolution: {}'.format(result1, result2))
            break


if __name__ == "__main__":
    a, b = [int(i) for i in input().split()]
    # print(naive_lcm(a, b))
    print(lcm(a, b))
    # print(efficient_lcm(a, b))

    #STRESS TESTS
    # stress_test(173)
    # euclid_stress_test(10**7)

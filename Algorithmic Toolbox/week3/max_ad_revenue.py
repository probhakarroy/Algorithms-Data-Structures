# python3


def max_ad_revenue(n, a, b):
    sum = 0
    a.sort()
    b.sort()
    for i in range(n):
        sum += a[i]*b[i]
    
    return sum


if __name__ == "__main__":
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]

    print(max_ad_revenue(n, a, b))
# python3


def fractional_knapsack(n, W, v, w):
    V = 0
    for _ in range(n):
        if W == 0:
            return V

        index = 0
        for j in range(n):
            if (index is None) or (w[j] > 0 and v[j]/w[j] > v[index]/w[index]):
                index = j

        a = min(w[index], W)
        V += a*(v[index]/w[index])
        v[index] -= a*(v[index]/w[index])
        w[index] -= a
        W -= a

    return V


if __name__ == "__main__":
    n, W = [int(i) for i in input().split()]
    v, w = [], []

    for i in range(n):
        vi, wi = [int(i) for i in input().split()]
        v.append(vi)
        w.append(wi)

    print('{:.4f}'.format(fractional_knapsack(n, W, v, w)))
